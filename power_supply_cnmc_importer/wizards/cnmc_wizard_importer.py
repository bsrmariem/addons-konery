# Copyright

import base64
import io
import csv
from odoo import fields, models, api
from odoo.exceptions import ValidationError

TYPE = [
    ('marketer', 'Marketer'),
    ('distributor', 'Distributor'),
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
        print("Import sim")
        l = 0
        k = 0

        #line = csv[i].split(',')
        #print(line)

        #for key in SIM_KEYS:
        #    if j < len(SIM_KEYS)-1:
        #        print("TEST", key, line[j])
        #        if key == line[j]:
        #            j += 1
        #        else:
        #            raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % SIM_KEYS)
        try:
            for line in csv:
                print("NEW LINE")
                split_line = line.split(',')
                if l == 0:
                    for key in SIM_KEYS:
                        if k < len(SIM_KEYS) - 1:
                            print("TEST", key, split_line[k])
                            if key == split_line[k]:
                                k += 1
                            else:
                                raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % SIM_KEYS)
                    l += 1
                    k = 0

                else:
                    sim_registered = self.env['res.sim'].search([
                        ("iccid", "=", split_line[k]),
                    ], limit=1)
                    if not sim_registered:
                        print("KEY", k)
                        self.env['res.sim'].sudo().create({
                            'name': str(split_line[k]),
                            'iccid': str(split_line[k]),
                            'access_ip': str(split_line[k+1]),
                            'access_port': str(split_line[k+2]),
                            'control_port': str(split_line[k+3]),
                            'application_port': str(split_line[k+4]),
                            'phone': str(split_line[k+5]),
                            'state': str(split_line[k+6]),
                            'coverage': str(split_line[k+7]),
                        })

        except Exception as e:
            raise ValidationError('Error %s' % e)

    def import_distributor(self, csv):
        print("Import distributor")
        l = 0
        k = 0

        # line = csv[i].split(',')
        # print(line)

        # for key in SIM_KEYS:
        #    if j < len(SIM_KEYS)-1:
        #        print("TEST", key, line[j])
        #        if key == line[j]:
        #            j += 1
        #        else:
        #            raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % SIM_KEYS)
        try:
            for line in csv:
                print("NEW LINE")
                split_line = line.split(',')
                if l == 0:
                    for key in DIS_KEYS:
                        if k < len(DIS_KEYS) - 1:
                            print("TEST", key, split_line[k])
                            if key == split_line[k]:
                                k += 1
                            else:
                                raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % DIS_KEYS)
                    l += 1
                    k = 0

                else:
                    dis_registered = self.env['res.distributor'].search([
                        ("cif", "=", split_line[k]),
                    ], limit=1)
                    if not dis_registered:
                        print("KEY", k)
                        self.env['res.distributor'].sudo().create({
                            'name': str(split_line[k+2]),
                            'order_number': str(split_line[k+1]),
                            'phone': str(split_line[k+3]),
                            'cif': str(split_line[k]),
                            'web': str(split_line[k + 4]),
                        })

        except Exception as e:
            raise ValidationError('Error %s' % e)

    def import_marketer(self, csv):
        print("Import marketer")
        l = 0
        k = 0

        # line = csv[i].split(',')
        # print(line)

        # for key in SIM_KEYS:
        #    if j < len(SIM_KEYS)-1:
        #        print("TEST", key, line[j])
        #        if key == line[j]:
        #            j += 1
        #        else:
        #            raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % SIM_KEYS)

        try:
            for line in csv:
                print("NEW LINE", line)
                split_line = line.split(',')
                print(split_line)
                for n in split_line:
                    print("KEY", n)
                if l == 0:
                    for key in MAR_KEYS:
                        if k < len(MAR_KEYS) - 1:
                            if key == split_line[k]:
                                k += 1
                            else:
                                raise ValidationError('Please upload a valid .csv file with ordered KEYS %s' % DIS_KEYS)
                    l += 1
                    k = 0

                else:
                    mark_registered = self.env['res.marketer'].search([
                        ("cif", "=", split_line[k+8]),
                    ], limit=1)
                    if not mark_registered:
                        self.env['res.marketer'].sudo().create({
                            'name': str(split_line[k + 1]),
                            'street': str(split_line[k + 2]),
                            'city': str(split_line[k + 4]),
                            'state': str(split_line[k + 5]),
                            'zip': str(split_line[k + 3]),
                            'order_number': str(split_line[k]),
                            'phone': str(split_line[k + 6]),
                            'sector': str(split_line[k + 7]),
                            'cif': str(split_line[k+8]),
                            'status': str(split_line[k + 12]),
                            #'date_discharge': str(split_line[k + 9]),
                            #'date_leaving': str(split_line[k + 10]),
                            'web': str(split_line[k + 11]),

                        })

        except Exception as e:
            raise ValidationError('Error %s' % e)

    def open_csv(self):
        print("OPEN CSV")

        if self.file_bin:
            strname = str(self.file_bin_name)
            strlen = len(strname)
            ext = strname[(strlen - 3)] + strname[(strlen - 2)] + strname[(strlen - 1)]
            print(self.file_bin_name)

            #print(csvfile)
            #csvfile.replace('\r', '\n')
            #csvfile.split(',')
            #print(csvfile)


            data = list(csv.reader(base64.b64decode(self.file_bin).decode('utf-8').splitlines()))

            for l in data:
                print(l[2])
            #if(ext == 'csv' or ext == 'CSV'):
            #    csvfile = base64.b64decode(self.file_bin).decode('utf-8').splitlines()
            #    if (self.file_type == 'sim'):
            #        self.import_sim(csvfile)
            #    elif (self.file_type == 'distributor'):
            #        self.import_distributor(csvfile)
            #    else:
            #        self.import_marketer(csvfile)
            #    print("")

            #else:
            #   raise ValidationError('Please upload a valid .csv file')
               #spamreader = csv.reader(csvfile)
               #print(spamreader)
               #for row in spamreader:
               #    print(row)
            #except TypeError as e:
            #    raise ValidationError('Please upload a valid .csv file')

        else:
            raise ValidationError('Please upload a valid .csv file')