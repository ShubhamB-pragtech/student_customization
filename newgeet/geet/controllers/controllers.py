# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


# class Geet(http.Controller):
#     @http.route('/geet_index', website='True', auth='public')
#     def index(self, **kw):
#         # return "Hello, world"
#         student = request.env['geet.student'].sudo().search([])
#         return request.render("geet.geet_website_temp", { 'student': student})


class Geet(http.Controller):
    @http.route('/geet_index', website='True',type='http', auth='public')
    def index(self, **kw):
        # return "Hello, world"
        student = request.env['geet.student'].sudo().search([])
        return request.render("geet.one_index_tem")
class Geet2(http.Controller):
    @http.route('/boot_index', website='True',type='http', auth='public')
    def index(self, **kw):
        # return "Hello, world"
        student = request.env['geet.student'].sudo().search([])
        return request.render("geet.two_boot_tem")

#     @http.route('/geet/geet/objects/<model("geet.geet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('geet.object', {
#             'object': obj
#         })
