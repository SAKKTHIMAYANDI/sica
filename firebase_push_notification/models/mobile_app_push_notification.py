# -*- coding: utf-8 -*-
##############################################################################
#                                                                            #
#    Odoo                                                                    #
#    Copyright (C) 2023-2024 Feddad Imad (feddad.imad@gmail.com)             #
#                                                                            #
##############################################################################


from odoo import models, fields, api, _
import requests

from odoo.exceptions import UserError, ValidationError

import firebase_admin
from firebase_admin import credentials, messaging
import os
import logging
_logger = logging.getLogger(__name__)



class MobileAppPushNotification(models.Model):
    _name = 'mobile.app.push.notification'
    _description = 'Push Notification'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _order = 'id desc'

    STATE_SELECTION = [
        ('draft', 'Draft'),
        ('done', 'Sent'),
        ('Planned', 'Planned'),
        ('cancel', 'Cancel'),
        ('error', 'Error'),
    ]
    # cred = credentials.Certificate("/opt/odoo15/SICAWeb/firebase_push_notification/data/serviceAccountKey.json")

    # firebase_admin.initialize_app(cred)

    name = fields.Char('Title', tracking=True)
    body = fields.Text('Message', tracking=True)
    send_notification_to = fields.Selection([('to_all','All Partners'),('to_specefic','To a partner')], string='Send To', default='to_all', tracking=True)

    # log_history = fields.One2many('push.notification.log.history', 'notification_id', 'History' )
    log_history = fields.One2many('push.notification.log.partner','notification_id', string="Logs")

    partner_ids = fields.Many2one('res.partner', string="User")
    state = fields.Selection(STATE_SELECTION, 'Status', readonly=True, default='draft', tracking=True)


    def send_notification(self):
        tokens = []
        message = messaging.Message(
            data=None,
            notification=messaging.Notification(
                title= self.name or '',
                body= self.body or ''
            ),
            token=self.partner_ids.token,
        )
        response = messaging.send(message)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", response)
        if response:
            self.env['push.notification.log.history'].sudo().create({
                                                                  'notification_id': self.id,
                                                                  'date_send' : fields.Datetime.now(),
                                                                  'notification_state': 'success',
                                                                })
            self.write({'state': 'done'})
            
class PushNotificationLogHistory(models.Model):
    _name = 'push.notification.log.history'
    _description = 'Push Notification'


    notification_id = fields.Many2one('mobile.app.push.notification')
    date_send = fields.Datetime("Send Date")
    notification_state = fields.Selection([('success','Succès'),('failed','Échoué')], string="State")

    




