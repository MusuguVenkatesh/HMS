from odoo import models , fields , api

class MedicalBillLine(models.Model):
    _name = 'medical.bill.line'
    _description = 'Medical Bill Line'

    bill_id = fields.Many2one('medical.bill', string='Bill')

    medicine_id = fields.Many2one(
        'medicine.master',
        string='Medicine',
        required=True,
        ondelete='restrict',
        help='Select or create a medicine'
    )

    cost = fields.Float(string='Cost')
    quantity = fields.Integer(string='Quantity', default=1)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('cost', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.cost * line.quantity


