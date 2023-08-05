# Copyright 2013-2016 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# Copyright 2014 Serv. Tecnol. Avanzados - Pedro M. Baeza
# Copyright 2016 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountPaymentMode(models.Model):
    _inherit = "account.payment.mode"

    initiating_party_issuer = fields.Char(
        string="Initiating Party Issuer",
        size=35,
        help="This will be used as the 'Initiating Party Issuer' in the "
        "PAIN files generated by Odoo. If not defined, Initiating Party "
        "Issuer from company will be used.\n"
        "Common format (13): \n"
        "- Country code (2, optional)\n"
        "- Company idenfier (N, VAT)\n"
        "- Service suffix (N, issued by bank)",
    )
    initiating_party_identifier = fields.Char(
        string="Initiating Party Identifier",
        size=35,
        help="This will be used as the 'Initiating Party Identifier' in "
        "the PAIN files generated by Odoo. If not defined, Initiating Party "
        "Identifier from company will be used.\n"
        "Common format (13): \n"
        "- Country code (2, optional)\n"
        "- Company idenfier (N, VAT)\n"
        "- Service suffix (N, issued by bank)",
    )
    initiating_party_scheme = fields.Char(
        string="Initiating Party Scheme",
        size=35,
        help="This will be used as the 'Initiating Party Scheme Name' in "
        "the PAIN files generated by Odoo. This value is determined by the "
        "financial institution that will process the file. If not defined, "
        "no scheme will be used.\n",
    )
