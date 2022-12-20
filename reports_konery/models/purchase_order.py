from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    report_type = fields.Many2one('report.type', string='Report Type')
    #x_observaciones = fields.Text('Observaciones')

    def get_template_report(self):
        return self.report_type.template.xml_id