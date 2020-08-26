import cocktail_blender.database.manager as db_manager
import cocktail_blender.database.settings as cocktail_db_settings
import cocktail_blender.database.updator as cocktail_db_updator
import cocktail_blender.database.models as cocktail_models


if __name__ == '__main__':    
    db_manager.reset_database()
    db_manager.initialize_database()
    cocktail_db_updator.update_from_file('tests/test.json')

    session = cocktail_db_settings.Session()
    added_drink = session.query(cocktail_models.Drink).filter_by(drink_name='chambord').first()
    print(added_drink.drink_name, added_drink.drink_type)
    session.close()
