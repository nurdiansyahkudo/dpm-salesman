from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    initial = fields.Char(string="Initial", compute="_compute_initial", store=True)

    def _compute_initial(self): 
        for partner in self: # Ambil inisial dari nama partner
            partner.initial = ''.join([name[0].upper() for name in partner.name.split()])