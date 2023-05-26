{
    'name': 'Konery importer',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Power Supply CNMC contacts importer 
""",
    'author': 'Serincloud',
    'depends': [
        'power_supply',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/wizard_cnmc_importer.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
}
