from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('invoice_ids','invoice_ids.report_type.konery','sale_order_ids','sale_order_ids.report_type.konery')
    def get_konery_customer(self):
        konery_customer = False
        if (self.invoice_ids.report_type.konery) or (self.sale_order_ids.report_type.konery): 
            konery_customer = True
        self.konery_customer = konery_customer
    konery_customer = fields.Boolean('Konery customer', store=True, compute=get_konery_customer)

    @api.depends('invoice_ids','invoice_ids.report_type.solarteam','sale_order_ids','sale_order_ids.report_type.solarteam')
    def get_solarteam_customer(self):
        solarteam_customer = False
        if (self.invoice_ids.report_type.solarteam) or (self.sale_order_ids.report_type.solarteam): 
            solarteam_customer = True
        self.solarteam_customer = solarteam_customer
    solarteam_customer = fields.Boolean('Konery customer', store=True, compute=get_solarteam_customer)
