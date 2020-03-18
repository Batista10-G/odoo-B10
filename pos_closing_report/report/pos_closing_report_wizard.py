# -*- coding: utf-8 -*-
from openerp import api, models
from openerp.exceptions import UserError


class ReportHelloworld(models.AbstractModel):
    _name = 'report.pos_closing_report.pos_closing_report'

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
        }
        
        return self.env['report'].render('pos_closing_report.pos_closing_report', docargs)

