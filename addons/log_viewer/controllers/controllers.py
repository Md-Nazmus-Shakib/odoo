# from odoo import http


# class LogViewer(http.Controller):
#     @http.route('/log_viewer/log_viewer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/log_viewer/log_viewer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('log_viewer.listing', {
#             'root': '/log_viewer/log_viewer',
#             'objects': http.request.env['log_viewer.log_viewer'].search([]),
#         })

#     @http.route('/log_viewer/log_viewer/objects/<model("log_viewer.log_viewer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('log_viewer.object', {
#             'object': obj
#         })

