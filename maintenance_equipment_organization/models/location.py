from odoo import api, fields, models


class MaintenanceEquipmentLocations(models.Model):
    _name = "maintenance.equipment.location"

    organization = fields.Many2one('maintenance.equipment.organization', string="Organization")

    location = fields.Char(string='Locations')

    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.location))
        return result
