
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

    state = fields.Selection([
        ('draft', 'Draft'),
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged')
    ], string="Status", default='draft')

    @api.model
    def create(self, vals):
        # Check if sequence exists, create it if not
        sequence = self.env['ir.sequence'].sudo().search([('code', '=', 'hospital.patient')], limit=1)
        if not sequence:
            sequence = self.env['ir.sequence'].sudo().create({
                'name': 'Patient ID',
                'code': 'hospital.patient',
                'prefix': 'PAT',
                'padding': 4,
                'number_next': 1,
                'number_increment': 1,
            })

        # Optional: Reset sequence if no patients exist (CAUTION: only for testing)
        if not self.env['hospital.patient'].sudo().search([]):
            sequence.number_next = 1

        if vals.get('patient_id', 'New') == 'New':
            vals['patient_id'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'

        return super(Patient, self).create(vals)


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

                if dob <= today:
                    years = today.year - dob.year
                    months = today.month - dob.month
                    if today.day < dob.day:
                        months -= 1

                    if months < 0:
                        years -= 1
                        months += 12

                    record.age = f"{years} year(s) and {months} month(s) old"
                else:
                    delta = dob - today
                    record.age = f"Will be born in {delta.days} day(s)"
            else:
                record.age = "Date of birth not set"


    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender')

   # age = fields.Integer(string='Age', compute='_compute_age', store=True)
    age = fields.Char(string='Age', compute='_compute_age_display')
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

    #
    # def action_reset_form(self):
    #     return {
    #         'type': 'ir.actions.client',
    #         'tag': 'do_nothing',  # We don't need a specific client action to be executed
    #         'params': {
    #             'type': 'clear_hospital_patient_form',  # This is the custom event type we'll listen for
    #         }
    #     }



