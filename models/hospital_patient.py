from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError
import re

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in', 'In'),
        ('out','Out')], default='draft', string='State', tracking=True,)
    name = fields.Char(string='Name', default='New', required=True)
    patient_name = fields.Char(string='Patient Name and Last Name')
    dni = fields.Char(string='DNI', tracking=True, required=True)
    treatment_id = fields.Many2one('hospital.treatment', string='Treatment')

    def default_get(self, fields_list):
        """
        :param fields_list:
        :return:
        """
        defaults = super().default_get(fields_list)
        if 'name' in defaults:
            defaults['name'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return defaults

    @api.constrains('dni')
    def _check_dni(self):
        """
        Validation if DNI has only numbers
        :return:
        """
        for rec in self:
            if rec.dni:
                if not re.match(r'^[0-9]+$', rec.dni):
                    raise ValidationError("Only numbers are allowed in this field.")
