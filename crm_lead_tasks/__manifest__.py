# © 2023 Serincloud ( https://www.ingenieriacloud.com )
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'CRM lead tasks',
    'version': '16.0.1.0.0',
    'category': '',
    "license": "AGPL-3",
    'description': u"""
Tasks integration in CRM Leads
""",
    'author': 'Serincloud',
    'depends': [
        'crm',
        'project',
    ],
    'data': [
        'security/security_rules.xml',
        'views/crm_lead_views.xml',
        'views/project_task_views.xml',
        'views/res_company_views.xml',
    ],
    'installable': True,
}
