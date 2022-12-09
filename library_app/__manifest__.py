# -*- coding: utf-8 -*-
{
    'name': "Gestión de la biblioteca",

    'summary': """
        Gestión del catálogo de la biblioteca y los préstamos de los libros
        """,
   
    'author': "Irene",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # base.module_category_services_library
    'category': 'Services/Library',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    # always loaded
    'data': [
        'security/library_security.xml',
        'views/library_menu.xml',
    ],
    
    'application': True,
}
