#-*- coding: utf-8 -*-
from openerp import models, fields, api

class cashdro(models.Model):
	_inherit = 'pos.config'
	cashdroip = fields.Char(string="CashDro IP", requiered=False)
	cashdrouser = fields.Char(string="CashDro User", requiered=False)
	cashdropass = fields.Char(string="CashDro Password", requiered=False)


	
