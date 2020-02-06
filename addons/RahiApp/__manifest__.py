# -*- coding: utf-8 -*-

{
    'name': "StorySpac",

    'summary': """
        Custom Odoo module for Initial practice by Rahi""",

    'description': """
        Simple working for practice and learning
    """,

    'author': "Rahi",
    'website': "https://www.fb.com/icerahi/",
    'category': 'Tools',
    'version': '1.0',
    'depends': [
        'base',
      
    ],
    'data': [
        'views/view.xml',
        'views/view2.xml',
    ],
    'qweb': [''],
    'images': ["static/storyspac.gif"],
    'license': "",
    'installable': True,
    'application': True,
    'sequence': 1,
}
