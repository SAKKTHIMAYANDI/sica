from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MemberJobProvider(models.Model):
    _name = 'member.job.provider'
    _inherit = ["mail.thread", "mail.activity.mixin", "format.address.mixin", "avatar.mixin"]

    _description = 'Member Job Provider'

    name = fields.Char(string='Reference', default='/', readonly=True)
    member_id = fields.Many2one('res.member')
    mobile_number = fields.Char()
    member_name = fields.Char()
    membership_no = fields.Char()
    designation = fields.Char()
    experience = fields.Char()
    skill = fields.Text()
    medium = fields.Many2many('member.medium')
    portifolio_link = fields.Char()
    project_requirement = fields.Many2many('job.title')
    note = fields.Text()
    profile_pic = fields.Binary()
    state = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], default='active')
    active = fields.Boolean(default='True')
    date = fields.Date()
    available_start_date = fields.Date()
    available_end_date = fields.Date()
    required_from = fields.Date()
    required_till = fields.Date()
    post_required_id = fields.Many2one('job.title')
    medium_id = fields.Many2one('member.medium')
    grade = fields.Char()
    skill_ids = fields.Many2many('member.skill')
    # description = fields.Char()
    # grade = fields.Selection([
    #     ("junior", "Junior"),
    #     ("staff", "Staff"),
    #     ("life", "Life"),
    #     ("active", "Active"),
    #     ("associate", "Associate"),
    # ], string="Grade")


    def button_inactive(self):
        for rec in self:
            rec.state = 'inactive'
    def button_active(self):
        for rec in self:
            rec.state = 'active'

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('/'):
            vals['name'] = self.env['ir.sequence'].next_by_code('job.provider') or _('/')
        return super(MemberJobProvider, self).create(vals)

    def action_find_job_seeker(self):
        for rec in self:
            job_seeker_ids = []
            if rec.required_till < fields.Date.today():
                raise UserError(_('Post already expired'))
            filter_by_date = self.env['member.job.seeker'].search([('till_date', '<=', rec.required_till)])
            for job_seeker in filter_by_date:
                if any(skill.id in rec.skill_ids.ids for skill in job_seeker.skill_ids):
                    job_seeker_ids.append(job_seeker.id)
            for job_seeker in filter_by_date:
                if rec.medium_id.id == job_seeker.medium_id.id:
                    job_seeker_ids.append(job_seeker.id)
            for job_seeker in filter_by_date:
                if rec.post_required_id.id == job_seeker.post_applying_id.id:
                    job_seeker_ids.append(job_seeker.id)

            return {
                'type': 'ir.actions.act_window',
                'name': _('Job Seeker'),
                'view_mode': 'tree,form',
                'res_model': 'member.job.seeker',
                'domain': [('id', 'in', job_seeker_ids)],
            }

