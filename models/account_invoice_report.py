from odoo import models, fields, api

class AccountInvoiceReport(models.Model):
  _inherit = "account.invoice.report"

  invoice_employee_id = fields.Many2one(
        'hr.employee',
        string='Salesman',
        readonly=True
    )