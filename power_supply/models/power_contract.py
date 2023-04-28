# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _

class PowerContract(models.Model):
    _name = 'power.contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Contracts'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean('Active')
    date = fields.Date(string='Date contracted')
    date_start = fields.Date(string='Date start')
    date_end = fields.Date(string='Date end')
    supply_id = fields.Many2one('power.supply', string='Power supply', store=True, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', related='supply_id.partner_id')

    type_id = fields.Many2one('power.contract.type', string='Contract type')
    marketeer_id = fields.Many2one('res.partner', store=True, domain="[('is_marketeer','=',True)]")
    marketeer_contact_id = fields.Many2one('res.partner', store=True, string='Marketeer contact',
                                           domain="[('is_marketeer','=',True)]")

    origin_warranty = fields.Boolean('Origin warranty')
    compromise = fields.Boolean('Compromise')
    auto_renew = fields.Boolean('Auto renew')

    date_on = fields.Date(string='Activation date')
    p1 = fields.Float(string='P1/Q', store=True)
    p2 = fields.Float(string='P2', store=True)
    p3 = fields.Float(string='P3', store=True)
    p4 = fields.Float(string='P4', store=True)
    p5 = fields.Float(string='P5', store=True)
    p6 = fields.Float(string='P6', store=True)
    