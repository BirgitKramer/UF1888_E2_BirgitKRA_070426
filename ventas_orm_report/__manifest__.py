{
    'name': 'Ventas ORM Report',
    'version': '19.0.1.0.0',
    'summary': 'Consultas ORM de ventas, clientes y productos mas vendidos',
    'description': '''
    Modulo para Odoo 19 que muestra como explotar informacion comercial usando unicamente el ORM de Odoo.
    ''',
    'category': 'Sales/Reporting',
    'author': 'Birgit Kra',
    'license': 'LGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_report_orm_views.xml',
        'report/sale_report_orm_templates.xml',
        'report/sales_report_orm:report.xml',
    ],
    'installable': True,
    'application': True,
    
}