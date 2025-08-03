from odoo import http, fields
from odoo.http import request
import json
import random
import requests
import datetime
from datetime import datetime
import razorpay


class JobList(http.Controller):

    @http.route('/api/job_list/', type='json', auth='none', methods=['GET'], csrf=False)
    def active_job_list(self, **kw):
        try:
            api_key = kw.get('api_key')
            print(11111111111111111111111111111111111111111111111)
            print(api_key)
            stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"

            if api_key != stored_api_key:
                return {
                    "status": 403,
                    "message": "Invalid API Key"
                }

            records = request.env['member.job.provider'].sudo().search([('state', '=', 'active')])
            result = []
            for rec in records:
                result.append({
                    "id": rec.id,
                    "member_name": rec.member_name,
                    "mobile_number": rec.mobile_number,
                    "designation": rec.designation,
                    "experience": rec.experience,
                    "skills": [skill.name for skill in rec.skill_ids],
                    "project_requirements": [proj.name for proj in rec.project_requirement],
                    "available_start_date": rec.available_start_date.strftime('%Y-%m-%d') if rec.available_start_date else None,
                    "available_end_date": rec.available_end_date.strftime('%Y-%m-%d') if rec.available_end_date else None,
                    "state": rec.state,
                })

            return {
                "status": 200,
                "data": result
            }

        except Exception as e:
            return {
                "status": 500,
                "message": "An error occurred while fetching job list",
                "error": str(e)
            }
        

    @http.route('/api/description/', type='json', auth='none', methods=['POST'], csrf=False)
    def active_description(self, **kw):
        try:
            api_key = kw.get('api_key')
            print(11111111111111111111111111111111111111111111111)
            print(api_key)
            stored_api_key = "8f4f506e4b4022e154ac3651f9ee006e9b751261"

            if api_key != stored_api_key:
                return {
                    "status": 403,
                    "message": "Invalid API Key"
                }

            records = request.env['member.job.provider'].sudo().search([('state', '=', 'active')])
            result = []
            for rec in records:
                result.append({
                    "id": rec.id,
                    "description": rec.note,
                    # "mobile_number": rec.mobile_number,
                    # "designation": rec.designation,
                    # "experience": rec.experience,
                    # "skills": [skill.name for skill in rec.skill_ids],
                    # "project_requirements": [proj.name for proj in rec.project_requirement],
                    # "available_start_date": rec.available_start_date.strftime('%Y-%m-%d') if rec.available_start_date else None,
                    # "available_end_date": rec.available_end_date.strftime('%Y-%m-%d') if rec.available_end_date else None,
                    # "state": rec.state,
                })

            return {
                "status": 200,
                "data": result
            }

        except Exception as e:
            return {
                "status": 500,
                "message": "An error occurred while fetching job list",
                "error": str(e)
            }