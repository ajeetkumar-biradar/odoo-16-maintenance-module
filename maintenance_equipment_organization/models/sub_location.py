from odoo import models, fields


class MaintenanceEquipmentSubLocation(models.Model):
    _name = "maintenance.equipment.sub_location"

    organization = fields.Many2one('maintenance.equipment.organization', string="Organization")
    location = fields.Many2one('maintenance.equipment.location', string="Location")
    sub_location = fields.Char(string='Sub-Location')
    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.sub_location))
        return result
