# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCity(models.Model):
    _inherit = "res.city"

    department_id = fields.Many2one(
        'res.country.department',
        string='Department',
        help='Department of this city'
    )
