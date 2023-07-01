# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
# VER CON PEDRO QUE LOS STATES NO SE IMPORTAN:
STATE = [('available','Available'),('used','Used')]

class PowerSim(models.Model):
    _name = 'power.sim'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sims'

    name = fields.Char(string='ICCID', required=True)
    access_ip = fields.Char("Access IP")
    access_port = fields.Integer("Access port")
    control_port = fields.Integer("Control port")
    active = fields.Boolean('Active', default=True)
    rs485_port = fields.Char("Port RS485")
    phone = fields.Char("Phone")
    coverage_id = fields.Many2one('power.coverage', string="Coverage", store=True)
    communication_ids = fields.One2many('power.communication', 'sim_id', string='Communication', store=True)

    def _get_sim_state(self):
        for record in self:
            state = 'available'
            if record.communication_ids.ids:
                state = 'used'
            record['state'] = state
    state = fields.Selection(selection=STATE, string="State", store=False, compute='_get_sim_state')
