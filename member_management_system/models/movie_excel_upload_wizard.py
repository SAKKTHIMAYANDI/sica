from odoo import models, fields, api, _
import base64
from odoo.exceptions import ValidationError
import xlrd
import datetime

class MovieExcelUploadWizard(models.TransientModel):
    _name = 'movie.excel.upload.wizard'
    _description = 'Upload Movie Excel Wizard'

    excel_file = fields.Binary('Excel File', required=True)
    file_name = fields.Char('Filename')

    def action_import(self):
        if not self.excel_file:
            raise ValidationError("Please upload a valid Excel file.")

        # Load workbook
        workbook = xlrd.open_workbook(file_contents=base64.b64decode(self.excel_file))

        for sheet in workbook.sheets():
            for row in range(1, sheet.nrows):
                try:
                    sno = sheet.cell(row, 0).value
                    date_val = sheet.cell(row, 1).value
                    movie_name = sheet.cell(row, 2).value
                    dop_name = sheet.cell(row, 3).value
                    production = sheet.cell(row, 4).value if sheet.ncols > 4 else ''
                    team_member = sheet.cell(row, 5).value if sheet.ncols > 5 else ''
                    movie_link = sheet.cell(row, 6).value if sheet.ncols > 6 else ''
                    
                    # Clean and validate project_type
                    project_type = ''
                    if sheet.ncols > 7:
                        raw_project_type = sheet.cell(row, 7).value
                        if isinstance(raw_project_type, str):
                            project_type = raw_project_type.strip().lower()
                    valid_types = ['movies', 'series', 'serial', 'others']
                    if project_type not in valid_types:
                        project_type = 'movies'

                    channel_name = sheet.cell(row, 8).value if sheet.ncols > 8 else ''

                    # Date Parsing
                    if isinstance(date_val, float):
                        parsed_date = datetime.datetime(*xlrd.xldate_as_tuple(date_val, workbook.datemode)).date()
                    else:
                        try:
                            parsed_date = datetime.datetime.strptime(date_val, "%d %B %Y").date()
                        except Exception:
                            parsed_date = fields.Date.today()

                    # Create record
                    self.env['movie.list'].create({
                        'sequence': int(sno) if sno else 0,
                        'date': parsed_date,
                        'movie_name': movie_name,
                        'dop_name': dop_name,
                        'production_companies': production,
                        'team_member': team_member,
                        'movie_link': movie_link,
                        'project_type': project_type,
                        'channel_name': channel_name,
                    })

                except Exception as e:
                    raise ValidationError(f"Error in sheet '{sheet.name}' row {row + 1}: {e}")

        # Redirect to movie.list tree view
        return {
            'type': 'ir.actions.act_window',
            'name': 'Movie List',
            'res_model': 'movie.list',
            'view_mode': 'tree,form',
            'target': 'current',
        }



    # def action_import(self):
    #     if not self.excel_file:
    #         raise ValidationError("Please upload a valid Excel file.")

    #     workbook = xlrd.open_workbook(file_contents=base64.b64decode(self.excel_file))
    #     sheet = workbook.sheet_by_index(0)

    #     for row in range(1, sheet.nrows):
    #         sno = sheet.cell(row, 0).value
    #         date_val = sheet.cell(row, 1).value
    #         movie_name = sheet.cell(row, 2).value
    #         dop_name = sheet.cell(row, 3).value
    #         production = sheet.cell(row, 4).value if sheet.ncols > 4 else ''
    #         team_member = sheet.cell(row, 5).value if sheet.ncols > 5 else ''
    #         movie_link = sheet.cell(row, 6).value if sheet.ncols > 6 else ''
    #         if isinstance(date_val, float):
    #             parsed_date = datetime.datetime(*xlrd.xldate_as_tuple(date_val, workbook.datemode)).date()
    #         else:
    #             try:
    #                 parsed_date = datetime.datetime.strptime(date_val, "%d %b %Y").date()
    #             except Exception:
    #                 parsed_date = fields.Date.today()

    #         self.env['movie.list'].create({
    #             'sequence': int(sno),
    #             'date': parsed_date,
    #             'movie_name': movie_name,
    #             'dop_name': dop_name,
    #             'production_companies': production,
    #             'team_member': team_member,
    #             'movie_link': movie_link,
    #         })

    #     # Redirect to movie.list tree  
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Movie List',
    #         'res_model': 'movie.list',
    #         'view_mode': 'tree,form',
    #         'target': 'current',
    #     }