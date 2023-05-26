{
    'name': 'Power Supplies',
    'version': '16.0.1.0.0',
    'category': '',
    'description': u"""
Power Supply history
""",
    'author': 'Serincloud',
    'depends': [
        'base_partner_company_group',
        'mail',
    ],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/power_pricelist_views.xml',
        'views/power_tag_views.xml',
        'views/power_contract_type_views.xml',
        'views/power_contract_views.xml',
        'views/power_power_views.xml',
        'views/power_supply_views.xml',
        'views/power_saving_views.xml',
#        'views/res_partner_views.xml',
        'views/power_dealer_views.xml',
        'views/power_marketeer_views.xml',
        'views/power_sim_views.xml',
    ],
    'installable': True,
}
