from odoo import models, fields

class RapidDiagnosticTest(models.Model):
    _name = 'rapid.diagnostic.test'
    _description = 'Rapid Diagnostic Test'

    test_type = fields.Selection([
        ('malaria', 'Malaria Test'),
        ('dengue', 'Dengue Test'),
        ('covid19', 'COVID-19 Test'),
        ('typhoid', 'Typhoid Test'),
    ], string='Test Type', required=True)

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_age = fields.Char(string='Patient Age', related='patient_id.age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', readonly=True)

    test_result = fields.Selection([
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ], string='Test Result', required=True)

    test_date = fields.Date(string='Test Date', default=fields.Date.context_today)
    remarks = fields.Text(string='Remarks')

