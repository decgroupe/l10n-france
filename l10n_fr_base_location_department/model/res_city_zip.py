# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCityZip(models.Model):
    _inherit = "res.city.zip"

    department_id = fields.Many2one(
        'res.country.department',
        string='Department',
        related='city_id.department_id',
        help='Department of this city'
    )
