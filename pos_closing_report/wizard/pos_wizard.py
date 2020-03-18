# -*- coding: utf-8 -*-

from openerp import api, fields, models

class posreportclosing(models.TransientModel):
    _name = 'pos.closing.model'
    _description = 'Wizard POS Closing Report'
       
    config_id = fields.Many2one('pos.config', string='Terminal', required=True)



    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['config_id'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['config_id'])[0])
        return self.env['report'].get_action(self, 'pos_closing_report.pos_closing_report', data=data)

