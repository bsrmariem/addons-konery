from odoo import _, api, fields, models
from datetime import datetime, date

class FleetVehicleLogContract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'

    contract_km = fields.Integer('Contracted km', store=True, copy=True)
    additional_km_cost = fields.Float('Additional km', store=True, copy=True, digits='Product Price')
    returned_km_cost = fields.Float('Returned km', store=True, copy=True, digits='Product Price')

    def _get_pending_contract_km(self):
        for record in self:
            record['pending_km'] = record.contract_km - record.vehicle_id.odometer
    pending_km = fields.Integer('Pending km', store=False, compute='_get_pending_contract_km')

    def _get_annual_estimated_km(self):
        for record in self:
            dif = record.expiration_date - record.start_date
            record['annual_estimated_km'] = record.contract_km / ( dif.days / 365 )
    annual_estimated_km = fields.Integer('Annual estimated km', store=False, copy=True, compute='_get_annual_estimated_km')

    def _get_annual_consumed_km(self):
        for record in self:
            dif = date.today() - record.start_date
            record['annual_consumed_km'] = record.vehicle_id.odometer / ( dif.days / 365 )
    annual_consumed_km = fields.Integer('Annual consumed km', store=False, compute='_get_annual_consumed_km')
