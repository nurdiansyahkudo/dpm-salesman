from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2many(
        'hr.employee',
        string="Salesman"
    )