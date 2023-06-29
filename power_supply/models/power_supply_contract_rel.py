# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class SupplyContractRel(models.Model):
    _name = 'power.supply.contract.rel'
    _description = 'Power Supply Contract Rel'

    name = fields.Char('Rel supply contract')
    supply_id = fields.Many2one('power.supply', string='Supply', store=True)
    contract_id = fields.Many2one('power.contract', string='Contract', store=True)