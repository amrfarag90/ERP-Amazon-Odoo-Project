from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    supplier_risk = fields.Selection(
        related='partner_id.supplier_risk',
        string="Supplier Risk",
        readonly=True
    )
