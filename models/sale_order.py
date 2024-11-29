from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one(
        'hr.employee',
        string="Salesman"
    )