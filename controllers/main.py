from odoo import http
# from odoo.http import request
#
# class HospitalICUController(http.Controller):
#
#     @http.route('/icu_beds', type='http', auth="user", website=True)
#     def display_icu_beds(self, **kwargs):
#         beds = request.env['hospital.icu.bed'].get_all_icu_beds()
#         return request.render('patient.icu_bed_grid_template', {'beds': beds})
