# -*- coding: utf-8 -*-
{
    'name': "Most viewd and Sold Product",
    'version': '17.0.1.0.0',
    'depends': ['base','contacts','product', 'stock', 'sale','website_sale'],
    'category': '',
    'description': """
    summary of this app
    """,
    'data': [
        'views/snippets/most_sold_snippet_view.xml',
        'views/snippets/most_viewed_snippet_view.xml',
             ],
        'assets':{
        'web.assets_frontend': [
            'most_viewed_and_sold_products/static/src/js/snippet.js',
            'most_viewed_and_sold_products/static/src/xml/most_viewed.xml',
            'most_viewed_and_sold_products/static/src/xml/sold_products.xml',

        ],
    },
    # 'demo': [],
    'application': 'True',
    'installable': True,
}