# -*- coding: utf-8 -*-

from odoo import api,fields,models,_ 

class RahiApp(models.Model):
    _name='rahiapp'

    name=fields.Char(string="Name",required=True)
    date_of_birth=fields.Date(string='Date of birth',required=True,help='Your date of birth')
    active = fields.Boolean(string='Active',default=True)
    bio = fields.Text(string='About yourself')
    age = fields.Integer(string='Your Age')
    salary = fields.Float(string='Salary',digit=(6,2))
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])

class RahiApp2(models.Model):
    _inherit='rahiapp'

    _name='rahiapp2'

    email=fields.Char(string='Email')
