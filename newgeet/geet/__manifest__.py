# -*- coding: utf-8 -*-
{
    'name': "geet",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website', 'web'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'Report/student_report.xml',
        'views/index.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/student.xml',
        'static/src/xml/index_temp.xml',
        'static/src/xml/Boot_temp.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'qweb': ['static/src/xml/index_temp.xml'],
}
