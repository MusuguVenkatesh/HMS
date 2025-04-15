from odoo import fields, models

class LabTest(models.Model):
    _name = 'hospital.labtest'
    _description = 'Lab Test'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    test_name = fields.Char(string="Test Name")
    test_date = fields.Date(string="Test Date", default=fields.Date.today)
    result = fields.Text(string="Test Result")
    attachment = fields.Binary(string="Attach Report")
    price = fields.Float(string="Price")
    billing_id = fields.Many2one('hospital.billing', string='Billing')



