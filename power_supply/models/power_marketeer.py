# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerMarketeer(models.Model):
    _name = 'power.marketeer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
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
    vat = fields.Char("VAT")
    status = fields.Char("Status")
    date_discharge = fields.Date(string='Date discharge')
    date_leaving = fields.Date(string='Date leaving')
    web = fields.Char("Web")

    electricity = fields.Boolean('Electricity')
    gas = fields.Boolean('Gas')
    gas_sifco = fields.Char('Sifco')
    gas_sector = fields.Char('Ambito en gas')
    gas_phone = fields.Char('Gas phone')
    gas_date_discharge = fields.Date(string='Gas Date discharge')
    gas_date_leaving = fields.Date(string='Gas Date leaving')
    country = fields.Char('Country')
    gas_status = fields.Char("Gas Status")
