# -*- coding: utf-8 -*-
{
    'name': "support_sys",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,
    'sequence': 1,

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'sale', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/ticket_history.xml',
        'views/new_ticket.xml', 'views/ticket_list.xml', 'views/email_templates.xml','views/homepage.xml','views/emp_expense.xml','views/employee_history.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'support_sys/static/src/components/**/*.js',
            'support_sys/static/src/components/**/*.xml',
            # 'support_sys/static/src/scss/**/*.scss',
            # 'support_sys/static/src/components/chart_renderer/chart_renderer.js',
            # 'support_sys/static/src/components/chart_renderer/chart_renderer.xml',
            # 'support_sys/static/src/components/kpi_card/kpi_card.js'
            # 'support_sys/static/src/components/kpi_card/kpi_card.xml'
        ],


        'web.assets_frontend': [
            'support_sys/static/src/css/nepali.datepicker.v4.0.1.min.css',

        ]

    }
}