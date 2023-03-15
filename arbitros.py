# -*- coding: utf-8 -*-
from odoo import models,fields


class arbitros(models.Model):
    _name = 'helloworld.arbitros'

    liga_id = fields.Many2one('helloworld.ligas',string='Liga')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    
    _order = 'liga_id,name'
