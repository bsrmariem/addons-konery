from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    report_type = fields.Many2one('report.type', string='Report Type')
    #x_observaciones = fields.Text('Observaciones')

    def get_template_report(self):
        print("Template",self.report_type.template.name)
        return self.report_type.template.xml_id