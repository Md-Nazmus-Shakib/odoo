# from odoo import models, fields, api


# class log_viewer(models.Model):
#     _name = 'log_viewer.log_viewer'
#     _description = 'log_viewer.log_viewer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

