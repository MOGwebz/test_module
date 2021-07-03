import base64
from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError
from odoo.exceptions import ValidationError
from datetime import datetime

class XpertModel(models.Model):
    _name = 'xpert.model'

    field_one = fields.Integer('Field One')