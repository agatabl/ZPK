from flask import request
from flask_restplus import Resource

from ..util.dto import MapDto
from ..service.map_service import save_new_map, get_a_map, get_all_maps

api = MapDto.api
_map = MapDto.map


@api.route('/')
class MapList(Resource):
    @api.doc('list_of_maps')
    @api.marshal_list_with(_map, envelope='data')
    def get(self):
        """List all maps"""
        return get_all_maps()

    @api.response(201, 'Map successfully created.')
    @api.doc('create a new map')
    @api.expect(_map)
    def post(self):
        """Creates a new Map """
        data = request.json
        return save_new_map(data=data)


@api.route('/<id>')
@api.param('map', 'The map identifier')
@api.response(404, 'Map nor found.')
class Map(Resource):
    @api.doc('get a map')
    @api.marshal_with(_map)
    def get(self, id):
        map = get_a_map(id)
        if not map:
            api.abort(404)
        else:
            return map
