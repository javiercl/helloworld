# -*- coding: utf-8 -*-
from odoo import models,fields

class coachs(models.Model):
    _name = 'helloworld.coachs'
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')

    _order = 'name'

class teams(models.Model):
    _name = 'helloworld.teams'

    liga_id = fields.Many2one('helloworld.ligas',string='Liga')
    name = fields.Char(string='Nombre')
    coach_id = fields.Many2one('helloworld.coachs',string='Coach')
    photo = fields.Binary(string='Foto')
    player_ids = fields.One2many('helloworld.players','team_id',string='Team')
    player2_ids = fields.Many2many('helloworld.players',string='Jugadores')
    playsp = fields.Integer(string='Juegos jugados')
    playsw = fields.Integer(string='Juegos ganados')
    playsl = fields.Integer(string='Juegos perdidos')
    playse = fields.Integer(string='Juegos empatados')
    _order = 'name'
