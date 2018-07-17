#-*- coding: utf-8 -*-
from openerp import models, fields, api

class crmbioaire(models.Model):
	_inherit = 'crm.lead'
	metres_nau = fields.Char(string="M2 Warehouse", requiered=False, )
	press_tipus = fields.Char(string="Quotation Type", requiered=False, )
	provincia = fields.Char(string="State", requiered=False, )
	tipus_nau = fields.Char(string="Space Type", requiered=False, )
	tipus_sostre = fields.Char(string="Roof Type", requiered=False, )
	ventilacio = fields.Char(string="Ventilation", requiered=False, )
	alt_nau = fields.Char(string="Height", requiered=False, )

	
