# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GameMatch(models.Model):
    _name = 'game.match'  # Table name in db
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'GameMatch table'

    image = fields.Binary(string="Image", attachment=True)

    server_location = fields.Char(string='Server location', required=True)

    team_A_score = fields.Integer(string='Team A score', required=True)
    team_A_throne = fields.Boolean(string='Team A throne status', required=True)

    team_B_score = fields.Integer(string='Team B score', required=True)
    team_B_throne = fields.Boolean(string='Team B throne status', required=True)

    duration = fields.Integer(string='match duration, min', required=True)

    winner_team = fields.Char(compute='_compute_winner', store=True)

    reg_match_date = fields.Datetime(string='Match datetime registration')

    @api.depends('team_A_throne', 'team_B_throne')
    def _compute_winner(self):
        for res in self:
            if res.team_A_throne:
                res.winner_team = 'team_A'
            elif res.team_B_throne:
                res.winner_team = 'team_B'
            elif res.team_B_throne and res.team_A_throne:
                res.winner_team = 'draw'
            else:
                res.winner_team = 'draw'
