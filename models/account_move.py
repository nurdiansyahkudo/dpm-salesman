from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    employee_ids = fields.Many2many('hr.employee', string="Salesmen")

    @api.model
    def create(self, vals):
        if 'invoice_origin' in vals:
            sale_order = self.env['sale.order'].search([('name', '=', vals['invoice_origin'])], limit=1)
            if sale_order:
                vals['employee_ids'] = [(6, 0, sale_order.employee_ids.ids)]
        return super(AccountMove, self).create(vals)
