{
    'name':'Library Book Borrowing',
    'description':'Members can borrow books from the library',
    'author':'Harvey Zhang',
    'depends':['library_member'],
    'data':[
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/checkout_view.xml',
        'data/library_checkout_stage.xml',
        ],
}