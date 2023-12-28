from odoo import api, fields, models


class MaintenanceEquipmentLocations(models.Model):
    _name = "maintenance.equipment.organization"
    _description = "Maintenance Equipment Organization"

    organization = fields.Char(string="Organization")

    company_id = fields.Many2one(
        'res.company',
        string='Company Name'
    )

    active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.organization))
        return result
