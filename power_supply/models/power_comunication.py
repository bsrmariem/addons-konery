# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

COMTYPE     = [('gsm','GSM'),('gprs','GPRS'),('datadis','Datadis'),('other','Other')]
COMPROTOCOL = [('iec','IEC'),('dlms','DLMS Prime'),('internet','Internet'),('modbus','Modbus')]
COMPORT     = [('rs232','RS232'),('rs485','RS485'),('ethernet','Ethernet'),('optical','Optical')]

class PowerCommunication(models.Model):
    _name = 'power.communication'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Power Communication'

    name = fields.Char(string='Device name', required=True, store=True)
    type = fields.Selection(selection=COMTYPE, string='Technology', store=True)
    photovoltaic = fields.Boolean('Photovoltaic', store=True)

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

    @api.depends('sim_id','sim_owner')
    def _geticcid(self):
        iccid = ''
        if self.sim_id.id and self.sim_owner=='konery':
            iccid = self.sim_id.iccid
        self.iccid = iccid
    iccid = fields.Char('ICCID', store=True, copy=False, compute=_geticcid)
    phone = fields.Char('Phone', store=True, copy=False)
    access_ip = fields.Char('IP Address', store=True, copy=False)
    access_port = fields.Integer('IP port', store=True, copy=False)
    control_port = fields.Integer('Control port', store=True, copy=False)

    protocol_communication = fields.Selection(selection=COMPROTOCOL, store=True, copy=False)
    protocol_port = fields.Selection(selection=COMPORT, store=True, copy=False)

    description = fields.Html('Description', store=True)

#    @api.depends('sim_id', 'sim_owner')
#    def _update_konery_sim_data(self):
#        if self.sim_owner != 'konery':
#            self.sim_id = False
#        self.write({'iccid':self.sim_id.name, 'phone':self.sim_id.phone,
#                    'access_ip':self.sim_id.access_ip, 'access_port':self.sim_id.access_port,
#                    'control_port':self.sim_id.control_port
#                    })
