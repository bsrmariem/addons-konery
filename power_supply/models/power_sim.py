# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
# VER CON PEDRO QUE LOS STATES NO SE IMPORTAN:
STATE = [('available','Available'),('used','Used'),('cancel','Cancel')]
COVERAGE = [('movistar','Movistar'),('Multi COB'),('orange','Orange'), ('telefonica','Telefonica')]

class PowerSim(models.Model):
    _name = 'power.sim'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sims'

    # ¿Porqué name y phone? name debería ser number y quitar phone
    name = fields.Char(string='Name', required=True)
    iccid = fields.Char("ICCID")
    access_ip = fields.Char("Access IP")
    access_port = fields.Char("Access port")
    control_port = fields.Char("Control port")
    active = fields.Boolean('Active', default=True)
    application_port = fields.Char("Application port")
    phone = fields.Char("Phone")

    # ¿Calculado para que cuando esté en uso en un ps el estado sea 'used'?
    state = fields.Selection(selection=STATE, string="State")
    coverage = fields.Selection(selection=COVERAGE, string="Coverage")

    # AÑADIR UN CAMPO O2M A DESTINOS SIM PARA SI HAY ALGO, EL ESTADO CAMBIE A USED:


