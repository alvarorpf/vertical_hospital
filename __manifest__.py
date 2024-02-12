# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Vertical Hospital",
    "version": "16.0.0",
    "description": """
    
    """,
    "author": "Alvaro Renato Paredes Flores",
    'category': '',
    "depends": ['base','mail'],
    "data": [
        # Data
        'data/data_hospital.xml',
        # Security
        'security/ir.model.access.csv',
        # Confs

        # Main Menus
        'views/menus.xml',
        # Views
        'views/hospital_patient_views.xml',
        'views/hospital_treatment_views.xml',
        'views/res_config_settings_views.xml',
        # Reports
        'reports/hospital_patient_reports.xml',
        # Wizards

    ],
    'demo': [

    ],
    'license': 'LGPL-3',
}
