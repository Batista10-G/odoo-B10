#-*- coding: utf-8 -*-
from openerp import models, fields, api

class partnerbioaire(models.Model):
	_inherit = 'res.partner'
	horarimatiini = fields.Float(string="Morning Hours", requiered=False,)
	horarimatifi = fields.Float(string="to", requiered=False,)
	horaritardaini = fields.Float(string="Afternoon Hours", requiered=False,)
	horaritardafi = fields.Float(string="to", requiered=False,)
	


