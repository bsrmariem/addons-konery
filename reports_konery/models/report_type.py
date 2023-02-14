from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class ReportType(models.Model):
    _name = 'report.type'
    _description = 'Report types'

    name = fields.Char(string='Nombre')
    type_pdf_watermark = fields.Binary(
        "Watermark", help="Upload an pdf file to use as an watermark on this report."
    )
    report_id = fields.Many2one('ir.actions.report', string='Informe')
    model = fields.Char(string='Modelo', related='report_id.model')
    template = fields.Many2one('ir.ui.view', string='Plantilla', required=True)
    paperformat_id = fields.Many2one('report.paperformat', 'Formato Papel')