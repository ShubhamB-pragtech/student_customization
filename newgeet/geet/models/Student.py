from odoo import models, fields,api
class Student(models.Model):
    _name = 'geet.student'
    _description = 'Student'
    name = fields.Char(string="Name")
    age = fields.Integer(string="age")
