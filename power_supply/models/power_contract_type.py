# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerContractType(models.Model):
    _name = 'power.contract.type'
    _description = 'Power Contract Type'

    name = fields.Char(string='Name', required=True)
    