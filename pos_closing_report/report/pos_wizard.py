# -*- coding: utf-8 -*-

import datetime
import pytz
import time
from openerp import tools
from openerp.osv import osv
from openerp.report import report_sxw

class pos_wizard(report_sxw.rml_parse):

    def _get_utc_time_range(self, form):
        user = self.pool['res.users'].browse(self.cr, self.uid, self.uid)
        tz_name = user.tz or self.localcontext.get('tz') or 'UTC'
        user_tz = pytz.timezone(tz_name)
        between_dates = {}

        for date_field, delta in {'date_ini': {'days': 0}, 'date_fi': {'days': 1}}.items():
            timestamp = datetime.datetime.strptime(form[date_field] + ' 00:00:00', tools.DEFAULT_SERVER_DATETIME_FORMAT) + datetime.timedelta(**delta)
            timestamp = user_tz.localize(timestamp).astimezone(pytz.utc)
            between_dates[date_field] = timestamp.strftime(tools.DEFAULT_SERVER_DATETIME_FORMAT)

        return between_dates['date_ini'], between_dates['date_fi']


    def _get_session(self, form):
        pos_obj = self.pool.get('pos.session')
        terminal_id = form['config_id']
        data = []
        result = {}
        date_ini, date_fi = self._get_utc_time_range(form)
        session_ids = pos_obj.search(self.cr, self.uid, [
            ('start_at', '>=', date_ini),
            ('start_at', '<', date_fi),
            ('config_id', '=', terminal_id[0]),
        ])
        for pos in pos_obj.browse(self.cr, self.uid, session_ids, context=self.localcontext):
            result = {
                    'id': pos.id,
                    'name': pos.name,
                    'date_ini': pos.start_at,
                    'date_fi': pos.stop_at,
                    'total_amount': pos.total_amount,
                    'state': pos.state,
                }
            data.append(result)
            
        if data:
            return data
        else:
            return {}
            
    def _get_payment(self, form, session):
        pos_pay = self.pool.get('account_bank_statement')
        data = []
        result = {}
        payment_ids = pos_pay.search(self.cr, self.uid, [
            ('pos_session_id', '=', session),
            ('balance_end_real', '!=', 0),
        ])
        
        return 'hola'

    def __init__(self, cr, uid, name, context):
        super(pos_wizard, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'get_session': self._get_session,
            'get_payment': self._get_payment,
        })

class Reportposreportclosing(osv.AbstractModel):
    _name = 'report.pos_closing_report.pos_closing_report'
    _inherit = 'report.abstract_report'
    _template = 'pos_closing_report.pos_closing_report'
    _wrapped_report_class = pos_wizard



