from odoo import api, fields, models


class MaintenanceOperatingSystem(models.Model):
    _name = "maintenance.equipment.os"

    os = fields.Char(string='Operating System')

    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.os))
        return result
