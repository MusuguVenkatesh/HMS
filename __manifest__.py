# -*- coding: utf-8 -*-
{
    'name': "patient",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': 5,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/patient_view.xml',
    'views/menu_views.xml',
    'views/appointment_views.xml',
    'views/labtest_views.xml',
    'views/prescription_views.xml',
    'views/doctor_note_views.xml',
    'views/billing_views.xml',
    'views/medical_history_views.xml',
    'views/vital_sign_views.xml',
    'views/medication_plan_views.xml',
    'views/icu_bed_views.xml',
],

    'demo': [

    ],
'assets': {
    'web.assets_backend': [
        'patient/static/src/css/custom.css',
        'patient/static/src/img/bed.png',


    ],
},


    "installable":True,
    "application":True,
    "License":"LGPl-3"
}

