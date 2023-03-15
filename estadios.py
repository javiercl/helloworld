# -*- coding: utf-8 -*-
from odoo import models,fields


""" class horarios(models.Model):
    _name = 'helloworld.horarios'

    estadio_id = fields.Many2one('helloworld.estadios',string='Estadio')
    lun = fields.Char(string='Lunes')
    mar = fields.Char(string='Martes')
    
    _order = 'liga_id,name' 
"""


class estadios(models.Model):
    _name = 'helloworld.estadios'

    liga_id = fields.Many2one('helloworld.ligas',string='Liga')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    
    _order = 'liga_id,name'
