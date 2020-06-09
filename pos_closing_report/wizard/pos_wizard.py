# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class pos_wizard(models.TransientModel):
    _name = 'pos.closing.wizard'
    _description = 'Wizard POS Closing Report'
    start_date = fields.Date(required=True, default=fields.Date.today)
    end_date = fields.Date(required=True, default=fields.Date.today)
    pos_session_ids = fields.Many2one('pos.config', string='Point of Sale Name', required=True)

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    @api.multi
    def generate_report(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date, 'session_id': self.pos_session_ids.ids}
        return self.env.ref('pos_closing_report.pos_closing_report').report_action([],data=data)



