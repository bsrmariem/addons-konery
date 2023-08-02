from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Pendiente de incluir en init de modelos cuando completen todos los vat que faltan:
    vat = fields.Char(required=True)
