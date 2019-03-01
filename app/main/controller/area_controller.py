from flask import request
from flask_restplus import Resource

from ..util.dto import AreaDto
from ..service.area_service import save_new_area, get_a_area, get_all_areas, delete_a_area

api = AreaDto.api
_area = AreaDto.area


@api.route('/')
class AreaList(Resource):
    @api.doc('list_of_areas')
    @api.marshal_list_with(_area, envelope='data')
    def get(self):
        """List all areas"""
        return get_all_areas()

    @api.response(201, 'Area successfully created.')
    @api.doc('create a new area')
    @api.expect(_area)
    def post(self):
        """Creates a new Area """
        data = request.json
        return save_new_area(data=data)


@api.route('/<id>')
@api.param('area', 'The area identifier')
@api.response(404, 'Area nor found.')
class Area(Resource):
    @api.doc('get a area')
    @api.marshal_with(_area)
    def get(self, id):
        area = get_a_area(id)
        if not area:
            api.abort(404)
        else:
            return area

    @api.doc('delete area')
    @api.marshal_with(_area)
    def delete(self, id):
        # data = request.json
        return delete_a_area(id)
