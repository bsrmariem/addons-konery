from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    report_type = fields.Many2one('report.type', string='Formato Impresión')

    def get_template_report(self):
        return self.report_type.template.xml_id