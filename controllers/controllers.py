# -*- coding: utf-8 -*-
# from odoo import http


# class SalesmanEmployee(http.Controller):
#     @http.route('/salesman_employee/salesman_employee', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salesman_employee/salesman_employee/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('salesman_employee.listing', {
#             'root': '/salesman_employee/salesman_employee',
#             'objects': http.request.env['salesman_employee.salesman_employee'].search([]),
#         })

#     @http.route('/salesman_employee/salesman_employee/objects/<model("salesman_employee.salesman_employee"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salesman_employee.object', {
#             'object': obj
#         })

