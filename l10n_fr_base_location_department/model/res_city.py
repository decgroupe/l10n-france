# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResCity(models.Model):
    _inherit = "res.city"

    _sql_constraints = [
        (
            'name_state_country_uniq', 'Check(1=1)',
            'Invalid constraint disabled'
        ),
    ]

    @api.onchange('state_id')
    def _onchange_state(self):
        domain = []
        if self.state_id:
            domain = [('state_id', '=', self.state_id.id)]
        return {'domain': {'department_id': domain}}
