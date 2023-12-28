from odoo import models, fields, api


class MaintenanceEquipmentBrand(models.Model):
    _name = 'maintenance.equipment.brand'
    _description = 'Equipment Brand'

    brand = fields.Char(string='Brand Name', required=True)
    model_ids = fields.One2many('maintenance.equipment.models', 'brand', string='Models')
    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for brand in self:
            result.append((brand.id, brand.brand))
        return result


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    status_id = fields.Many2one('maintenance.equipment.status', string='Status', domain=[('is_active', '=', True)])
    os_id = fields.Many2one('maintenance.equipment.os', string='Operating System', domain=[('is_active', '=', True)])
    version_id = fields.Many2one('maintenance.equipment.os.version', string='OS Version',
                                 domain=[('is_active', '=', True)])
    brand_id = fields.Many2one('maintenance.equipment.brand', string='Brand')
    model_id = fields.Many2one('maintenance.equipment.models', string='Model', domain="[('brand', '=', brand_id)]")

    @api.onchange('brand_id')
    def _onchange_brand_id(self):
        self.model_id = False


class MaintenanceEquipmentModels(models.Model):
    _name = "maintenance.equipment.models"

    brand = fields.Many2one('maintenance.equipment.brand', string="Brand")
    model = fields.Char(string='Model')
    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for model in self:
            name = f"{model.model}" if model.brand and model.model else model.model
            result.append((model.id, name))
        return result
