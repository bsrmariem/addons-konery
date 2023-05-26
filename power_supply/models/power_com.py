# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerCommunication(models.Model):
    _name = 'power.com'
    _description = 'Power Communication'

    name = fields.Char(string='Name', required=True)
