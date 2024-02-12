# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, _, api
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    main_route = fields.Char(string="URL Route Main")
    patient_route = fields.Char(string="URL Route Patient")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['main_route'] = self.env['ir.config_parameter'].sudo().get_param('vertical_hospital.main_route')
        res['patient_route'] = self.env['ir.config_parameter'].sudo().get_param('vertical_hospital.patient_route')
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('vertical_hospital.main_route', self.main_route)
        self.env['ir.config_parameter'].sudo().set_param('vertical_hospital.patient_route', self.patient_route)