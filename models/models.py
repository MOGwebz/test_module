#-*- coding: utf-8 -*-

from odoo import models, fields, api


class test_module(models.Model):
    _name = 'test_module.test_module'
    _description = 'test_module.test_module'

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    @api.depends('field_one', 'field_two')
    def _value_pc(self):
        for rec in self:
            rec.field_3 = rec.field_one / rec.field_two if (rec.field_one > 0 or rec.field_one < 0) and (rec.field_two  > 0 or rec.field_two  < 0) else 0
    field_one = fields.Integer('Field One', default=0.25)
    field_two = fields.Integer('Field Two', default=0.25)
    field_3 = fields.Float('Field Three', compute=_value_pc)

    
