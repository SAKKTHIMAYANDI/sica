import base64

from odoo import http, fields
from odoo.http import request
import json
import random
import requests
import time,pytz
from datetime import datetime,timedelta,timezone,date
from dateutil.relativedelta import relativedelta


class MyMovieMyExperience(http.Controller):

    @http.route('/get/mymoviemyexperience', type='http', auth='public', methods=['GET'], csrf=False)
    def action_get_myexperience(self, **kw):
        base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url.image')

        api_key = kw.get('api_key')  # Extract the API key from the GET parameters
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"
        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})

        mmme_details = []
        mmme_vals = request.env['mymovie.myexperience'].sudo().search([('state', '=', 'approved')], order="sequence asc")
        for mmme in mmme_vals:
            image = base_url + '/web/image?' + 'model=mymovie.myexperience&id=' + str(mmme.id) + '&field=image_1920'
            base64_string = ''
            image_data = mmme.image
            if image_data:
                base64_string = base64.b64encode(image_data).decode('utf-8')
            vals = {
                'title': mmme.title or '',
                'date': mmme.date.strftime("%Y-%m-%d") if mmme.date else '',
                'views': mmme.views or 0,
                'description': mmme.description,
                'image_url': image
            }
            mmme_details.append(vals)
        return json.dumps({'My Movie My Experience': mmme_details})

    @http.route('/create/mmme_details/json', type="json", auth='none', methods=['POST'], csrf=False)
    def action_create_myexperience_json(self, args=None, **kw):
        payload = request.httprequest.data.decode()
        payload = json.loads(payload)

        api_key = payload.get('api_key')
        stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"

        if not api_key:
            return json.dumps({"error": "API key is missing"})
        if api_key != stored_api_key:
            return json.dumps({"error": "Invalid API key"})

        title = payload.get('title')
        date = payload.get('date')
        views = payload.get('views')
        description = payload.get('description')
        image = payload.get('image')

        create_works = request.env['mymovie.myexperience'].sudo().create({
            'title': title,
            'date': date,
            'views': views,
            'description': description,
            'image': image,
        })
        return json.dumps({'My Movie My Experience': 'My Movie My Experience is created', 'ID': create_works.id})
