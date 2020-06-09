# -*- coding: utf-8 -*-

import datetime
import pytz
import time
from odoo import api, fields, models


class Reportposreportclosing(models.AbstractModel):
    _name = 'report.pos_closing_report.report_pos_closing_report'

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
            date_ini = today

        if date_fi:
            date_fi = fields.Datetime.from_string(date_fi)
        else:
            date_fi = today + timedelta(days=1, seconds=-1)

        date_fi = max(date_fi, date_ini)

        date_ini = fields.Datetime.to_string(date_ini)
        date_fi = fields.Datetime.to_string(date_fi)
                
        session_ids = self.env['pos.session'].search([
            ('start_at', '>=', date_ini),
            ('start_at', '<=', date_fi),
            ('config_id', '=', config_id)])
            
        name_pos = self.env["pos.config"].search([('id', '=', config_id)]).name
        
        session_bank = self.env['account.bank.statement'].search([
            ('create_date', '>=', date_ini),
            ('create_date', '<=', date_fi),
            ('pos_session_id.config_id', '=', config_id)])
            
        amount = {}
        linies = {}
        for payment in session_bank:
            amount.setdefault(payment.pos_session_id.name, 0.0)
            amount[payment.pos_session_id.name] += payment.total_entry_encoding
            
        return {
            'ident': config_id,
            'name': name_pos,
            'date_ini': date_ini,
            'date_fi': date_fi,
            'sessions': [{
                'session_id': session.id,
                'session_name': session.name,
                'session_stat': dict(self.env['pos.session']._fields['state']._description_selection(self.env))[session.state],
                'session_ini': session.start_at,
                'session_fi': session.stop_at,
                'session_amount': amount[session.name],
                } for session in session_ids],
            'linies': [{
                'fpago': payment.journal_id.name,
                'declarat': payment.balance_end,
                'canvi': payment.balance_start,
                'total': payment.total_entry_encoding,
                'session_nom': payment.pos_session_id.name
                } for payment in session_bank]
            } 
        
    @api.multi
    def get_report_values(self, docids, data=None):
        data = dict(data or {})
        config_id = self.env['pos.config'].browse(data['session_id'])
        data.update(self.get_session(data['date_start'], data['date_stop'], data['session_id']))
        return data

