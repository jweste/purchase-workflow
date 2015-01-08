#    Author: Leonardo Pistone
#    Copyright 2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from openerp.tests.common import TransactionCase


class TestSaleWithoutOwner(TransactionCase):

    def test_sale_mto_buy_creates_procurements(self):
        self.so.action_button_confirm()

        proc1 = self.sol.procurement_ids
        self.assertEqual(1, len(proc1))
        self.assertEqual("move", proc1.rule_id.action)


    def XXX_PENDING_test_sale_vci_generates_special_po(self):
        raise

    def XXX_PENDING_test_special_po_makes_delivery_available(self):
        raise

    def setUp(self):
        super(TestSaleWithoutOwner, self).setUp()
        self.SO = self.env['sale.order']
        self.SOL = self.env['sale.order.line']
        self.Quant = self.env['stock.quant']
        self.Procurement = self.env['procurement.order']

        customer = self.env.ref('base.res_partner_2')
        self.product = self.env.ref('product.product_product_36')

        self.Quant.create({
            'qty': 5000,
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'product_id': self.product.id,
        })

        self.so = self.SO.create({
            'partner_id': customer.id,
            'picking_policy': 'direct',
        })
        self.sol = self.SOL.create({
            'name': '/',
            'order_id': self.so.id,
            'product_id': self.product.id,
        })
