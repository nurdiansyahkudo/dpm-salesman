from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2many(
        'hr.employee',
        string="Salesman"
    )
    # employee_id = fields.Many2one(
    #     'res.partner',
    #     string='Salesman',
    #     domain=[
    #         ('is_company', '=', False), 
    #         ('company_name', '=', 'Duta Pertiwi Mandiri')
    #     ],
    #     readonly=True
    # )