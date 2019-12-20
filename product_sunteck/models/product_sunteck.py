from odoo import fields, models

class Sunteck(models.Model):
    _name = 'product.sunteck'
    _description = 'sunteck products'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
