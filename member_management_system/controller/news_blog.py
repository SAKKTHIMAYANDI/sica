import base64

from odoo import http, fields
from odoo.http import request
import json
import random
import requests
import time,pytz
from datetime import datetime,timedelta,timezone,date
from dateutil.relativedelta import relativedelta


class NewsBlog(http.Controller):

    @http.route('/get/new/tech/talk', type='http', auth='none', methods=['GET'], csrf=False)
    def action_get_new_talk_details(self, **kw):
        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')
        event_image_default_url = request.env['ir.config_parameter'].sudo().get_param('website.event_image_link')
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})

        today = fields.Date.today()
        yesterday = today - relativedelta(days=1)
        tech_talk_vals = []
        tech_talk_ids = request.env['tech.talk'].sudo().search([('create_date', '>=', yesterday), ('create_date', '<=', today)], order="sequence asc")
        for tech_talk in tech_talk_ids:
            image = base_url + '/web/image?' + 'model=tech.talk&id=' + str(tech_talk.id) + '&field=image'
            vals = {
                'title': tech_talk.title or '',
                'date': tech_talk.date.strftime("%Y-%m-%d") if tech_talk.date else '',
                'views': tech_talk.views or 0,
                'link': tech_talk.link,
                'image_url': image
            }
            tech_talk_vals.append(vals)
        return json.dumps({'Tech talk Vals': tech_talk_vals})

    @http.route('/get/tech/talk', type='http', auth='none', methods=['GET'], csrf=False)
    def get_tech_talk_details(self, **kw):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')

        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})
        tech_talk_vals = []
        tech_talk_ids = request.env['tech.talk'].sudo().search([], order="sequence asc")
        for tech_talk in tech_talk_ids:
            image = base_url + '/web/image?' + 'model=tech.talk&id=' + str(tech_talk.id) + '&field=image'
            vals = {
                'title': tech_talk.title or '',
                'date': tech_talk.date.strftime("%Y-%m-%d") if tech_talk.date else '',
                'views': tech_talk.views or 0,
                'link': tech_talk.link,
                'image_url': image
            }
            tech_talk_vals.append(vals)
        return json.dumps({'Tech talk Vals': tech_talk_vals})

    @http.route('/get/new/sica/blog', type='http', auth='none', methods=['GET'], csrf=False)
    def action_get_sica_blog_details(self, **kw):
        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        print("11111111111111111111111111111111111111111111111111111")
        print("api_key: ",api_key)
        print("222222222222222222222222222222222222222222222222222222222")
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')
        event_image_default_url = request.env['ir.config_parameter'].sudo().get_param('website.event_image_link')
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})

        today = fields.Date.today()
        yesterday = today - relativedelta(days=1)
        blog_vals = []
        blog_ids = request.env['sica.blog'].sudo().search([('create_date', '>=', yesterday), ('create_date', '<=', today)], order="sequence asc")
        for blog in blog_ids:
            image = base_url + '/web/image?' + 'model=sica.blog&id=' + str(blog.id) + '&field=image'
            vals = {
                'title': blog.title or '',
                'date': blog.date.strftime("%Y-%m-%d") if blog.date else '',
                'views': blog.views or 0,
                'description': blog.description,
                'image_url': image
            }
            blog_vals.append(vals)
        return json.dumps({'Sica Blog Vals': blog_vals})



    @http.route('/get/sica/blog', type='http', auth='none', methods=['GET'], csrf=False)
    def get_sica_blog_details(self, **kw):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')

        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})
        blog_vals = []
        blog_ids = request.env['sica.blog'].sudo().search([],order="sequence asc")
        for blog in blog_ids:
            image = base_url + '/web/image?' + 'model=sica.blog&id=' + str(blog.id) + '&field=image'
            vals = {
                'title': blog.title or '',
                'date': blog.date.strftime("%Y-%m-%d") if blog.date else '',
                'views': blog.views or 0,
                'description': blog.description,
                'image_url': image
            }
            blog_vals.append(vals)
        return json.dumps({'Sica Blog Vals': blog_vals})

    @http.route('/get/new/sica/news', type='http', auth='none', methods=['GET'], csrf=False)
    def action_get_sica_news_details(self, **kw):
        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')
        event_image_default_url = request.env['ir.config_parameter'].sudo().get_param('website.event_image_link')
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})

        today = fields.Date.today()
        yesterday = today - relativedelta(days=1)
        news_vals = []
        news_ids = request.env['sica.news'].sudo().search([('create_date', '>=', yesterday), ('create_date', '<=', today)], order="sequence asc")
        for news in news_ids:
            image = base_url + '/web/image?' + 'model=sica.news&id=' + str(news.id) + '&field=image'
            vals = {
                'title': news.title or '',
                'date': news.date.strftime("%Y-%m-%d") if news.date else '',
                'views': news.views or 0,
                'description': news.description,
                'image_url': image
            }
            news_vals.append(vals)
        return json.dumps({'Sica News Vals': news_vals})


    @http.route('/get/sica/news', type='http', auth='none', methods=['GET'], csrf=False)
    def get_sica_news_details(self, **kw):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')

        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})
        news_vals = []
        news_ids = request.env['sica.news'].sudo().search([], order="sequence asc")
        for news in news_ids:
            image = base_url + '/web/image?' + 'model=sica.news&id=' + str(news.id) + '&field=image'
            vals = {
                'title': news.title or '',
                'date': news.date.strftime("%Y-%m-%d") if news.date else '',
                'views': news.views or 0,
                'description': news.description,
                'image_url': image
            }
            news_vals.append(vals)
        return json.dumps({'Sica News Vals': news_vals})

    @http.route('/get/new/sica/features', type='http', auth='none', methods=['GET'], csrf=False)
    def action_get_sica_features_details(self, **kw):
        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')
        event_image_default_url = request.env['ir.config_parameter'].sudo().get_param('website.event_image_link')
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})

        today = fields.Date.today()
        yesterday = today - relativedelta(days=1)
        blog_vals = []
        blog_ids = request.env['sica.features'].sudo().search([('create_date', '>=', yesterday), ('create_date', '<=', today)], order="sequence asc")
        for blog in blog_ids:
            attachments = []
            for attachment in blog.attachments_ids:
                attachment.public = True
                attachments.append(base_url + '/web/image/%s' % attachment.id)
            if not attachments:
                attachments.append(event_image_default_url)
            vals = {
                'title': blog.title or '',
                'date': blog.date.strftime("%Y-%m-%d") if blog.date else '',
                'views': blog.views or 0,
                'description': blog.description,
                'images_url': attachments,
            }
            blog_vals.append(vals)
        return json.dumps({'Sica Features Vals': blog_vals})


    @http.route('/get/sica/features', type='http', auth='none', methods=['GET'], csrf=False)
    def get_sica_features_details(self, **kw):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')
        event_image_default_url = request.env['ir.config_parameter'].sudo().get_param('website.event_image_link')
        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})
        blog_vals = []
        blog_ids = request.env['sica.features'].sudo().search([],order="sequence asc")
        for blog in blog_ids:
            attachments = []
            for attachment in blog.attachments_ids:
                attachment.public = True
                attachments.append(base_url + '/web/image/%s' % attachment.id)
            if not attachments:
                attachments.append(event_image_default_url)
            vals = {
                'title': blog.title or '',
                'date': blog.date.strftime("%Y-%m-%d") if blog.date else '',
                'views': blog.views or 0,
                'description': blog.description,
                'images_url': attachments,
            }
            blog_vals.append(vals)
        return json.dumps({'Sica Features Vals': blog_vals})
