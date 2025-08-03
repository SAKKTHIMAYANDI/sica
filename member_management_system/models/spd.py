from odoo import fields,models,api,_

class SpdCategory(models.Model):
    _name = 'spd.category'
    _description = 'SPD Category'

    name = fields.Char(string='Category Name')
    description = fields.Text()

class SubCategory(models.Model):
    _name = 'spd.sub.category'
    _description = 'SPD Sub Category'

    name = fields.Char(string='Name', required=True)
    company_name = fields.Char(string='Company Name')
    vendor_type = fields.Selection([
        ('vendor', 'Vendor'),
        ('supplier', 'Supplier'),
        # Add more choices as needed
    ], string='Vendor Type')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    photo = fields.Binary(attachment=True,
                          help='Upload an image')
    website = fields.Char(string='Website')
    address = fields.Text(string='Address')
    product_id = fields.Many2one('spd.product')
    category_id = fields.Many2one('spd.category')


class ProductProduct(models.Model):
    _name = 'spd.product'
    _description = 'SPD Product'

    name = fields.Char()
    description = fields.Char()
    vendor_ids = fields.One2many('product.vendor', 'product_id')

class ProductVendorList(models.Model):
    _name = 'product.vendor'
    _description = 'Product Description'

    product_id = fields.Many2one('spd.product')
    vendor_id = fields.Many2one('spd.sub.category')
    company_name = fields.Char(string='Company Name', related='vendor_id.company_name')
    vendor_type = fields.Selection([
        ('vendor', 'Vendor'),
        ('supplier', 'Supplier'),
        # Add more choices as needed
    ], string='Vendor Type', related='vendor_id.vendor_type')

    email = fields.Char(string='Email', related='vendor_id.email')

class Spdbannerphoto(models.Model):
    _name = 'spd.banner.photo'
    _description = 'Spd vendor Photo'

    name = fields.Char()
    photo = fields.Binary(attachment=True,
        help='Upload an image')
    promotion_link = fields.Char()
    description = fields.Char()