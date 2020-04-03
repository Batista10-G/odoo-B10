# -*- coding: utf-8 -*-

import time
from openerp.osv import osv, fields

class pos_wizard(osv.osv_memory):
    _name = 'pos.closing.model'
    _description = 'Wizard POS Closing Report'
    _columns = {
        'config_id': fields.many2one('pos.config', string='Terminal', required=True),
        'date_ini': fields.date('Date Start', requiered=True),
        'date_fi': fields.date('Date End', requiered=True),
    }
    _defaults = {
        'date_ini': fields.date.context_today,
        'date_fi': fields.date.context_today,
    }

    def print_report(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        datas = {'ids': context.get('active_ids', [])}
        res = self.read(cr, uid, ids, ['date_ini', 'date_fi', 'config_id'], context=context)
        res = res and res[0] or {}
        datas['form'] = res
        if res.get('id',False):
            datas['ids']=[res['id']]
        return self.pool['report'].get_action(cr, uid, [], 'pos_closing_report.pos_closing_report', data=datas, context=context)


