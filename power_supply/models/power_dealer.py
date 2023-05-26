# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerDealer(models.Model):
    _name = 'power.dealer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Dealers'

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean('Active', default=True)
    order_number = fields.Char("Order number")
    phone = fields.Char("Phone")
    cif = fields.Char("CIF")
    web = fields.Char("Web")