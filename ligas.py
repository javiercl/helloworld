# -*- coding: utf-8 -*-
from odoo import models,fields


class estados(models.Model):
    _name = 'helloworld.estados'
    name = fields.Char(string='Estado')
    _order = 'name'
    _sql_constraints = [('estados_uniq', 'unique(name)', 'Estado duplicado, intenta con otro...'),]

class poblaciones(models.Model):
    _name = 'helloworld.poblaciones'
    name = fields.Char(string='Población')
    _order = 'name'
    _sql_constraints = [('poblaciones_uniq', 'unique(name)', 'Población duplicada, intenta con otra...'),]


class ligas(models.Model):
    _name = 'helloworld.ligas'

    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Logo')
    poblacion_id = fields.Many2one('helloworld.poblaciones',string='Población')
    estado_id = fields.Many2one('helloworld.estados',string='Estado')
    teams = fields.Integer(compute='cal_num_teams',string='Equipos',readonly=True)
    team_ids = fields.One2many('helloworld.teams','liga_id',string='Equipos')
    
    _order = 'name'
    _sql_constraints = [('ligas_uniq', 'unique(name)', 'Liga duplicada, intenta con otra...'),]

    def cal_num_teams(self):
        for rec in self:
            num = 0
            for team in rec.team_ids:
                num += 1
            rec.teams = num
