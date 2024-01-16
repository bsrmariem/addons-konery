# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerCoverage(models.Model):
    _name = 'power.coverage'
    _description = 'Power Coverage'

    name = fields.Char(string='Name', required=True)
