# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _

class PowerPower(models.Model):
    _name = 'power.power'
    _description = 'Power Contract Powers'

    contract_id = fields.Many2one('power.contract', string='Contract', store=True, required=True)
    supply_id = fields.Many2one('power.supply', related='contract_id.supply_id', string='Supply', store=True)
    partner_id = fields.Many2one('res.partner', related='supply_id.partner_id', string='Customer', store=True)
    date_on = fields.Date(string='Activation date')
    p1 = fields.Float(string='P1/Q', store=True)
    p2 = fields.Float(string='P2', store=True)
    p3 = fields.Float(string='P3', store=True)
    p4 = fields.Float(string='P4', store=True)
    p5 = fields.Float(string='P5', store=True)
    p6 = fields.Float(string='P6', store=True)
