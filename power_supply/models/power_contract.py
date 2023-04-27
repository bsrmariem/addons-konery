# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerContract(models.Model):
    _name = 'power.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Contracts'

    name = fields.Char(string='Name', required=True)
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    supply_id = fields.Many2one('power.supply', string='Power supply', store=True, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', related='supply_id.partner_id')

    contract_type = fields.Many2one('power.contract', string='Contract type')
    marketeer_id = fields.Many2one('res.partner', store=True, domain="[('is_marketeer','=',True)]", store=True)
    marketeer_contact_id = fields.Many2one('res.partner', store=True, string='Marketeer contact',
                                           domain="[('is_marketeer','=',True),('company_type','=','person')]")

    p1 = fields.Float(string='P1/Q', store=True)
    p2 = fields.Float(string='P2', store=True)
    p3 = fields.Float(string='P2', store=True)
    p4 = fields.Float(string='P2', store=True)
    p5 = fields.Float(string='P2', store=True)
    p6 = fields.Float(string='P2', store=True)
    