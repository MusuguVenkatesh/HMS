from odoo import models, fields


class HospitalMedicalHistory(models.Model):
    _name = 'hospital.medical.history'
    _description = 'Medical History'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    patient_age = fields.Char(string="Age", related='patient_id.age', store=True)
    patient_name = fields.Char(string="Patient Name", related='patient_id.name', store=True)
    diagnosis_date = fields.Date(string="Diagnosed On")
    condition = fields.Char(string="Condition")
    notes = fields.Text(string="Details")
    test_type = fields.Selection([
        ('blood', 'Blood Test'),
        ('cardiac', 'Cardiac Test'),
        ('urine', 'Urine Test'),
        ('imaging', 'Imaging'),
        ('rapid', 'Rapid Test'),
    ], string="Test Type")

    medicine_line_ids = fields.One2many('hospital.medicine.line', 'history_id', string="Medicines")

    def action_save_patient(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Saved',
                'message': 'Patient record saved successfully!',
                'type': 'success',
                'sticky': False,
            }
        }
