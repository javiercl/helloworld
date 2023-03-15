# -*- coding: utf-8 -*-
from odoo import models,fields


class players(models.Model):
    _name = 'helloworld.players'

    team_id = fields.Many2one('helloworld.teams',string='Team')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    numero = fields.Integer(string='Número de playera')
    posicion = fields.Selection([('del','Delantero'),('def','Defensa'),('por','Portero'),('car','Carrilero'),('cen','Central')],string='Número de playera')
    
    _order = 'team_id,name'
