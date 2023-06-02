# Copyright

import base64
import io
import csv
import datetime
from odoo import fields, models, api
from odoo.exceptions import ValidationError

TYPE = [
    ('marketer', 'Marketer'),
    ('dealer', 'Dealer'),
    ('sim', 'SIM'),
]

SIM_KEYS = ['ICCID', 'TELEFONO', 'IP ACCESO', 'PUERTO ACCESO', 'PUERTO CONTROL', 'PUERTO 485', 'ESTADO', 'COBERTURA']
DIS_KEYS = ['NIF empresa', 'Nº de orden', 'Nombre empresa', 'Teléfono gratuito incidencias', 'Portal de medidas',]
MAR_KEYS = ['Nº de orden', 'Nombre empresa', 'Dirección empresa', 'C.P.', 'Municipio empresa', 'Provincia empresa',
            'Teléfono Att cliente gratuito', 'Ámbito actuación', 'NIF empresa', 'Fecha alta', 'Fecha baja',
            'Página web', 'Estado']

class ImporterCnmc(models.TransientModel):
    _name = 'cnmc.importer'
    _description = 'CNMC importer wizard'

    name = fields.Char('Name')
    file_type = fields.Selection(
        selection=TYPE,
        string="File type",
        default="marketer",
    )
    file_bin = fields.Binary("Document")
    file_bin_name = fields.Char('File name')

    def import_sim(self, csv):
        l = 0
        k = 0
        try:
            for line in csv:
                if l == 0:
                    for key in SIM_KEYS:
                        if k < len(SIM_KEYS) - 1:
                            if key == line[k]:
                                k += 1
                            else:
                                raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % SIM_KEYS)
                    l += 1
                    k = 0
                else:
                    sim_registered = self.env['power.sim'].search([
                        ("name", "=", line[k]),
                    ], limit=1)
                    if not sim_registered:
                        coverage_id = self.env['power.coverage'].search([
                            ("name", "=", line[k + 7]),
                        ], limit=1)
                        if coverage_id:
                            self.env['power.sim'].sudo().create({
                                'name': str(line[k]),
                                'access_ip': str(line[k+2]),
                                'access_port': str(line[k+3]),
                                'control_port': str(line[k+4]),
                                'rs485_port': str(line[k+5]),
                                'phone': str(line[k+1]),
                                'coverage_id': coverage_id.id,
                            })
                        else:
                            raise ValidationError('Verifica que existan la/las Operadoras (Cobertura) en el menú Configuración => Cobertura')
        except Exception as e:
            raise ValidationError('Error %s' % e)

    def import_dealer(self, csv):
        l = 0
        k = 0

        try:
            for line in csv:
                if l == 0:
                    for key in DIS_KEYS:
                        if k < len(DIS_KEYS) - 1:
                            if key == line[k]:
                                k += 1
                            else:
                                raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % DIS_KEYS)
                    l += 1
                    k = 0
                else:
                    dis_registered = self.env['power.dealer'].search([
                        ("cif", "=", line[k]),
                    ], limit=1)
                    if not dis_registered:
                        self.env['power.dealer'].sudo().create({
                            'name': str(line[k+2]),
                            'order_number': str(line[k+1]),
                            'phone': str(line[k+3]),
                            'cif': str(line[k]),
                            'web': str(line[k + 4]),
                        })

        except Exception as e:
            raise ValidationError('Error %s' % e)

    def import_marketer(self, csv):
        l = 0
        k = 0

        try:
            for line in csv:
                if l == 0:
                    for key in MAR_KEYS:
                        if k < len(MAR_KEYS) - 1:
                            if key == line[k]:
                                k += 1
                            else:
                                raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % DIS_KEYS)
                    l += 1
                    k = 0

                else:
                    mark_registered = self.env['power.marketeer'].search([
                        ("cif", "=", line[k+8]),
                    ], limit=1)
                    if not mark_registered:
                        date_discharge = False
                        date_leaving = False
                        if line[k + 9] != '':
                            temp_date = line[k + 9].replace('/','')
                            date_discharge = datetime.datetime.strptime(temp_date, '%d%m%Y').date()
                        if line[k + 10] != '':
                            temp_date = line[k + 10].replace('/', '')
                            date_leaving = datetime.datetime.strptime(temp_date, '%d%m%Y').date()

                        self.env['power.marketeer'].sudo().create({
                            'name': str(line[k + 1]),
                            'street': str(line[k + 2]),
                            'city': str(line[k + 4]),
                            'state': str(line[k + 5]),
                            'zip': str(line[k + 3]),
                            'order_number': str(line[k]),
                            'phone': str(line[k + 6]),
                            'sector': str(line[k + 7]),
                            'cif': str(line[k+8]),
                            'status': str(line[k + 12]),
                            'date_discharge': date_discharge,
                            'date_leaving': date_leaving,
                            'web': str(line[k + 11]),
                        })
        except Exception as e:
            raise ValidationError('Error %s' % e)

    def open_csv(self):
        if self.file_bin:
            strname = str(self.file_bin_name)
            strlen = len(strname)
            ext = strname[(strlen - 3)] + strname[(strlen - 2)] + strname[(strlen - 1)]

            if(ext == 'csv' or ext == 'CSV'):
                #csvfile = base64.b64decode(self.file_bin).decode('utf-8').splitlines()
                csvfile = list(csv.reader(base64.b64decode(self.file_bin).decode('utf-8').splitlines()))
                if (self.file_type == 'sim'):
                    self.import_sim(csvfile)
                elif (self.file_type == 'dealer'):
                    self.import_dealer(csvfile)
                else:
                    self.import_marketer(csvfile)

        else:
            raise ValidationError('Please upload a valid .csv file')