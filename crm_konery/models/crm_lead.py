from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    power_kw = fields.Float(string='Power (kw)', store=True)
    fv_origin = fields.Selection([('fv_konery','FV Konery'),('fv_other','FV others'),('none','None')],
                                 string='FV Origin', store=True)