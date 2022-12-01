{
    'name': 'CRM lead tasks',
    'version': '16.0.1.0.0',
    'category': '',
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
    #    'views/crm_lead_views.xml',
    #    'views/project_task_views.xml',
    #    'views/res_company_views.xml',
    ],
    'installable': True,
}
