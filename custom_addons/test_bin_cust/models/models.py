# from odoo import models, fields, api


# class test_bin_cust(models.Model):
#     _name = 'test_bin_cust.test_bin_cust'
#     _description = 'test_bin_cust.test_bin_cust'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

