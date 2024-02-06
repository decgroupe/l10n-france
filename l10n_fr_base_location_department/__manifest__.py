# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "French Departments (base_location support)",
    "summary": "Add French Departments (Départements) supports to Location"
    "management (aka Better ZIP)",
    "version": "14.0.1.0.0",
    "category": "French Localization",
    "author": "DEC, " "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-france",
    "license": "AGPL-3",
    "depends": [
        "base_location",
        "l10n_fr_base_address_city_department",
    ],
    "data": [
        "view/res_city.xml",
    ],
    "post_init_hook": "set_department_and_state_on_res_city",
    "installable": True,
}
