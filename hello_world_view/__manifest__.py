# -*- coding: utf-8 -*-
{
    'name': "Hello World",

    'summary': "Say Hello",
    'description': """
        Say Hellow to the world
    """,

    'version': '0.1',
    'depends': ['web', 'contacts', 'base_geolocalize'],
    'data': [
        "views/assets.xml",
        "views/data.xml"
    ],
    'qweb': [],
    'installable': True,
    'auto_install': True
}