# © 2023 Serincloud ( https://www.ingenieriacloud.com )
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'CRM Konery Custom',
    'version': '16.0.1.0.2',
    'category': '',
    'description': u"""
CRM Konery Customs
""",
    'author': 'Serincloud',
    'depends': [
        'crm',
        'sale_management',
    ],
    'data': [
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
}
