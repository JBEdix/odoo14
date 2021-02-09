# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model): #Nombre de la clase, en la base de datos
    _name = 'openacademy.course' #nombre de tabla openacademy_course
    _description = "OpenAcademy Courses" #descripcion para odoo

    #campos de la tabla.
    name = fields.Char(string="Title", required=True) #char de tamaño pequeño 
    description = fields.Text() # text tama;o grande

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")