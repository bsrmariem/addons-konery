# © 2023 Serincloud ( https://www.ingenieriacloud.com )
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Custom Konery',
    'version': '16.0.1.0.1',
    'category': '',
    "license": "AGPL-3",
    'website': "https://ingenieriacloud.com",
    'summary': 'Konery Customs, project group Admin and permissions',
    'author': 'Serincloud',
    'depends': [
        'purchase',
        'project',
        'helpdesk',
    ],
    'data': [
        'data/scheduled_actions.xml',
        'security/user_groups.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
