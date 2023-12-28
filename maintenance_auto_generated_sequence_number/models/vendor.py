from odoo import models, fields, api


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    sequence_number = fields.Char(string='Ticket Id', readonly=True, copy=False)

    def _compute_sequence_number(self):
        for record in self:
            sequence = self.env['ir.sequence'].next_by_code('maintenance.request.sequence') or '/'
            record.sequence_number = sequence

    def _create_sequence_number(self):
        for record in self:
            if not record.sequence_number:
                record._compute_sequence_number()

    @api.model
    def create(self, vals):
        record = super(MaintenanceRequest, self).create(vals)
        record._create_sequence_number()
        return record
