import base64
from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError
from odoo.exceptions import ValidationError
from datetime import datetime

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    field_1 = fields.Float("Field One")
    field_2 = fields.Integer("Field OTwo")
    #field_two = fields.Float("Field Two")