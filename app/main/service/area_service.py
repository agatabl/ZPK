# TODO:  zrobić, żeby tylko admin mógł dodawać mapy
# albo  żeby mapy musiały czekać na zatwierdzenie admina, zamin się pojawią w serwisie
from app.main import db
from app.main.model.area import Area


def save_new_area(data):
    area = Area.query.filter_by(name=data['name']).first()
    if not area:
        new_area = Area(
            id=data['id'],
            name=data['name'],
            starting_point_lat=data['starting_point_lat'],
            starting_point_lon=data['starting_point_lon'],
            radius=data['radius']
        )

        save_changes(new_area)
        response_object = {
            'status': 'succes',
            'message': 'Pomyslnie dodano arenę.'
        }

        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'Arena o tej nazwie już istnieje.',
        }
        return response_object, 409


def delete_a_area(id):
    area = Area.query.filter_by(id=id).first()
    if not area:
        response_object = {
            'status': 'fail',
            'message': f'Area {id} does not exist'
        }
        return response_object, 404
    else:
        db.session.delete(area)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Trail deleted'
        }
        return response_object, 200


def get_all_areas():
    return Area.query.all()


def get_a_area(name):
    return Area.query.filter_by(name=name).first()

# # ?
#
#
# def delete_trail(area):
#     db.session.delete(area)
#     db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
