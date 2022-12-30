
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from base64 import b64decode
from io import BytesIO
from logging import getLogger

from PIL import Image

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval

import os

logger = getLogger(__name__)

try:
    # we need this to be sure PIL has loaded PDF support
    from PIL import PdfImagePlugin  # noqa: F401
except ImportError:
    logger.error("ImportError: The PdfImagePlugin could not be imported")

try:
    from PyPDF2 import PdfFileReader, PdfFileWriter  # pylint: disable=W0404
    from PyPDF2.utils import PdfReadError  # pylint: disable=W0404
except ImportError:
    logger.debug("Can not import PyPDF2")


class ReportWaterMark(models.Model):
    _inherit = "ir.actions.report"

    report_type_ids = fields.One2many('report.type','report_id',string='Types')

    @api.model
    def _run_wkhtmltopdf(
        self,
        bodies,
        report_ref=False,
        header=None,
        footer=None,
        landscape=False,
        specific_paperformat_args=None,
        set_viewport_size=False,
    ):
        docids = self.env.context.get("res_ids", False)
        report_sudo = self._get_report(report_ref)
        records = self.env[report_sudo.model].browse(docids)
        if report_sudo.model in ['sale.order',['account.move']]:
            for record in records:
                #BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
                #print(("%s/static/img/watermark_kn.pdf" % BASE_DIR))
                #with open(("%s/static/img/watermark_kn.pdf" % BASE_DIR), mode='rb') as file:
                #    fileContent = file.read()
                report_sudo.pdf_watermark = record.report_type.type_pdf_watermark
                if record.report_type.paperformat_id:
                    report_sudo.paperformat_id = record.report_type.paperformat_id

        return super(ReportWaterMark, self)._run_wkhtmltopdf(
            bodies,
            report_ref=report_ref,
            header=header,
            footer=footer,
            landscape=landscape,
            specific_paperformat_args=specific_paperformat_args,
            set_viewport_size=set_viewport_size,
        )




