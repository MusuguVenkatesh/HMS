from odoo import models, fields



class ResUsers(models.Model):
    _inherit = 'res.users'

    specialization = fields.Char(string="Specialization")


