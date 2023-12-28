from odoo import models, fields, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    organization_id = fields.Many2one('maintenance.equipment.organization', string='Organization')
    location_id = fields.Many2one('maintenance.equipment.location', string='Location')
    sub_location_id = fields.Many2one('maintenance.equipment.sub_location', string='Sub-Location')

    @api.onchange('organization_id')
    def _onchange_organization_id(self):
        self.location_id = False
        self.sub_location_id = False

    @api.onchange('location_id')
    def _onchange_location_id(self):
        self.sub_location_id = False


class MaintenanceEquipmentOrganization(models.Model):
    _name = "maintenance.equipment.organization"
    _description = "Maintenance Equipment Organization"

    organization = fields.Char(string="Organization")
    company_id = fields.Many2one('res.company', string='Company Name')
    active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.organization))
        return result


class MaintenanceEquipmentLocation(models.Model):
    _name = "maintenance.equipment.location"

    organization = fields.Many2one('maintenance.equipment.organization', string="Organization")
    location = fields.Char(string='Locations')
    is_active = fields.Boolean(string='Is Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.location))
        return result


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
