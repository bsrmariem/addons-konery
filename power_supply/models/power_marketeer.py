# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerMarketeer(models.Model):
    _name = 'power.marketeer'
    _description = 'Power Marketeer'

    name = fields.Char(string='Name', required=True)
    street = fields.Char("Street")
    city = fields.Char("City")
    state = fields.Char("State")
    zip = fields.Char("Zip")
    active = fields.Boolean('Active', default=True)
    order_number = fields.Char("Order number")
    phone = fields.Char("Phone")
    sector = fields.Char("Sector")
    cif = fields.Char("CIF")
    status = fields.Char("Status")
    date_discharge = fields.Date(string='Date discharge')
    date_leaving = fields.Date(string='Date leaving')
    web = fields.Char("Web")