# models/models.py

from odoo import models, fields, api


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.request'

    team_members = fields.Many2many(
        'res.users',
        string='Team Members',
        compute='_compute_team_members',
        readonly=False,
        store=True,
        domain=lambda self: [('id', 'in', self._compute_team_member_ids())],
    )

    def _compute_team_member_ids(self):
        return self.maintenance_team_id.member_ids.ids

    @api.depends('maintenance_team_id', 'maintenance_team_id.member_ids')
    def _compute_team_members(self):
        for equipment in self:
            equipment.team_members = equipment._compute_team_member_ids() if equipment.maintenance_team_id else False
