from odoo import models, fields, api


class ccpae(models.Model):
    _inherit = 'product.template'
    ntv_access = fields.Boolean("Product CCPAE", requiered=False)
