{
    'name': "User Management Module",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
           Store user data
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       
        'security/ir.model.access.csv',
        # 'data/email_template.xml',
        'views/student_view.xml',
        'data/email_template.xml',
        'views/menue.xml',
         
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

