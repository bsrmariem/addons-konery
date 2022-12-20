# Copyright 2022 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Reports Konery & ST ",
    "summary": "Reports form sale order and invoice.",
    "version": "16.0.1.0.0",
    "category": "Reports",
    "author": "Pedro Guirao, ",
    "website": "",
    "license": "AGPL-3",
    "depends": ["account", "purchase", "sale", "report_qweb_pdf_watermark"],
    "data": [

        "views/kn_report_invoice.xml",
        "views/st_report_invoice.xml",
        "views/kn_report_so.xml",
        "views/st_report_so.xml",
        "views/kn_report_po.xml",
        "views/templates.xml",
        "views/ir_action_report.xml",
        "views/form_views.xml",
        "data/paper_format.xml",
        "security/ir.model.access.csv",
    ],

}
