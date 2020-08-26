import cocktail_blender.database.manager as db_manager
import cocktail_blender.database.settings as cocktail_db_settings
import cocktail_blender.database.models as cocktail_models

db_manager.reset_database()
db_manager.initialize_database()
session = cocktail_db_settings.Session()
tmp_drink = cocktail_models.Drink()
tmp_drink.drink_name = 'water'
tmp_drink.drink_id = 123
tmp_drink.drink_type = cocktail_models.DrinkType.Soft
session.add(tmp_drink)
session.commit()

added_drink = session.query(cocktail_models.Drink).filter_by(drink_name='water').first()

print(added_drink)

session.close()
