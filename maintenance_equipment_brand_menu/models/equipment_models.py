from odoo import api, fields, models


class MaintenanceEquipmentModels(models.Model):
    _name = "maintenance.equipment.models"

    brand = fields.Many2one('maintenance.equipment.brand', string="Brand")

    model = fields.Char(string='Models')

    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.model))
        return result
