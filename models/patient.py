
try:
    from odoo import fields, models, api
except ImportError:
    raise ImportError("The 'odoo' module must be installed and properly configured to use Odoo fields and models.")
from datetime import date


class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Management'

    patient_id = fields.Char(string="Patient ID", required=True, copy=False, readonly=True, default='New')
    date_of_birth = fields.Date(string='Date of Birth')
    name = fields.Char(string="Name", required=True)
    state_id = fields.Many2one(
        'res.country.state',
        string="State",
        domain="[('country_id.code', '=', 'IN')]"
    )

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                dob = record.date_of_birth
                years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = years
            else:
                record.age = 0

    @api.depends('date_of_birth')
    def _compute_age_display(self):
        for record in self:
            if record.date_of_birth:
                today = date.today()
                dob = record.date_of_birth
                delta = today - dob

                if delta.days >= 0:
                    years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                    days = (today - dob.replace(year=today.year)).days
                    if days < 0:
                        days += 365
                    record.age_display = f"{years} year(s) and {days} day(s) old"
                else:
                    record.age_display = f"Will be born in {abs(delta.days)} day(s)"
            else:
                record.age_display = "Date of birth not set"

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender')

    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    age_display = fields.Char(string='Age Display', compute='_compute_age_display')
    contact_number = fields.Char(string="Contact Number")
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
    ], string='Blood Group')

    martial_status = fields.Selection([('single','Single'),('Married','Married'),('divorce','Divorce')])
    address = fields.Text(string="Address")
    case_description = fields.Text(string='Case Description')

    def action_save_patient(self):
        # In Odoo, record is auto-saved on changes.
        # This is just for demonstration.
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

    def action_reset_form(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Reset',
                'message': 'Form data cleared.',
                'type': 'warning',
                'sticky': False,
            }
        }



