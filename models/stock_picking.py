from odoo import fields, models, api

class Picking(models.Model):
    _inherit = 'stock.picking'

    # employee_id = fields.Many2many(
    #     'hr.employee',
    #     string='Salesman',
    #     compute='_compute_employee_id',
    #     store=True
    # )
    employee_id = fields.Many2one(
        'res.partner',
        string='Salesman',
        domain=[
            ('is_company', '=', False), 
            ('company_name', '=', 'PT Duta Pertiwi Mandiri')
        ],
        readonly=True
    )

    @api.depends('sale_id')
    def _compute_employee_id(self):
        for picking in self:
            if picking.sale_id:
                picking.employee_id = picking.sale_id.employee_id
            else:
                picking.employee_id = False