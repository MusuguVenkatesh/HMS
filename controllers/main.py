from odoo import http
from odoo.http import request

class MedicalReceiptController(http.Controller):

    @http.route(['/medical/receipt/<int:bill_id>'], type='http', auth='user', website=True)
    def medical_receipt(self, bill_id):
        bill = request.env['medical.bill'].sudo().browse(bill_id)
        return request.render('HMS.medical_receipt_template', {
            'doc': bill
        })
