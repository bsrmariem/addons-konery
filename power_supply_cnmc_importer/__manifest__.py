{
    'name': 'Power Suppliers cnmc importer',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Power Supply CNMC contacts
""",
    'author': 'Serincloud',
    'depends': [
        'power_supply',
    ],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'wizards/wizard_cnmc_importer.xml',
        'views/menu_views.xml',
        'views/power_contact_cnmc_views.xml',

    ],
    'installable': True,
}
