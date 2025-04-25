# -*- coding: utf-8 -*-
{
    'name': "patient",
    'summary': "Hospital Management System with ICU Bed Booking",
    'description': """
Full-featured Hospital Management System including:
- Patient Management
- Appointments
- ICU Bed Booking System
- Medical History, Vital Signs, Medication Plans
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Healthcare',
    'version': '1.0.1',
    'sequence': 5,
    'depends': ['base'],

    'data': [
       # 'security/security.xml',
        'security/ir.model.access.csv',

        'views/patient_view.xml',
        'views/menu_views.xml',
        'views/appointment_views.xml',
        'views/doctor_note_views.xml',
        'views/medical_history_views.xml',
        'views/vital_sign_views.xml',

        'views/hospital_medication_plan_line_views.xml',
        'views/labtest_views.xml',
        'views/bloodtest_views.xml',
        'views/urinetest_views.xml',
        'views/cardiactest_views.xml',
        'views/rapiddiagnostic_views.xml',
        'views/imagingtest_views.xml',

    #     'views/medicalbillreport_views.xml',
    #     'views/medicalbill_views.xml',
    # # QWeb template

        # Views
       # 'views/medicalbillreport_views.xml',
        'views/medicalbill_views.xml',
        'report/report_medical_bill.xml',


        # ICU Bed Booking System Views
        'views/icu_bed_views.xml',
        'views/icu_booking_views.xml',

        # ICU Bed Data
        'data/icu_bed_data.xml',
       # 'data/icu_bed_cron.xml',
    ],

    'assets': {
        'web.assets_backend.css': [
            # HMS Custom Assets
            'patient/static/src/css/custom.css',
           'patient/static/src/img/bed.png',
          'patient/static/src/css/appointment_colors.css',
          # 'patient/static/src/js/reset_form.js',
         'patient/static/src/css/custom_buttons.css',

            # ICU Bed Layout Assets
            'patient/static/src/css/icu_bed.css',

             'patient/static/src/css/bed.css',
          #  'HMS/static/src/img/bed.png',
          'patient/static/description/bed1.png'
            # Optional future widget
            # 'patient/static/src/js/icu_bed_widget.js',
        ],
    },
            'web.assets_frontend': [
            'patient/static/src/js/reset_form.js',
        ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
