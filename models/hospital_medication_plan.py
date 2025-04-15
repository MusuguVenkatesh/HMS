from odoo import models, fields

class HospitalMedicationPlan(models.Model):
    _name = 'hospital.medication.plan'
    _description = 'Medication Plan'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    medication_name = fields.Char(string="Medication")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    dosage = fields.Char(string="Dosage")
    frequency = fields.Char(string="Frequency")
    instructions = fields.Text(string="Instructions")
