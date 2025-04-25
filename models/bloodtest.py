from odoo import models, fields

class BloodTest(models.Model):
    _name = 'blood.test'
    _description = 'Blood Test'

    test_type = fields.Selection([
        ('sugar', 'Blood Sugar'),
        ('hemoglobin', 'Hemoglobin'),
        ('cbc', 'Complete Blood Count (CBC)'),
        ('thyroid', 'Thyroid Function Test (TFT)')
    ], string='Test Type', required=True)





    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    # These fields are automatically fetched from the selected patient
    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_age = fields.Char(string='Patient Age', related='patient_id.age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', readonly=True)
    blood_sugar = fields.Float(string="Blood Sugar (mg/dL)")
    hemoglobin = fields.Float(string="Hemoglobin (g/dL)")
    wbc_count = fields.Float(string="WBC Count (cells/mcL)")
    rbc_count = fields.Float(string="RBC Count (millions/mcL)")
    tsh = fields.Float(string="TSH (µIU/mL)")

