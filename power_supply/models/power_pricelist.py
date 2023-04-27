# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerPricelist(models.Model):
    _name = 'power.pricelist'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Supplies'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', store=True)
    