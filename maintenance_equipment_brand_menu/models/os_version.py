from odoo import api, fields, models


class MaintenanceOperatingSystemVersion(models.Model):
    _name = "maintenance.equipment.os.version"

    os_id = fields.Many2one('maintenance.equipment.os', string='Operating System')

    version = fields.Char(string='OS Version')

    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.version))
        return result
