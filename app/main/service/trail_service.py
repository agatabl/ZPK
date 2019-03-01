import uuid
from app.main import db
from app.main.model.trail import Trail


def save_new_trail(data):
    trail = Trail.query.filter_by(name=data['name']).first()
    if not trail:
        new_trail = Trail(
            id=data['id'],
            name=data['name'],
            map_id=data['map_id'],
            file=data['file']
        )
        save_changes(new_trail)
        response_object = {
            'status': 'success',
            'message': 'Trail successfully created'

        }
        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'Trail with this name already exists'
        }
        return response_object, 409


def delete_a_trail(id):
    trail = Trail.query.filter_by(id=id).first()
    if not trail:
        response_object = {
            'status': 'fail',
            'message': f'Trail {id} does not exist'
        }
        return response_object, 404
    else:
        db.session.delete(trail)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Trail deleted'
        }
        return response_object, 200


def get_all_trails():
    return Trail.query.all()


def get_a_trail(id):
    return Trail.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
