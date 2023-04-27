from odoo import _, api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    supply_id = fields.Many2one('power.supply', string='Supply point', store=True)
