from odoo import api, fields, models, http
from odoo.http import request
import json

class PatientController(http.Controller):

    @http.route('/<string:main_route>/<string:specific_route>/<int:sequence>', auth='public', type='http', methods=['GET'])
    def patient_consult(self, main_route, specific_route, sequence, **kwargs):
        """
        Route to consult patient information
        :param main_route:
        :param specific_route:
        :param dni:
        :param kwargs:
        :return:
        """
        route = "%s/%s" % (main_route, specific_route)
        main = request.env['ir.config_parameter'].sudo().get_param('vertical_hospital.main_route')
        specific = request.env['ir.config_parameter'].sudo().get_param('vertical_hospital.patient_route')
        config_route = "%s/%s" % (main, specific)
        if route == config_route:
            patient = request.env['hospital.patient'].sudo().search([('name', '=', sequence)])
            if patient:
                data = {
                    'seq': patient.name,
                    'name': patient.patient_name,
                    'dni': patient.dni,
                    'state': patient.state,
                }
                return json.dumps(data)
            else:
                return "Patient not Found"
        else:
            return "Connection error: Incorrect Route"