# -*- coding: utf-8 -*-
# from odoo import http


# class Modulo-git(http.Controller):
#     @http.route('/modulo-git/modulo-git', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo-git/modulo-git/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo-git.listing', {
#             'root': '/modulo-git/modulo-git',
#             'objects': http.request.env['modulo-git.modulo-git'].search([]),
#         })

#     @http.route('/modulo-git/modulo-git/objects/<model("modulo-git.modulo-git"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo-git.object', {
#             'object': obj
#         })

