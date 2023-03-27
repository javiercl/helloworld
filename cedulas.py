# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import UserError

class cedulas(models.Model):
    _name = 'helloworld.cedulas'

    name = fields.Char(string='Folio', readonly=True)
    play_id = fields.Many2one('helloworld.plays',string='Juego', required="True")
    play_desc = fields.Char(compute='cal_desc_play',string='Desc. Juego', readonly=True)
    resultado = fields.Char(string='Resultado', required="True") # 1-1, 0-0, 3-2, etc
    fecha_inicio = fields.Datetime(string='Fecha de inicio', required="True")
    fecha_fin = fields.Datetime(string='Fecha de finalización', required="True")
    player_ids = fields.One2many('helloworld.cedula_det','cedula_id',string='Players', required="True")
    state = fields.Selection([('cre','Creado'),('env','Enviada'),('can','Cancelado')],string='Estado',readonly=True, default='cre', required="True")

    _order = 'play_id'

    def registrar(self):
        raise UserError('Cambiar status')

    @api.depends('play_id')
    def cal_desc_play(self):
        for rec in self:
            rec.play_desc = rec.play_id.team1_id.name + ' vs ' + rec.play_id.team2_id.name


class cedula_det(models.Model):
    _name = 'helloworld.cedula_det'
    cedula_id = fields.Many2one('helloworld.cedulas',string='Cedula')
    player_id = fields.Many2one('helloworld.players',string='Jugador')
    eventos_ids = fields.One2many('helloworld.eventos','player_id',string='Eventos')


class eventos(models.Model):
    _name = 'helloworld.eventos'
    player_id = fields.Many2one('helloworld.cedula_det',string='Jugador')
    tipo = fields.Selection([('gol','Gol'),('tarj','Tarjeta')],string='Tipo')
    minuto = fields.Char(string='Minuto del gol') # 45, 60, 89, 100
    targeta = fields.Selection([('amarilla','Amarilla'),('roja','Roja')],string='Targeta')
    
    _order = 'cedula_id,player_id'
