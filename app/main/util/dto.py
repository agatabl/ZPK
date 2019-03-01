from flask_restplus import Namespace, fields
""""data transfer object"""
"""responsible for carying objects between processes. W tym wypadku
odpowiedzilany za marashalowanie danych dla zapytań API"""


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user identifier'),

    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })


class AreaDto:
    api = Namespace('area', description='area related operations')
    area = api.model('area', {
        'id': fields.String(required=True, description='area id'),
        'name': fields.String(required=True, description='area name'),
        'starting_point_lat': fields.String(required=True, description='starting_point_lat'),
        'starting_point_lon': fields.String(required=True, description='starting_point_lon'),
        'radius': fields.String(required=True, description='radius of buffor')

    })


class TrailDto:
    api = Namespace('trail', description='trails related operation')
    trail = api.model('trail', {
        'id': fields.String(required=True, description='trail id'),
        'name': fields.String(required=True, description='trail name'),
        'map_id': fields.String(required=True, description="trail's map"),
        'file': fields.String(required=False, description='path to GPX? file')
    })


class MapDto:
    api = Namespace('map', description='maps related operation')
    map = api.model('map', {
        'id': fields.String(required=True, description='map id'),
        'name': fields.String(required=True, description='map name'),
        'area_id': fields.String(required=True, description='area id'),
        'map_file': fields.String(required=True, description='map file path'),
        'border_N': fields.String(required=True, description='N border limit'),
        'border_S': fields.String(required=True, description='S border limit'),
        'border_E': fields.String(required=True, description='E border limit'),
        'border_W': fields.String(required=True, description='W border limit')

    })
