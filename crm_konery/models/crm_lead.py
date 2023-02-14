from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    power_kw = fields.Float(string='Power (kw)', store=True)
    crm_user_id = fields.Many2one('CRM Salesman', related='opportunity_id.user_id')
    crm_team_id = fields.Many2one('CRM Team', related='opportunity_id.team_id')