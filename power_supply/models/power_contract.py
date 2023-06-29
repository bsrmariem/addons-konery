# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class PowerContract(models.Model):
    _name = 'power.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Contracts'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean('Active', default=True)
    date = fields.Date(string='Date contracted')
    date_start = fields.Date(string='Date start', required=True)
    date_end = fields.Date(string='Date end', required=True)
    energy_type = fields.Selection([('electricity', 'Electricity'), ('gas', 'Gas')], string='Energy type')
    partner_id = fields.Many2one('res.partner', string='Customer',  store=True)
    company_group_id = fields.Many2one('res.partner', string='Holding', related='partner_id.company_group_id')

    supply_ids = fields.Many2many(
        "power.supply",
        relation="power_supply_contract_rel",
        column1="contract_id",
        column2="supply_id",
        store=True,
    )

    type_id = fields.Many2one('power.contract.type', string='Contract type')
    marketeer_id = fields.Many2one('power.marketeer', store=True)
    marketeer_contact_id = fields.Many2one('res.partner', store=True, string='Marketeer contact')

    origin_warranty = fields.Boolean('Origin warranty')
    compromise = fields.Boolean('Compromise')
    auto_renew = fields.Boolean('Auto renew')
    atr_detached = fields.Boolean('Detached ATR')
    description = fields.Text('Notes')

    # Comentado porque no funciona, hay que hacer AcciónAutomática:
    #    @api.onchange('date_start','date_end', 'supply_id')
    def _check_valid_date(self):
        for record in self:
            if (record.id) and (record.supply_ids.ids):

                contracts = self.env['power.supply.contract.rel'].search(
                    [('supply_id', 'in', record.supply_ids.ids), ('contract_id', '!=', record.id),
                     ('contract_id.active', 'in', [True, False])]).contract_id

                for co in contracts:
                    if not (co.date_start) or not (co.date_end):
                        raise UserError(
                            'Before save this contract check previous to assign starting and ending dates (actives or archived).')
                    if (record.date_start < co.date_end) and (record.date_start > co.date_start):
                        raise UserError('Begin date overlaped with other contract (actives or archived).')
                    if (record.date_end < co.date_end) and (record.date_end > co.date_start):
                        raise UserError('End date overlaped with other contract (actives or archived).')
                    if (record.date_start < co.date_start) and (record.date_end > co.date_start):
                        raise UserError(
                            'Not valid period, check other contract dates for this Supply (actives or archived).')
                    if (record.date_start > record.date_end):
                        raise UserError('Date end earlier than begin')
