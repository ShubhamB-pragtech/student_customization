# -*- coding: utf-8 -*-
# from odoo import http


# class Geet(http.Controller):
#     @http.route('/geet/geet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/geet/geet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('geet.listing', {
#             'root': '/geet/geet',
#             'objects': http.request.env['geet.geet'].search([]),
#         })

#     @http.route('/geet/geet/objects/<model("geet.geet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geet.object', {
#             'object': obj
#         })
