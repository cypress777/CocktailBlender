import cocktail_blender.database as cbdb
import cocktail_blender.database_settings as cocktail_db_settings
import cocktail_blender.database_updator as cocktail_db_updator
import cocktail_blender.models as cocktail_models


if __name__ == '__main__':    
    cbdb.reset_database()
    cbdb.initialize_database()
    cocktail_db_updator.update_from_file('tests/test.json')

    session = cocktail_db_settings.Session()
    added_drink = session.query(cocktail_models.Drink).filter_by(drink_name='chambord').first()
    print(added_drink.drink_name, added_drink.drink_type)
    session.close()
