from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    task_ids = fields.One2many('project.task', 'lead_id', store=True)
    def get_tasks_count(self):
        self.task_count = len(self.tas_ids)
    task_count = fields.Integer('Tasks', compute=get_tasks_count, store=False)
