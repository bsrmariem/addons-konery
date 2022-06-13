# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order',

    all_revision_ids = fields.Many2many('sale.order', string="Revisions", compute="get_all_revisions")
    all_mail_messages = fields.Many2many('mail.message', compute="get_all_messages", store=False)

    def get_all_messages(self):
        messages = self.env['mail.message'].search([('model', '=', 'sale.order'),
                                                    ('id', 'in', self.all_revision_ids.ids)])
        print("messages", messages)
        self.all_mail_messages = [(6, 0, messages.ids)]

    def get_all_revisions(self):
        revision = self.env['sale.order'].search([('unrevisioned_name', '=', self.unrevisioned_name)])
        self.all_revision_ids = [(6, 0, revision.ids)]

