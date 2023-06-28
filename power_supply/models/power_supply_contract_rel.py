# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class SupplyContractRel(models.Model):
    _name = 'power.supcon.rel'
    _description = 'Power SupplyContract Rel'

    name = fields.Char('Name')
    supply_id = fields.Many2one('power.supply', string='Supply', store=True)
    contract_id = fields.Many2one('power.contract', string='Contract', store=True)
#    supply_id = fields.Integer(string='Supply', store=True)
#    contract_id = fields.Integer(string='Contract', store=True)
