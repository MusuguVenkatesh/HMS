from odoo import models, fields

class MedicationPlanLine(models.Model):
    _name = 'hospital.medication.plan.line'
    _description = 'Medication Plan Line'





    medicine_name = fields.Char(string='Medicine', required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)

    duration = fields.Integer(string='Duration (days)')
    dosage = fields.Char(string="Dosage")
    frequency_morning = fields.Boolean(string='Morning')
    frequency_afternoon = fields.Boolean(string='Afternoon')
    frequency_evening = fields.Boolean(string='Evening')
    frequency_night = fields.Boolean(string='Night')
    instruction = fields.Text(string='Instructions')
    medication_line_ids = fields.One2many('hospital.medication.plan.line', 'patient_id',string='Medications')
    note = fields.Text(string="Instructions")

    def action_save_medication_line(self):
        # You can add custom logic here, validations etc.
        # This is already saved in memory (form view will call this on current record)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "Saved!",
                'message': "Medication Line saved successfully.",
                'type': 'success',
                'sticky': False,
            }
        }