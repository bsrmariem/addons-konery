from odoo import _, api, fields, models


class ProductProductAutomations(models.Model):
    _inherit = 'product.product'

    standard_price = fields.Float(track_visibility='onchange')



