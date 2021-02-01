from odoo import _, api, fields, models


class ResCompanyPriceSupervisor(models.Model):
    _inherit = 'res.company'

    user_id_purchase_price_supervisor = fields.Many2one('res.users', string='Supervisor coste productos',
                                                        help='Crea una actividad al usuario'
                                                             'cuando el precio de compra cambia')




