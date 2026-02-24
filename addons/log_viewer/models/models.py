from odoo import models, fields, api

class logmodel(models.Model):
    _inherit = 'log_log'
    
    def show_email_template_wizard(self):
        # self.ensure_one()
        template_id = self.env.ref('user_management.email_template_shakib').id
       
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'mail.template',
        'view_mode': 'form',
        'res_id': template_id,   # This opens existing template
        'target': 'current',
    }




