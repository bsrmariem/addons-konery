# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerSupply(models.Model):
    _name = 'power.supply'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
    cups = fields.Char('CUPS', store=True)
    anual_power = fields.Integer('Anual power (kWh)')
    tag_ids = fields.Many2many('power.tag', string='Tags', store=True)
    dealer_id = fields.Many2one('power.dealer', store=True)

    monitor = fields.Boolean('Monitorized')
    monitor_type = fields.Selection([('gprs','GPRS'),('gsm','GSM'),('datadis','Datadis')])
    monitor_ip = fields.Char('IP')
    monitor_port = fields.Integer('Port')
    monitor_phone = fields.Char('Phone')
    link_address = fields.Char('Link address')

    meter = fields.Selection([('sold','Sold'),('exist','Exist'),('rent','Rented')])
    meter_note = fields.Char('Meter notes')
    contract_ids = fields.One2many('power.contract', 'supply_id', string='Contracts', store=True)
    power_electricity_ids = fields.One2many('power.power', 'supply_id', string='Electrical Power', store=True)
    power_gas_ids = fields.One2many('power.power', 'supply_id', string='Gas Power', store=True)
    saving_ids = fields.One2many('power.saving', 'supply_id', string='Savings', store=True)

    @api.depends('power_electricity_ids', 'power_gas_ids', 'contract_ids')
    def _get_energy_type_readonly(self):
        total = False
        if (self.power_electricity_ids.ids) or (self.power_gas_ids) or (self.contract_ids):
            total = True
        self.energy_type_readonly = total
    energy_type_readonly = fields.Boolean('Energy type is readonly', compute='_get_energy_type_readonly')

    communication_ids = fields.One2many('power.communication','supply_id', string='Communications', store=True)