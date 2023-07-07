# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _

class PowerPower(models.Model):
    _name = 'power.power'
    _description = 'Power Contract Powers'

    supply_id = fields.Many2one('power.supply', string='Supply', store=True)
    energy_type = fields.Selection(string='Energy type', related='supply_id.energy_type')

    partner_id = fields.Many2one('res.partner', related='supply_id.partner_id', string='Customer', store=True)

    date_on = fields.Date(string='Activation date')
    qgas = fields.Float(string='Q (kWh/day)', store=True)
    p1 = fields.Float(string='P1 (kW)', store=True)
    p2 = fields.Float(string='P2 (kW)', store=True)
    p3 = fields.Float(string='P3 (kW)', store=True)
    p4 = fields.Float(string='P4 (kW)', store=True)
    p5 = fields.Float(string='P5 (kW)', store=True)
    p6 = fields.Float(string='P6 (kW)', store=True)

    @api.depends('supply_id', 'date_on')
    def _get_power_power_name(self):
        name = "/"
        if (self.supply_id.id) and (self.date_on):
            name = str(self.supply_id.name) + " > " + str(self.date_on)
        self.name = name
    name = fields.Char('Name', store=True, compute='_get_power_power_name')