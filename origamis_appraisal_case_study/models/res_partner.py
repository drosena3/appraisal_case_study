import requests

from odoo import _, api, fields, models

KEY = 'c3d98f7dd'

# Editing existing model
class ResPartner(models.Model):
    '''Overriding model from odoo/odoo from module base to module origamis_ares'''
    _inherit = 'res.partner'

    salutation = fields.Selection([('first_name', 'First Name'),
                             ('last_name', 'Last Name')], string='Salutation')
    
    form_of_address = fields.Selection([('informal_address', 'Informal Address'),
                             ('formal_address', 'Formal Address')], string='Forms of Address')
    
    generated_salutation = fields.Char(compute='_compute_generated_salutation', string='Generated Salutation', store=True)

    @api.depends('salutation', 'form_of_address', 'is_company')
    def _compute_generated_salutation(self):
        for rec in self:
            rec.generated_salutation = False
            # Conditions that must be set
            if rec.salutation and rec.form_of_address and not rec.is_company and rec.name:
                url_base = f'https://www.sklonovani-jmen.cz/api?klic={KEY}&pad=5&osloveni-muze=pane&osloveni-zeny=paní&pohlavi=0&tvar=1'
                jmeno = rec.name
                pouzivat_krestni, pouzit_prijmeni = (('ano', 'ne') if rec.salutation == 'first_name' else ('ne', 'ano'))   
                pouzit_osloveni = 'ne' if rec.form_of_address == 'informal_address' else 'ano'
                url = url_base + f'&jmeno={jmeno}&pouzit-krestni={pouzivat_krestni}&pouzit-osloveni={pouzit_osloveni}&pouzit-prijmeni={pouzit_prijmeni}'
                response = requests.get(url)
                generated_salutation = response.text
                rec.generated_salutation = generated_salutation
