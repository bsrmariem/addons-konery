# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class PowerTag(models.Model):
    _name = 'power.tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Tags'

    name = fields.Char(string='Name', required=True)
    