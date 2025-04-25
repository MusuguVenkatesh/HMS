from odoo import models, fields


class CardiacTest(models.Model):
    _name = 'cardiac.test'
    _description = 'Cardiac Test'

    test_type = fields.Selection([
        ('ecg', 'ECG'),
        ('echo', 'Echocardiogram'),
        ('bp', 'Blood Pressure'),
        ('troponin', 'Troponin'),
        ('lipid', 'Lipid Profile')
    ], string='Test Type', required=True)

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_age = fields.Char(string='Patient Age', related='patient_id.age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', readonly=True)

    systolic_bp = fields.Integer(string="Systolic BP (mmHg)")
    diastolic_bp = fields.Integer(string="Diastolic BP (mmHg)")
    ecg_result = fields.Text(string="ECG Report")
    echo_result = fields.Text(string="Echocardiogram Report")
    troponin_level = fields.Float(string="Troponin (ng/mL)")

    # Lipid Profile
    total_cholesterol = fields.Float(string="Total Cholesterol (mg/dL)")
    hdl = fields.Float(string="HDL (mg/dL)")
    ldl = fields.Float(string="LDL (mg/dL)")
    triglycerides = fields.Float(string="Triglycerides (mg/dL)")


