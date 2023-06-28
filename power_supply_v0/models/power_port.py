# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerPort(models.Model):
    _name = 'power.port'
    _description = 'Power Port'

    name = fields.Char(string='Name', required=True)
