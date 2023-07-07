# © 2023 Serincloud ( https://www.ingenieriacloud.com )
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'CRM Auditor Readonly',
    'version': '16.0.0.1.0',
    'category': 'Sales/CRM',
    "license": "AGPL-3",
    'sequence': 15,
    'summary': '',
    'website': '',
    'author': 'Serincloud',
    'depends': [
        'crm',
        'sales_team',
        'sale_management',
        'sale_crm',
    ],
    'data': [
        'security/crm_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
