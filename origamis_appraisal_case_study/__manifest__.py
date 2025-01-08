# -*- coding: utf-8 -*-
{
    'name': 'Appraisal Case Study',
    'category': 'Contacts',
    'summary': 'Appraisal Case Study',
    'version': '17.0.0.0.1',
    'website': 'https://origamis.cz',
    'author': 'Origamis',
    'depends': [
        #base odoo/odoo modules  
        'base', 
        'contacts',

    ],
    'data': [
            'views/res_partner_views.xml',
            ],
            
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}
