# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

COMTYPE     = [('gsm','GSM'),('gprs','GPRS'),('datadis','Datadis'),('other','Other')]
COMPROTOCOL = [('iec','IEC'),('dlms','DLMS Prime'),('internet','Internet'),('modbus','Modbus')]
COMPORT     = [('rs232','RS232'),('rs485','RS485'),('ethernet','Ethernet'),('optical','Optical')]

class PowerCommunication(models.Model):
    _name = 'power.communication'
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
    meter_intensity_ratio = fields.Char('Intensity address', store=True)
    meter_image = fields.Binary('Meter image', store=True)

    # COMM:
    sim_owner = fields.Selection([('konery','Konery'),('dealer','Dealer')], string='SIM Owner', store=True)
    sim_id = fields.Many2one('power.sim', string='SIM', store=True)

    iccid = fields.Char('ICCID', store=True)
    phone = fields.Char('Phone', store=True)
    access_ip = fields.Char('IP Address', store=True)
    access_port = fields.Integer('IP port', store=True)
    control_port = fields.Integer('Control port', store=True)

    protocol_communication = fields.Selection(selection=COMPROTOCOL, store=True)
    protocol_port = fields.Selection(selection=COMPORT, store=True)

    description = fields.Html('Description', store=True)

    @api.onchange('sim_id')
    def _update_konery_sim_data(self):
        self.write({'iccid':sim_id.name, 'phone':sim_id.phone, 'access_ip':sim_id.access_ip,
                    'access_port':sim_id.access_port, 'control_port':sim_id.control_port
                    })