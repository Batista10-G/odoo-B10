{
    'name': 'Hide Costs',
    'summary': 'Hide Costs from product and sales.',
    'author': 'Marc Tormo - Batista10',
    'website': "https://www.batista10.cat",
    'depends': ['account', 'product', 'sale', 'sale_margin'],
    'version': '9.0.0.1.0',
    'license': 'AGPL-3', 
    'application': True,
    'category': 'Sales',
    'data': [
	'views/cost.xml',
	'security/cost.xml',
    ],
}
