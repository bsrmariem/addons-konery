{
    'name': "Sale Order Revision IC",
    'summary': """
        Create sale order revision with secuential code.
        Internal tab with other revisions and chatter messages.
        """,
    'author': "Serincloud SL",
    'license': 'AGPL-3',
    'website': "https://ingenieriacloud.com",
    'category': 'Tools',
    'version': '16.0.1.0.0',
    'depends': [
        'sale_management',
    ],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
}
