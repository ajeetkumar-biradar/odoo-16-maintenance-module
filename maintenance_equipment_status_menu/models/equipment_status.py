from odoo import api, fields, models


class MaintenanceEquipmentStatus(models.Model):
    _name = "maintenance.equipment.status"

    status = fields.Char(string='Status', required=True)

    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.status))
        return result
