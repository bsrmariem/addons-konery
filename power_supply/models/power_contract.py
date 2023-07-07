# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from datetime import date, datetime

class PowerContract(models.Model):
    _name = "power.contract"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Power Contracts'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean('Active', default=True)
    date = fields.Date(string='Date contracted')
    date_begin = fields.Date(string='Date start', required=True)
    date_end = fields.Date(string='Date end', required=True)
    energy_type = fields.Selection([('electricity', 'Electricity'), ('gas', 'Gas')], string='Energy type')
    partner_id = fields.Many2one('res.partner', string='Customer',  store=True)
    company_group_id = fields.Many2one('res.partner', string='Holding', related='partner_id.company_group_id')

    supply_ids = fields.Many2many(
        comodel_name="power.supply",
        relation='power_supply_contract_rel',
        store=True, index=True, context={'active_test': False}
    )

    type_id = fields.Many2one('power.contract.type', string='Contract type')
    marketeer_id = fields.Many2one('power.marketeer', store=True)
    marketeer_contact_id = fields.Many2one('res.partner', store=True, string='Marketeer contact')

    origin_warranty = fields.Boolean('Origin warranty')
    compromise = fields.Boolean('Compromise')
    auto_renew = fields.Boolean('Auto renew')
    atr_detached = fields.Boolean('Detached ATR')
    description = fields.Text('Notes')

    @api.constrains('date_begin','date_end','supply_ids','date')
    def _check_date_begin_end(self):
        for record in self:
            # La fecha de contratación ha de ser anterior a la de inicio:
            if (record.date_begin < record.date):
                raise ValidationError('The hiring date must be prior to the start date')
            # Chequeo de contratos relacionados para no solapar fechas:
            if record.date_begin and record.date_end:
                # En el propio, si fecha inicio mayor que fin, no válido:
                if (record.date_begin > record.date_end):
                    raise ValidationError('Date end earlier than begin')
                # Chequeo del resto de contratos:
                for cup in record.supply_ids:
                    for co in cup.contract_ids:
                        if (co.date_begin) and (co.date_end) and (co.id != record.id):
                            # Si fecha inicio está comprendida entre rango comprarado, solapa:
                            if (record.date_begin < co.date_end) and (record.date_begin >= co.date_begin):
                                raise ValidationError('Begin date overlaped with other contract (actives or archived).')
                            # Si fecha fin entre rango comparado, solapa:
                            if (record.date_end <= co.date_end) and (record.date_end > co.date_begin):
                                raise ValidationError('End date overlaped with other contract (actives or archived).')
                            # Si inicio es anterior pero fin posterior al inicio, solapa:
                            if (record.date_begin <= co.date_begin) and (record.date_end > co.date_begin):
                                raise ValidationError(
                                    'Not valid period, check other contract dates for this Supply (actives or archived).')
