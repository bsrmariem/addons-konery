from odoo import _, api, fields, models


class ProductTemplateAutomations(models.Model):
    _inherit = 'product.template'

    standard_price = fields.Float(track_visibility='onchange')

    @api.onchange('standard_price')
    def _on_change_standard_price(self):
        for record in self:

            product = self.env['product.template'].search([('name','=',record.name)])

            supervisor = self.env.user.company_id.user_id_purchase_price_supervisor
            if supervisor:
                summary = "Nuevo precio de coste para " + record.name + ": " + str(record.standard_price) + "€"
                modelo = self.env['ir.model'].search([('model', '=', 'product.template')])
                nueva = self.env['mail.activity'].create(
                    {'res_id': product.id, 'activity_type_id': 4, 'res_model_id': modelo.id, 'res_model': modelo.name,
                     'summary': summary, 'note': 'Registro creado automáticamente.', 'user_id': supervisor.id})





