# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerSaving(models.Model):
    _name = 'power.saving'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Savings'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', required=True)
    supply_id = fields.Many2one('power.supply', string='Power supply', store=True, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', related='supply_id.partner_id')
    cups = fields.Char('CUPS', related='supply_id.cups', store=True)
    power_qty = fields.Integer('Power(kWh/Q)')
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one('res.currency', string='Currency', default=1)
