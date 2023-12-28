from odoo import fields, models


class CustomInherit(models.Model):
    _inherit = 'maintenance.equipment.category'

    cat_img = fields.Image(string="Image")
