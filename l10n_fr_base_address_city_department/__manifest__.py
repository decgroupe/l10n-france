# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "French Departments (base_address_city support)",
    "summary": "Add French Departments (Départements) supports to built-in city model",
    "version": "14.0.1.0.0",
    "category": "French Localization",
    "author": "DEC, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-france",
    "license": "AGPL-3",
    "depends": [
        "base_address_city",
        "l10n_fr_department",
    ],
    "data": [
        "view/res_city.xml",
    ],
    "installable": True,
}
