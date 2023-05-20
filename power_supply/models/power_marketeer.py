# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerMarketeer(models.Model):
    _name = 'power.marketeer'
    _description = 'Power Marketeer'

    name = fields.Char(string='Name', required=True)
