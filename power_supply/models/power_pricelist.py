# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerPricelist(models.Model):
    _name = 'power.pricelist'
    _description = 'Power Supplies'

    name = fields.Char(string='Name', required=True)
