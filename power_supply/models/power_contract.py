# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class PowerContract(models.Model):
    _name = 'power.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Contracts'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean('Active', default=True)
    date = fields.Date(string='Date contracted')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    supply_id = fields.Many2one('power.supply', string='Power supply', store=True, required=True)
    energy_type = fields.Selection([('electricity', 'Electricity'), ('gas', 'Gas')], string='Energy type',
                                   related='supply_id.energy_type')
    partner_id = fields.Many2one('res.partner', string='Customer', related='supply_id.partner_id')
    company_group_id = fields.Many2one('res.partner', string='Holding', related='partner_id.company_group_id')
    cups = fields.Char('CUPS', related='supply_id.cups', store=True)

    type_id = fields.Many2one('power.contract.type', string='Contract type')
    marketeer_id = fields.Many2one('power.marketeer', store=True)
    marketeer_contact_id = fields.Many2one('res.partner', store=True, string='Marketeer contact')

    origin_warranty = fields.Boolean('Origin warranty')
    compromise = fields.Boolean('Compromise')
    auto_renew = fields.Boolean('Auto renew')
    atr_detached = fields.Boolean('Detached ATR')
    description = fields.Text('Notes')

    @api.onchange('date_start','date_end')
    def _check_valid_date(self):
        contracts = self.env['power.contract'].search([('id','!=',self.id),('supply_id','=',self.supply_id.id)])
        raise ValidationError(contracts)
