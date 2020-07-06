import cocktail_blender.database as cbdb
from cocktail_blender.database_settings import Session
from cocktail_blender.database_updator import update_from_file
from cocktail_blender.models import Drink


if __name__ == '__main__':    
    cbdb.reset_database()
    cbdb.initialize_database()
    update_from_file('tests/test.json')

    session = Session()
    added_drink = session.query(Drink).filter_by(drink_name='chambord').first()
    print(added_drink.drink_name, added_drink.drink_type)
    session.close()
