import base64
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource


class HospitalICUBed(models.Model):
    _name = 'hospital.icu.bed'
    _description = 'ICU Bed'
    _order = 'name'

    name = fields.Char(required=True)
    code = fields.Char()
    is_available = fields.Boolean(default=True, compute="_compute_availability", store=True)
    booking_id = fields.Many2one('hospital.icu.booking',string="Current Booking",ondelete='set null')
    patient_id = fields.Many2one('hospital.patient', string="Assigned Patient")
    assigned_date = fields.Datetime(string="Assigned Date")
    status = fields.Selection([('available', 'Available'),('occupied', 'Occupied'),
    ], string="Status", default='available', tracking=True)
    bed_image = fields.Image(string="ICU Bed Image", default=lambda self: self._get_default_image())

    @api.depends('booking_id', 'booking_id.end_datetime')
    def _compute_availability(self):
        for bed in self:
            bed.is_available = not bed.booking_id or bool(bed.booking_id.end_datetime)

    def _get_default_image(self):
        image_path = get_module_resource('HMS', 'static/description', 'bed1.png')
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read())

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            name = vals.get('name')
            if not name or name.isnumeric():
                raise ValidationError("Invalid ICU Bed name. Please use names like 'ICU Bed A1'.")
            if self.env['hospital.icu.bed'].search([('name', '=', name)]):
                raise ValidationError(f"ICU Bed with name '{name}' already exists.")
        return super().create(vals_list)

    def unlink(self):
        for bed in self:
            if bed.booking_id and not bed.booking_id.end_datetime:
                raise ValidationError("You cannot delete a bed that is currently booked.")
            bed.booking_id = False  # Remove the link before deletion
        return super().unlink()

    @api.depends('booking_id', 'booking_id.end_datetime')
    def _compute_status(self):
        for bed in self:
            if bed.booking_id and not bed.booking_id.end_datetime:
                bed.status = 'occupied'
            else:
                bed.status = 'available'

            @api.model
            def create(self, vals):
                existing = self.search([('name', '=', vals.get('name'))], limit=1)
                if existing:
                    raise ValidationError(f"ICU Bed with name '{vals['name']}' already exists.")
                return super(HospitalICUBed, self).create(vals)

    def action_save_icu_bed_save(self):
                # In Odoo, record is auto-saved on changes.
                # This is just for demonstration.
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Saved',
                        'message': 'icu bed record saved successfully!',
                        'type': 'success',
                        'sticky': False,
                    }
                }

