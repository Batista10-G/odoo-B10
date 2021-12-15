# -*- coding: utf-8 -*-
# Copyright 2019 - Marc Tormo i Bochaca - Batista10
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Hide Costs',
    'summary': 'Hide Costs from product and sales.',
    'author': 'Marc Tormo - Batista10',
    'website': "https://github.com/B10Serveis/Odoo-addons/hide_cost",
    'depends': ['account', 'product', 'sale', 'sale_margin'],
    'version': '14.0.0.1.0',
    'license': 'AGPL-3', 
    'application': True,
    'category': 'Sales',
    'data': [
	'views/cost.xml',
	'security/cost.xml',
    ],
    'installable': False,
}
