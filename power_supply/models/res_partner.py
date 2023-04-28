from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_dealer = fields.Boolean('Is dealer')
    is_marketeer = fields.Boolean('Is marketeer')
