
# -*- coding: utf-8 -*-
{
    'name': "Payslipbatch Duplication",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sailotech",
    'website': "http://www.Sailotech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'payslipbatchtype',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['hr_payroll','base'],

    # always loaded
    'data': [        
        
        # 'views/tax_deduction_description_view.xml',
        'wizard/payslip_batch_wizard_view.xml',
          'views/payslipbatch_duplication_view.xml',
          

         
         
     ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}