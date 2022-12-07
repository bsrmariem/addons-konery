from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    report_type = fields.Many2one('report.type', string='Report Type')

    def get_template_report(self):
        print(self.report_type.template.name)
        print(self.report_type.template.xml_id)

        return self.report_type.template.xml_id