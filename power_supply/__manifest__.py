# © 2023 Serincloud ( https://www.ingenieriacloud.com )
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Power Supplies',
    'version': '16.0.1.0.3',
    'category': '',
    'description': u"""
Power Supply history
""",
    'author': 'Serincloud',
    'depends': [
        'calendar',
        'web_map',
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
        'views/power_dealer_views.xml',
        'views/power_marketeer_views.xml',
        'views/power_sim_views.xml',
        'views/power_communication_views.xml',
        'views/power_coverage_views.xml',
        'views/power_port_views.xml',
    ],
    'application': True,
    'installable': True,
}
