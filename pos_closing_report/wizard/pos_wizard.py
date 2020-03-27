# -*- coding: utf-8 -*-

from openerp import api, fields, models

class posreportclosing(models.TransientModel):
    _name = 'pos.closing.wizard.model'
    _description = 'Wizard POS Closing Report'
    config_id = fields.Many2one('pos.config', string='Terminal', required=True)
    date_ini =  fields.Date(string='Date Start', requiered=True, default=fields.Date.today)
    date_fi =  fields.Date(string='Date End', requiered=True, default=fields.Date.today)

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['config_id','date_ini','date_fi'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['config_id','date_ini','date_fi','session_id'])[0])
        return self.env['report'].get_action(self, 'pos_closing_report.pos_closing_report', data=data)

