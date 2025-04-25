from odoo import models,fields
class MedicineMaster(models.Model):
    _name = 'medicine.master'
    _description = 'Medicine Master'

    name = fields.Char(string='Medicine Name', required=True)