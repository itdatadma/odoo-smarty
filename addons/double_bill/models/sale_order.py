from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_print_double_bill(self):
        self.ensure_one()
        return self.env.ref('custom_double_bill.action_report_saleorder').report_action(self)