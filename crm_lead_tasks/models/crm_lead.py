from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    task_ids = fields.One2many('project.task', 'lead_id', store=True)
