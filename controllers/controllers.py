# -*- coding: utf-8 -*-
# from odoo import http


# class GameMod(http.Controller):
#     @http.route('/game_mod/game_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/game_mod/game_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('game_mod.listing', {
#             'root': '/game_mod/game_mod',
#             'objects': http.request.env['game_mod.game_mod'].search([]),
#         })

#     @http.route('/game_mod/game_mod/objects/<model("game_mod.game_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('game_mod.object', {
#             'object': obj
#         })
