# Copyright 2022 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Reports Konery & ST ",
    "summary": "Reports form sale order and invoice.",
    "version": "16.0.1.0.0",
    "category": "Reports",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ["web", "account", "account_payment_mode"],
    "data": [
        "data/paper_format.xml",
        "views/report_invoice.xml",
        "views/templates.xml",
        "views/account_move.xml",
    ],

}
