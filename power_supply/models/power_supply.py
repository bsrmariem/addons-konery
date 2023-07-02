# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class PowerSupply(models.Model):
    _name = "power.supply"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Power Supplies'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', store=True, default=True)
    energy_type = fields.Selection([('electricity','Electricity'),('gas','Gas')],string='Energy type')
    partner_id = fields.Many2one('res.partner', string='Customer', store=True, required="1")
    company_group_id = fields.Many2one('res.partner', string='Holding', related='partner_id.company_group_id')
    manager_id = fields.Many2one('res.users', string='Manager')
    salesman_id = fields.Many2one('res.users', string='Salesman')
    tax_exception = fields.Boolean('Tax exception', store=True)
    pricelist_id = fields.Many2one('power.pricelist', string='Pricelist', store=True)

    location = fields.Char('Location', store=True)
    location_map = fields.Many2one('res.partner', store=True, string='Map address')
    cups = fields.Char('CUPS', store=True, copy=False)
    annual_power = fields.Integer('Annual power (kWh)')
    tag_ids = fields.Many2many('power.tag', string='Tags', store=True)
    dealer_id = fields.Many2one('power.dealer', store=True)

    contract_ids = fields.Many2many(
        comodel_name='power.contract',
        relation='power_supply_contract_rel',
        store=True, copy=False, index=True, context={'active_test': False}
    )

    @api.depends('name', 'cups')
    def _compute_display_name(self):
        name = "/"
        if self.cups != "" and self.name != "":
            name = str(self.cups) + " " + str(self.name)
        self.display_name = name
    display_name = fields.Char(compute='_compute_display_name', recursive=True, store=True, index=True)

    power_electricity_ids = fields.One2many('power.power', 'supply_id', string='Electrical Power', store=True)
    power_gas_ids = fields.One2many('power.power', 'supply_id', string='Gas Power', store=True)
    saving_ids = fields.One2many('power.saving', 'supply_id', string='Savings', store=True)
    meter_owner = fields.Selection([('acquire','Acquired'),('rent','Rented')], store=True, string='Meter owner')

    @api.depends('power_electricity_ids', 'power_gas_ids', 'contract_ids')
    def _get_energy_type_readonly(self):
        total = False
        if (self.power_electricity_ids.ids) or (self.power_gas_ids) or (self.contract_ids):
            total = True
        self.energy_type_readonly = total
    energy_type_readonly = fields.Boolean('Energy type is readonly', compute='_get_energy_type_readonly')

    communication_ids = fields.One2many('power.communication','supply_id', string='Communications', store=True)


    @api.onchange('contract_ids')
    def _check_date_contracts(self):
        for record in self:
            subcon = []
            for li in record.contract_ids: subcon.append(li.id)
            for co in record.contract_ids:
                if (co.date_begin) and (co.date_end):
                    for sub in subcon:
                        corev = self.env['power.contract'].search([('id','=',sub)])
                        # Si fecha inicio está comprendida entre rango comprarado, solapa:
                        if (co.date_begin < corev.date_end) and (co.date_begin >= corev.date_begin):
                            raise ValidationError('Begin date overlaped with other contract (actives or archived).')
                        # Si fecha fin entre rango comparado, solapa:
                        if (co.date_end <= corev.date_end) and (co.date_end > corev.date_begin):
                            raise ValidationError('End date overlaped with other contract (actives or archived).')
                        # Si inicio es anterior pero fin posterior al inicio, solapa:
                        if (co.date_begin <= corev.date_begin) and (co.date_end > corev.date_begin):
                            raise ValidationError(
                                'Not valid period, check other contract dates for this Supply (actives or archived).')
                        # Si fecha inicio mayor que fin, no puede ser:
                        if (co.date_begin > co.date_end):
                            raise ValidationError('Date end earlier than begin')
#                        subcon.remove(sub)
