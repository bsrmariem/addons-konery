{
    'name': 'Power Supplies',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Power Supply history
""",
    'author': 'Serincloud',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/power_pricelist_views.xml',
    ],
    'installable': True,
}
