
from odoo import models, fields

class LabTest(models.Model):
    _name = 'lab.test'
    _description = 'Lab Test'

    test_type = test_type = fields.Selection([
    ('blood', 'Blood Test'),
    ('sugar', 'Sugar Test'),
    ('xray', 'X-Ray'),
    ('scan', 'Scanning')
], string='Test Type', required=True)

    result = fields.Text(string='Result')

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    # These fields are automatically fetched from the selected patient
    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_age = fields.Char(string='Patient Age', related='patient_id.age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', readonly=True)




