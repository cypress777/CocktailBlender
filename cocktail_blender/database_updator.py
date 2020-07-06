import json

from cocktail_blender.database_settings import Session
from cocktail_blender.models import Drink


def convert_json_to_object(json_object):
    drink = Drink()
    if 'drink_name' in json_object: drink.drink_name = json_object['drink_name']
    if 'drink_type' in json_object: drink.drink_type = json_object['drink_type']
    if 'water_solubility' in json_object: drink.water_solubility = json_object['water_solubility']
    if 'density' in json_object : drink.density = json_object['density']
    if 'color' in json_object: drink.color = json_object['color']
    return drink

def update_existed_row(query, new_object):
    keys = new_object.__dict__.keys()
    for key in keys:
        if key == 'drink_id' or key == '_sa_instance_state': continue
        query.update({key: new_object.__dict__[key]})

def update_from_file(filename):
    session = Session()
    with open(filename) as f:
        data = json.load(f)
        for new_info in data['drinks']:
            if 'drink_name' in new_info['drink']:
                drink = convert_json_to_object(new_info['drink'])

                query = session.query(Drink).filter_by(drink_name=drink.drink_name)
                found = query.one_or_none()
                if found is None:
                    session.add(drink)
                elif new_info['operator'] == 'mod':
                    update_existed_row(query, drink)
                session.commit()
        session.close()
