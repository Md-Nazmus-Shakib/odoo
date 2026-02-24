from odoo import fields,models,api,_
from odoo.exceptions import ValidationError,UserError
import re
from datetime import datetime
import smtplib
# from . import email_template

class User(models.Model):
    _name = 'user_info'
    _description = 'User Model'
    
    name = fields.Char(string='Username')
    email = fields.Char('Email')
    password = fields.Char('Password')
    
    @api.constrains('name')
    def _check_aame(self):
        for record in self:
            if not record.name:
                raise UserError("Name Field can not be empty..") 
            
                
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if not record.email:
                raise UserError("Email Field can not be empty..") 
            if record.email and not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                raise UserError("Invalid email format")  
                
    
    def save_action(self):
        for record in self:
            print("ok") 
            log_time=datetime.now()
            # self.env.cr.execute(
            #          "INSERT INTO log_log(log_description,log_time) VALUES(%s,%s)",
            #         ("A new user created.",log_time)
            #                 )
            values = {
                
                'log_description': "A new user created.",
                'log_time': datetime.now(),
                }
            self.env['log_log'].create(values)
        return True
    # def temp_action(self):
    #     self.ensure_one()
    # # Replace with your template's external ID
    #     template = self.env.ref('user_management.email_template_shakib')
    
    # # This triggers the standard mail composer with the template loaded
    #     return template.send_mail(self.id)
    def unlinkk(self):
        log_time=datetime.now()
        # s = smtplib.SMTP('smtp.gmail.com', 587)
        # # start TLS for security
        # s.starttls()
        # # Authentication
        # s.login("khan35-998@diu.edu.bd", "xcfh upcm fzmu xatm")
        # # message to be sent
        # # message = "Your data is deleted..."
        # message = email_template.Message(self.name)
        # # sending the mail
        # s.sendmail("khan35-998@diu.edu.bd", self.email, message)
        # # terminating the session
        # s.quit()
        # self.env.cr.execute(
            
            
        #              "INSERT INTO log_log(log_description,log_time) VALUES(%s,%s)",
        #             ("A  user deleted.",log_time)
        #                     )
        
        template = self.env.ref('user_management.email_template_shakib')
        # print(self.id.email)
        # for rec in :
        #     print(rec.email)
        # template.send_mail(self.id.email, force_send=True) 
        print(template) 
        template.send_mail(self.id, force_send=True)
        print("delete")
        values = {
                
                'log_description': "A  user deleted.",
                'log_time': datetime.now(),
                }
        self.env['log_log'].create(values)
        # Call the super method to perform actual deletion
        return super(User, self).unlink()
    # def show_email_template_wizard(self):
    #     self.ensure_one()
    #     template_id = self.env.ref('user_management.email_template_shakib').id
    #     # return {
    #     #     'type': 'ir.actions.act_window',
    #     #     'view_mode': 'form',
    #     #     'res_model': 'mail.template',
    #     #     'target': 'new',
    #     #     'context': {
    #     #         'default_model': self._name,
    #     #         'default_res_ids': [self.id],
    #     #         'default_use_template': bool(template_id),
    #     #         'default_template_id': template_id,
    #     #         'default_composition_mode': 'comment', # or 'mass_mail'
    #     #         'mark_so_as_sent': False,
    #     #     },
            
    #     # }
    #     return {
    #     'type': 'ir.actions.act_window',
    #     'res_model': 'mail.template',
    #     'view_mode': 'form',
    #     'res_id': template_id,   # This opens existing template
    #     'target': 'current',
    # }
  
        
class Log(models.Model):
    _name = 'log_log'
    _description = 'Log model'
     
    log_description = fields.Text(string='Log description')
    log_time = fields.Datetime(string='Log time',default=00.00)
    
   
    