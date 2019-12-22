from odoo import api, fields, models

class Sproduct(models.Model):
    _inherit = 'product.template'
    #is_available = fields.Boolean('Is Available?')
    sale_ok=fields.Boolean("Can be sold?",defualt=False)
    #purchase_ok=fields.Boolean("Can be Purchased?",default=False)
    serialNo = fields.Char("Sn",required=True,index=True)
    partstype=fields.Selection([('elec','Electrical'),('stru','Struct'),('other','Others')])

    @api.multi
    def _check_sn(self):
    	self.ensure_one()
    	snlen=self.serialNo.len()
    	return snlen==10

    @api.multi
    def button_check_sn(self):
    	for part in self:
    		if not part.serialNo:
                raise Warning('Please provide an SN for %s' % part.name)
            if part.serialNo and not book._check_sn():
                raise Warning('%s is an invalid SN' % part.sn)
            return True
