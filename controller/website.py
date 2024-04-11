from odoo import http
from odoo.http import request


class SoldProducts(http.Controller):
    @http.route('/most_sold_products', type='json', auth="public")
    def most_sold_products(self):
        sold = request.env['product.template'].sudo().search([])
        sold_count = sold.sorted('sales_count', reverse=True)

        values = []
        for rec in sold_count:
            values.append({
                'name': rec.name,
                'website': rec.website_url,
                'image': rec.image_1920
            })
        sold_product = [values[i:i + 4] for i in range(0, len(values), 4)]
        return sold_product


class ViewedProducts(http.Controller):
    @http.route('/most_viewed_products', type='json', auth="public")
    def most_viewed_products(self):
        view = request.env['website.visitor'].sudo().search([])
        view_count = view.sorted('visitor_product_count', reverse=True)

        prod = view_count.mapped('product_ids')
        values = []
        for rec in prod:
            values.append({
                'name': rec.name,
                'website': rec.website_url,
                'image': rec.image_1920
            })
        viewed_product = [values[i:i + 4] for i in range(0, len(values), 4)]
        return viewed_product
