# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerCommunication(models.Model):
    _name = 'power.communication'
    _description = 'Power Communication'

    name = fields.Char(string='Device name', required=True)
    supply_id = fields.Many2one('power.supply', string='Power supply', store=True, required=True)

    # METER:

    # COMM:
    sim_id = fields.Many2one('power.sim', string='SIM', store=True)
