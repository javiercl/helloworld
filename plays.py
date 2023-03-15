# -*- coding: utf-8 -*-
from odoo import models,fields, api
from datetime import datetime
from odoo.exceptions import UserError

class plays(models.Model):
    _name = 'helloworld.plays'

    #def cal_folio(self):
    #    self.name =  self.env['ir.sequence'].next_by_code('helloworld.plays.folio')

    #name = fields.Char(string='Folio', readonly=True, default='cal_folio')
    name = fields.Char(string='Folio', readonly=True)
    fecha = fields.Datetime(string='Fecha', required=True)
    liga_id = fields.Many2one('helloworld.ligas',string='Liga', required=True)
    team1_id = fields.Many2one('helloworld.teams',string='Equipo Local', required=True)
    team2_id = fields.Many2one('helloworld.teams',string='Equipo Visitante', required=True)
    estadio_id = fields.Many2one('helloworld.estadios',string='Estadio', required=True)
    arbitro_ids = fields.One2many('helloworld.plays_arbitros','play_id',string='Arbitros')
    state = fields.Selection([('cre','Creado'),('prog','Programado'),('rea','Realizo'),('can','Cancelado')],string='Estado',readonly=True, default='cre')
    
    _order = 'name'
    _sql_constraints = [('plays_uniq', 'unique(name)', 'Juego duplicado, intenta con otro...'),]

    @api.model
    def create(self,vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('helloworld.plays.folio')
        fecha_act = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        if vals['fecha'] < fecha_act:
            raise UserError('La fecha no debe ser menor a la actual')   

        if vals['team1_id'] == vals['team2_id']:
            raise UserError('El local y visitante deben ser diferentes')   

        return super(plays,self).create(vals)

    def write(self,vals):
        if vals.get('fecha'):
            fecha_act = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            if vals['fecha'] < fecha_act:
                raise UserError('La fecha no debe ser menor a la actual')   
            
        if vals.get('team1_id'):
            equ1 = vals['team1_id']
        else:
            equ1 = self.team1_id.id

        if vals.get('team2_id'):
            equ2 = vals['team2_id']
        else:
            equ2 = self.team2_id.id

        if equ1 == equ2:
            raise UserError('El local y visitante deben ser diferentes')   

        return super(plays,self).write(vals)


class plays_arbitros(models.Model):
    _name = 'helloworld.plays_arbitros'

    play_id = fields.Many2one('helloworld.plays',string='Play')
    arbitro_id = fields.Many2one('helloworld.arbitros',string='Arbitro')
    posicion = fields.Selection([('central','Central'),('bandera','Bandera'),('otro','Otro')],string='Posición')
    
    _order = 'play_id,arbitro_id'
    _sql_constraints = [('plays_uniq', 'unique(play_id,arbitro_id)', 'Arbitro duplicado, intenta con otro...'),]


