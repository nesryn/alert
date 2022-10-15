# -*- coding: utf-8 -*-
import base64

from odoo import models, fields, api

from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)

    @api.onchange('order_line')
    def show_alert(self):
        print('aaaaaaaa',self)
        print('aaaaaaaa',self.order_line.ids)
        ordes_ids = []
        for rec in self.order_line:
            print(rec.product_id)
            (ordes_ids)
            if rec.product_id.id in ordes_ids and  self.env.user.has_group('base.group_no_one'):
                raise ValidationError(
                    ('vous avez ajouté l’article … en double')
                 )
            ordes_ids.append(rec.product_id.id)
            print

