# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerPricelist(models.Model):
    _name = 'power.pricelist'
    _description = 'Power Pricelists'

    name = fields.Char(string='Name', required=True)
    energy_type = fields.Selection([('electricity','Electricity'),('gas','Gas')],string='Energy type',
                                   default='electricity', required=True)
