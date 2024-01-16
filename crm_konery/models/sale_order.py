from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

#    23/10 JA.- Siempre va a ser el mismo comercial que el de la oportunidad en el presupuesto, aunque lo redacte
#    otra persona; en principio si hay que cambiar el comercial se hará desde la oportunidad:
    user_id = fields.Many2one('res.users', related='opportunity_id.user_id', tracking=True)
    team_id = fields.Many2one('crm.team', related='opportunity_id.team_id', tracking=True)
