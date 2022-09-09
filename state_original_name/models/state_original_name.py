from odoo import models, fields, api


class StateOriginalName(models.Model):
    _inherit = 'res.country.state'
    original_name = fields.Char("Original name", requiered=False)
