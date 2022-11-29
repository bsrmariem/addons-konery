# -*- coding: utf-8 -*-


{
    'name': 'CRM Auditor Readonly',
    'version': '16.0.0.1.0',
    'category': 'Sales/CRM',
    'sequence': 15,
    'summary': '',
    'website': '',
    'depends': [
        'crm'
    ],
    'data': [
        'security/crm_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
