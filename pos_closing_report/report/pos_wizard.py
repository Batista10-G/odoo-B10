# -*- coding: utf-8 -*-

import datetime
import pytz
import time
from odoo import api, fields, models


class Reportposreportclosing(models.AbstractModel):
    _name = 'report.pos_closing_report.pos_closing_report'

    @api.model
    def get_session(self, date_ini=False, date_fi=False, config_id=False):
        if not config_id:
            config_id = self.env['pos.session'].search([])
        
        user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
        today = user_tz.localize(fields.Datetime.from_string(fields.Date.context_today(self)))
        today = today.astimezone(pytz.timezone('UTC'))
        if date_ini:
            date_ini = fields.Datetime.from_string(date_ini)
        else:
            # start by default today 00:00:00
            date_ini = today

        if date_fi:
            # set time to 23:59:59
            date_fi = fields.Datetime.from_string(date_fi)
        else:
            # stop by default today 23:59:59
            date_fi = today + timedelta(days=1, seconds=-1)

        # avoid a date_stop smaller than date_start
        date_fi = max(date_fi, date_ini)

        date_ini = fields.Datetime.to_string(date_ini)
        date_fi = fields.Datetime.to_string(date_fi)
                
        session_ids = self.env['pos.session'].search([
            ('start_at', '>=', date_ini),
            ('start_at', '<=', date_fi),
            ('config_id', '=', config_id)])
            
        name_pos =self.env["pos.config"].search([('id', '=', config_id)]).name
        
        return {
            'ident': config_id,
            'name': name_pos,
            'date_ini': date_ini,
            'date_fi': date_fi,
#            'total_amount': pos.total_amount,
#            'state': pos.state,
            } 
        
    @api.multi
    def render_html(self, docids, data=None):
        data = dict(data or {})
        config_id = self.env['pos.config'].browse(data['session_id'])
        data.update(self.get_session(data['date_start'], data['date_stop'], data['session_id']))
        return self.env['report'].render('pos_closing_report.pos_closing_report', data)

