# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _

STATE = [
    ('free', 'Free'),
    ('occupied', 'Occupied'),
]

class PowerSim(models.Model):
    _name = 'power.sim'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sims'

    name = fields.Char(string='Name', required=True)
    iccid = fields.Char("ICCID")
    access_ip = fields.Char("Access IP")
    access_port = fields.Char("Access port")
    control_port = fields.Char("Control port")
    active = fields.Boolean('Active', default=True)
    application_port = fields.Char("Application port")
    phone = fields.Char("Phone")
    state = fields.Char(
        string="State",
    )
    coverage = fields.Char("Coverage")


