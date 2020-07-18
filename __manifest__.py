# -*- coding: utf-8 -*-
{
    'name': "game modification",

    'summary': """
        Game custom addon for my favorite game""",

    'description': """
        My long description of game addon must be here, but.........
            """,

    'author': "Vadim Bardier",
    'website': "http://www.Github.com/GithubHungry",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Game mods',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/match_card.xml',
        'views/match.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
