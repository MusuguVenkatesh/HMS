from odoo import models, fields

class HospitalMedicalHistory(models.Model):
    _name = 'hospital.medical.history'
    _description = 'Medical History'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    condition = fields.Char(string="Condition")
    diagnosis_date = fields.Date(string="Diagnosed On")
    notes = fields.Text(string="Details")
