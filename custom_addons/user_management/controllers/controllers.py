# from odoo import http


# class TestBinCust(http.Controller):
#     @http.route('/test_bin_cust/test_bin_cust', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_bin_cust/test_bin_cust/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_bin_cust.listing', {
#             'root': '/test_bin_cust/test_bin_cust',
#             'objects': http.request.env['test_bin_cust.test_bin_cust'].search([]),
#         })

#     @http.route('/test_bin_cust/test_bin_cust/objects/<model("test_bin_cust.test_bin_cust"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_bin_cust.object', {
#             'object': obj
#         })

