# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.onchange('user_ids')
    def _get_user_departments(self):
        for record in self:
            department = []
            for user in record.user_ids:
                if (user.employee_id.department_id.id) and (user.employee_id.department_id.id not in department):
                    department.append(user.employee_id.department_id.id)
            record['department_ids'] = [(6, 0, department)]
    department_ids = fields.Many2many('hr.department', string='Departments', compute='_get_user_departments')
