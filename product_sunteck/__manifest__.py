{
    'name': 'Sunteck Product',
    'description': 'Manage products of Sunteck',
    'author': 'jeff',
    'depends': ['product','mail',],
    'application': False,
    'data':[
        'security/sunteck_security.xml',
        'views/sparts_view.xml',
        'security/ir.model.access.csv',
        #'views/library_menu.xml',
        #'views/member_view.xml',
        #'views/book_list_template.xml',
    ]
}
