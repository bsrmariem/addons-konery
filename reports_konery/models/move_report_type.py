from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class ReportType(models.Model):
    _name = 'report.type'

    name = fields.Char(string='Name')
    type_pdf_watermark = fields.Binary(
        "Watermark", help="Upload an pdf file to use as an watermark on this report."
    )
    report_id = fields.Many2one('ir.actions.report', string='Report')
    model = fields.Char(string='Model', related='report_id.model')
    template = fields.Many2one('ir.ui.view', string='Template', required=True)