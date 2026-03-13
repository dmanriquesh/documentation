{
    'name': "Resumen de Lotes (Pre-Nómina)",
    'summary': "Resumen de Lotes de recibos de pago",
    'description': "Listao personalizado para revisar los lotes de recibos de pago generados en la pre-nómina.",
    'author': "Arkisoft / Deivis Manrique",
    'website': "www.arkisoft-soluciones-de-software.odoo.com",
    'category': 'Human Resources/Payroll',
    'version': '17.0.1.0',
    'depends': ['base', 'hr_payroll'],
    'data': [
        'reports/ir_actions_report.xml',
        'reports/resumen_de_lotes.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}