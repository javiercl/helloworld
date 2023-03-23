# -*- coding: utf-8 -*-
from odoo import models,fields


class cedulas(models.Model):
    _name = 'helloworld.cedulas'

    play_id = fields.Many2one('helloworld.plays',string='Juego')
    resultado = fields.Char(string='Resultado') # 1-1, 0-0, 3-2, etc
    fecha_inicio = fields.Datetime(string='Fecha de inicio')
    fecha_fin = fields.Datetime(string='Fecha de finalización')
    player_ids = fields.Many2one('helloworld.cedula_det',string='Players')
    eventos_ids = fields.Many2one('helloworld.eventos',string='Eventos')

    _order = 'play_id'


class cedula_det(models.Model):
    _name = 'helloworld.cedula_det'
    cedula_id = fields.Many2one('helloworld.cedulas',string='Cedula')
    player_id = fields.Many2one('helloworld.players',string='Jugador')



class eventos(models.Model):
    _name = 'helloworld.eventos'
    player_id = fields.Many2one('helloworld.cedula_det',string='Jugador')
    tipo = fields.Selection([('gol','Gol'),('tarj','Tarjeta')],string='Tipo')
    minuto = fields.Char(string='Minuto del gol') # 45, 60, 89, 100
    targeta = fields.Selection([('amarilla','Amarilla'),('roja','Roja')],string='Targeta')
    
    _order = 'cedula_id,player_id'
