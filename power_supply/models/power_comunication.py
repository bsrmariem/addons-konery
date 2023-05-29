# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

COMTYPE     = [('gsm','GSM'),('gprs','GPRS'),('datadis','Datadis'),('other','Other')]
COMPROTOCOL = [('iec','IEC'),('dlms','DLMS Prime'),('internet','Internet'),('modbus','Modbus')]

class PowerCommunication(models.Model):
    _name = 'power.communication'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Communication'

    name = fields.Char(string='Device name', required=True, store=True)
    type = fields.Selection(selection=COMTYPE, string='Technology', store=True)
    photovoltaic = fields.Boolean('Photovoltaic', store=True)
    konery360 = fields.Boolean('Konery 360', store=True)

    supply_id = fields.Many2one('power.supply', string='Power supply', store=True, required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', store=True, related='supply_id.partner_id')
    cups = fields.Char('CUPS', store=True, related='supply_id.cups')

    # METER:
    meter_brand = fields.Char('Meter Brand', store=True)
    meter_link_addr = fields.Char('Link address', store=True)
    # ¿sobre ya que es supply_id?:
    meter_point = fields.Char('Point', store=True)
    meter_serial_speed = fields.Char('Serial speed', store=True)
    meter_optical_speed = fields.Char('Optical speed', store=True)
    meter_voltage_ratio = fields.Char('Voltage ratio', store=True)
    meter_intensity_ratio = fields.Char('Intensity ratio', store=True)
    meter_image = fields.Binary('Meter image', store=True)

    # COMM:
    sim_owner = fields.Selection([('konery','Konery'),('dealer','Dealer')], string='SIM Owner', store=True)
    sim_id = fields.Many2one('power.sim', string='SIM', store=True, copy=False)

    protocol_communication = fields.Selection(selection=COMPROTOCOL, string='Protocol', store=True, copy=False)
    protocol_port = fields.Many2one('power.port', string='Port', store=True, copy=True)

    description = fields.Html('Description', store=True)

    @api.depends('sim_id','sim_owner')
    def _get_sim_iccid(self):
        result = ''
        if self.sim_id.id and self.sim_owner=='konery':
            result = self.sim_id.name
        self.iccid = result
    iccid = fields.Char('ICCID', store=True, copy=False, compute=_get_sim_iccid)

    @api.depends('sim_id','sim_owner')
    def _get_sim_phone(self):
        result = ''
        if self.sim_id.id and self.sim_owner=='konery':
            result = self.sim_id.phone
        self.phone = result
    phone = fields.Char('Phone', store=True, copy=False, compute=_get_sim_phone)

    @api.depends('sim_id','sim_owner')
    def _get_sim_access_ip(self):
        result = ''
        if self.sim_id.id and self.sim_owner=='konery':
            result = self.sim_id.access_ip
        self.access_ip = result
    access_ip = fields.Char('IP Address', store=True, copy=False, compute=_get_sim_access_ip)

    @api.depends('sim_id','sim_owner')
    def _get_sim_access_port(self):
        result = 0
        if self.sim_id.id and self.sim_owner=='konery':
            result = self.sim_id.access_port
        self.access_port = result
    access_port = fields.Integer('IP port', store=True, copy=False, compute=_get_sim_access_port)

    @api.depends('sim_id','sim_owner')
    def _get_sim_control_port(self):
        result = ''
        if self.sim_id.id and self.sim_owner=='konery':
            result = self.sim_id.control_port
        self.control_port = result
    control_port = fields.Integer('Control port', store=True, copy=False, compute=_get_sim_control_port)

    @api.onchange('sim_id', 'sim_owner')
    def _update_konery_sim_data(self):
        if self.sim_owner != 'konery':
            self.sim_id = False
