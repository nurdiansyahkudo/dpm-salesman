{
    'name': 'Salesman from Employee',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Add Salesman from HR Employee',
    'author': '',
    'depends': ['sale', 'account', 'hr', 'sale_management'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move_view.xml',
        'views/hr_employee_view.xml',
        'views/sale_report_view.xml',
        'views/stock_picking_view.xml',
        # 'views/res_partner_view.xml',
        'views/account_invoice_report.xml',
    ],
    'installable': True,
    'application': False,
}