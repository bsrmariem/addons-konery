# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerDealer(models.Model):
    _name = 'power.dealer'
    _description = 'Power Dealers'

    name = fields.Char(string='Name', required=True)
