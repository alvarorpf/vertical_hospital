from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError
import re

class HospitalTreatment(models.Model):
    _name = 'hospital.treatment'
    _description = 'Treatment'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    doctor = fields.Char('Doctor')

    def name_get(self):
        result = []
        for rec in self:
            name = "[%s] %s" % (rec.code, rec.name)
            result.append((rec.id, name))
        return result

    @api.constrains('code')
    def check_code(self):
        for rec in self:
            if re.search(r'026', rec.code):
                raise ValidationError("The value '026' cannot be entered in the code field.")

