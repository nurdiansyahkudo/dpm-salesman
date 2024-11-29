from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    employee_id = fields.Many2one(
        'hr.employee',
        string='Salesman'
    )

    @api.model
    def create(self, vals):
        if 'invoice_origin' in vals:
            sale_order = self.env['sale.order'].search([('name', '=', vals['invoice_origin'])], limit=1)
            if sale_order:
                vals['employee_id'] = sale_order.employee_id.id
        return super(AccountMove, self).create(vals)