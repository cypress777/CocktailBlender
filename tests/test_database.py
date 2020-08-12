import cocktail_blender.database as cbdb
import cocktail_blender.database_settings as cocktail_db_settings
import cocktail_blender.models as cocktail_models

cbdb.reset_database()
cbdb.initialize_database()
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
