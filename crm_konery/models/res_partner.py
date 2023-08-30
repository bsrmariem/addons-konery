from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Pendiente de incluir en init de modelos cuando completen todos los vat que faltan:
    vat = fields.Char(required=True)
    power_kw = fields.Float(string='Power (kw)', store=True)
    fv_origin = fields.Selection([('fv_konery','FV Konery'),('fv_other','FV others'),('none','None')],
                                 string='FV Origin', store=True)