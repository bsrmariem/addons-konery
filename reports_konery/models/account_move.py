from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    move_report_type = fields.Selection(string="Report Type", selection=[('konery','Konery'),('solarteam','SolarTeam')])