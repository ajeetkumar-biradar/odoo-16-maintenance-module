from odoo import api, fields, models


class MaintenanceEquipmentStatus(models.Model):
    _name = "maintenance.equipment.brand"

    brand = fields.Char(string='Brand')

    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.brand))
        return result
