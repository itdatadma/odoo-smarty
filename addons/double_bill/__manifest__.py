{
    'name': 'Custom Double Bill',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Print two bills for the same transaction',
    'description': 'This module prints two bills for the same transaction, one for the customer and one for the owner with a specific footer.',
    'author': 'Your Name',
    'depends': ['sale', 'account'],
    'data': [
        'reports/sale_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'GPL-3',
}