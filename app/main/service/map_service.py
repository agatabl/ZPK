# TODO:  zrobić, żeby tylko admin mógł dodawać mapy
# albo  żeby mapy musiały czekać na zatwierdzenie admina, zamin się pojawią w serwisie

# TODO: dodac delete_map dla admina
import uuid
from app.main import db
from app.main.model.map import Map


def save_new_map(data):
    map = Map.query.filter_by(name=data['name']).first()
    if not map:
        new_map = Map(
            id=data['id'],
            name=data['name'],
            area_id=data['area_id'],
            map_file=data['map_file'],
            border_N=data['border_N'],
            border_S=data['border_S'],
            border_E=data['border_E'],
            border_W=data['border_W']

        )

        save_changes(new_map)
        response_object = {
            'status': 'succes',
            'message': 'Pomyslnie dodano mapę.'
        }

        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'Mapa o tej nazwie już istnieje.',
        }
        return response_object, 409


def get_all_maps():
    return Map.query.all()


def get_a_map(name):
    return Map.query.filter_by(name=name).first()


# def delete_map(map):
#     db.session.delete(map)
#     db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
