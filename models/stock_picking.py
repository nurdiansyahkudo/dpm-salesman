from odoo import fields, models, api

class Picking(models.Model):
    _inherit = 'stock.picking'

    employee_id = fields.Many2one(
        'hr.employee',
        string='Salesman',
        compute='_compute_employee_id',
        store=True
    )

    @api.depends('sale_id')
    def _compute_employee_id(self):
        for picking in self:
            if picking.sale_id:
                picking.employee_id = picking.sale_id.employee_id
            else:
                picking.employee_id = False