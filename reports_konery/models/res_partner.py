from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('invoice_ids','invoice_ids.report_type.konery','sale_order_ids','sale_order_ids.report_type.konery')
    def get_konery_customer(self):
        for record in self:
            konery_customer = False
            konery_invoices = self.env['account.move'].search([('partner_id','=',record.id)])
#                                                               ('move_type','in',['out_invoice'])])
#                                                               ('report_type.konery','=',True)])
            konery_sales = self.env['sale.order'].search([('partner_id','=',record.id),('report_type.konery','=',True)])
            if (konery_invoices.ids != False) or (konery_sales.ids != False):
                konery_customer = True
            record['konery_customer'] = konery_customer
    konery_customer = fields.Boolean('Konery customer', store=True, compute=get_konery_customer)

    @api.depends('invoice_ids','invoice_ids.report_type.solarteam','sale_order_ids','sale_order_ids.report_type.solarteam')
    def get_solarteam_customer(self):
        for record in self:
            solarteam_customer = False
            solarteam_invoices = self.env['account.move'].search([('partner_id','=',record.id),
                                                                  ('move_type','in',['out_invoice']),
                                                                  ('report_type.solarteam','=',True)])
            solarteam_sales = self.env['sale.order'].search([('partner_id','=',record.id),
                                                             ('report_type.solarteam','=',True)])
            if (solarteam_invoices.ids) or (solarteam_sales.ids):
                solarteam_customer = True
            record['solarteam_customer'] = solarteam_customer
    solarteam_customer = fields.Boolean('Konery customer', store=True, compute=get_solarteam_customer)
