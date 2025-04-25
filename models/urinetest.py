from odoo import models, fields
class UrineTest(models.Model):
    _name = 'urine.test'
    _description = 'Urine Test'

    test_type = fields.Selection([
        ('routine', 'Routine Urine Test'),
        ('albumin', 'Urine Albumin'),
        ('glucose', 'Urine Glucose'),
        ('pregnancy', 'Pregnancy Test (hCG)'),
        ('ketones', 'Urine Ketones'),
        ('culture', 'Urine Culture')
    ], string='Test Type', required=True)

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    # These fields are automatically fetched from the selected patient
    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_age = fields.Char(string='Patient Age', related='patient_id.age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', readonly=True)

    urine_color = fields.Char(string="Urine Color")
    urine_ph = fields.Float(string="Urine pH")
    glucose = fields.Float(string="Glucose (mg/dL)")
    albumin = fields.Float(string="Albumin (mg/dL)")
    ketones = fields.Float(string="Ketones (mg/dL)")
    leukocytes = fields.Float(string="Leukocytes (cells/mcL)")
    nitrites = fields.Selection([
        ('positive', 'Positive'),
        ('negative', 'Negative')
    ], string="Nitrites")
    pregnancy_test = fields.Selection([
        ('positive', 'Positive'),
        ('negative', 'Negative')
    ], string="Pregnancy Test (hCG)")
    culture_result = fields.Text(string="Culture Result")


