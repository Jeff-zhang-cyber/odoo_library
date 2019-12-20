from odoo import api, fields, models

class Sproduct(models.Model):
    _inherit = 'product.template'
    #is_available = fields.Boolean('Is Available?')
    sale_ok=fields.Boolean('Can be sold,why?', defualt=False)
    serialNo = fields.Char("Sn",required=True)
    #publisher_id = fields.Many2one(index=True)
        

