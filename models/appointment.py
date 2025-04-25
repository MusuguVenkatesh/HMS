from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Patient Appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('res.users', string="Doctor", required=True)
    appointment_date = fields.Datetime(string="Appointment Date", default=fields.Datetime.now)
    reason = fields.Text(string="Reason for Visit")
    fee = fields.Float(string='Appointment Fee')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="Status", default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_save_appointment(self):
            # In Odoo, record is auto-saved on changes.
            # This is just for demonstration.
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Saved',
                    'message': 'Appointment record saved successfully!',
                    'type': 'success',
                    'sticky': False,
                }
            }





appointment_type = fields.Selection([
    ('checkup', 'General Checkup'),
    ('followup', 'Follow-up'),
    ('emergency', 'Emergency'),
], string="Appointment Type")

duration = fields.Float(string="Duration (hrs)")

notes = fields.Html(string="Doctor's Notes")

is_first_visit = fields.Boolean(string="First Visit")




