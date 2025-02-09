from odoo import models, fields, api

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    total_so_count = fields.Integer(
        string="Total SO", compute="_compute_total_so_count", store=False)
    total_invoice_count = fields.Integer(
        string="Total Invoice", compute="_compute_total_invoice_count", store=False)
    initial = fields.Char(string="Initial", compute="_compute_initial", store=True)

    def _compute_total_so_count(self):
        for employee in self:
            # Hitung jumlah SO terkait salesman (relasi tidak langsung)
            employee.total_so_count = self.env['sale.order'].search_count(
                [('employee_id', '=', employee.id)]
            )

    def _compute_total_invoice_count(self):
        for employee in self:
            # Hitung total nilai invoice dengan status Paid terkait salesman
            employee.total_invoice_count = self.env['account.move'].search_count([
                ('employee_id', '=', employee.id),
                ('move_type', 'in', ['out_invoice', 'out_refund'])
            ])

    def _compute_initial(self): 
        for employee in self: # Ambil inisial dari nama employee
            employee.initial = ''.join([name[0].upper() for name in employee.name.split()])