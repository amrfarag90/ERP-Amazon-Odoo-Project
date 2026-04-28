{
    'name': 'Supplier Behavioral Drift Analyzer',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Detects behavioral drift and risk in suppliers (P2P)',
    'description': """
This module analyzes supplier behavior deviations in the Procure-to-Pay cycle
and classifies suppliers into risk levels based on purchasing patterns.
    """,
    'author': 'Your Team',
    'depends': [
        'purchase',
        'contacts'
    ],
    'data': [
        'views/res_partner_view.xml',
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': True,
}
