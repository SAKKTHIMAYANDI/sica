from odoo import api,models,fields
import base64
import tempfile
import xlrd
from datetime import datetime

class MyMovieList(models.Model):
    _name = 'movie.list'
    _description = 'My Movie list'
    _rec_name = 'movie_name'

    movie_name = fields.Char(string="Movie Name")
    project_type = fields.Selection([
        ("movies", "Movies"),("series", "Series"),
        ("serial", "Serial"),("others", "Others Etc.,"),
    ], default="movies", copy=False, string="Project Type")
    date = fields.Date(string="Date")
    production_companies = fields.Char(string="Production House")
    dop_name = fields.Char(string="DOP Name")
    team_member = fields.Char(string="Team Members")
    title = fields.Char(string="Title")
    channel_name = fields.Char(string="Channel Name")
    sequence = fields.Integer(string="Sequence")
    movie_link = fields.Char(string="Movie Link", help="Enter the URL or link to the movie resource (e.g., YouTube, website, etc.)")

    image = fields.Binary(string="Status")
    image_note = fields.Char(default='16:6 or 1:1')
    state = fields.Selection([
        ("on_going", "On-Going"),
        ("completed", "Completed"),
    ], default="on_going", copy=False, string="Status")

    # def action_approve(self):
    #     self.write({
    #         'state': 'completed',
    #     })