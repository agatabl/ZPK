from flask import request
from flask_restplus import Resource

from ..util.dto import TrailDto
from ..service.trail_service import save_new_trail, get_a_trail, get_all_trails, delete_a_trail

api = TrailDto.api
_trail = TrailDto.trail


@api.route('/')
class TrailList(Resource):
    @api.doc('list_of_trails')
    @api.marshal_list_with(_trail, envelope='data')
    def get(self):
        """List all trails"""
        return get_all_trails()

    @api.response(201, 'Trail successfully created.')
    @api.doc('create new trail')
    @api.expect(_trail)
    def post(self):
        """creates new trail"""
        data = request.json
        return save_new_trail(data=data)


@api.route('/<id>')
@api.param('trail', "Trail identyfier")
@api.response(404, 'Trail not found')
class Trail(Resource):
    @api.doc('get a trail')
    @api.marshal_with(_trail)
    def get(self, id):
        trail = get_a_trail(id)
        if not trail:
            api.abort(404)
        else:
            return trail

    @api.doc('delete trail')
    @api.response(200, 'Trail deleted')
    @api.marshal_with(_trail)
    def delete(self, id):
        # data = request.json
        return delete_a_trail(id)
