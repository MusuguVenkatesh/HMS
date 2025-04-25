from odoo import models, fields

class ImagingTest(models.Model):
    _name = 'imaging.test'
    _description = 'Imaging Test'

    test_type = fields.Selection([
        ('xray', 'X-Ray'),
        ('ct', 'CT Scan'),
        ('mri', 'MRI'),
        ('ultrasound', 'Ultrasound'),
        ('mammography', 'Mammography'),
    ], string='Test Type', required=True)

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_name = fields.Char(string='Patient Name', related='patient_id.name', readonly=True)
    patient_age = fields.Char(string='Patient Age', related='patient_id.age', readonly=True)
    patient_gender = fields.Selection(related='patient_id.gender', readonly=True)


    image = fields.Binary(string='Upload Image')
    image_filename = fields.Char(string='Image Filename')
    date_taken = fields.Date(string='Date Taken', default=fields.Date.today)

