from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HospitalICUBooking(models.Model):
    _name = 'hospital.icu.booking'
    _description = 'ICU Bed Booking'
    _order = 'start_datetime desc'

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    bed_id = fields.Many2one('hospital.icu.bed', string='ICU Bed', required=True)
    start_datetime = fields.Datetime(string='Start Time', default=fields.Datetime.now)
    end_datetime = fields.Datetime(string='End Time')
    notes = fields.Text(string='Notes')

    @api.model
    def create(self, vals):
        bed = self.env['hospital.icu.bed'].browse(vals.get('bed_id'))
        if bed.booking_id and not bed.booking_id.end_datetime:
            raise ValidationError('This bed is already booked.')
        booking = super(HospitalICUBooking, self).create(vals)
        bed.booking_id = booking
        bed.status = 'occupied'
        bed.patient_id = booking.patient_id
        bed.assigned_date = booking.start_datetime
        return booking

    def write(self, vals):
        res = super(HospitalICUBooking, self).write(vals)
        for record in self:
            if vals.get('end_datetime'):
                record.bed_id.booking_id = False
                record.bed_id.status = 'available'
                record.bed_id.patient_id = False
                record.bed_id.assigned_date = False
        return res

    def action_save_icu_save(self):
        # In Odoo, record is auto-saved on changes.
        # This is just for demonstration.
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Saved',
                'message': 'icu booking saved successfully!',
                'type': 'success',
                'sticky': False,
            }
        }

    # @api.model
    # def create(self, vals):
    #     booking = super().create(vals)
    #     if booking.bed_id:
    #         booking.bed_id.status = 'occupied'
    #         booking.bed_id.is_available = False
    #     return booking
