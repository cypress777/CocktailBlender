import cocktail_blender.database as cbdb
from cocktail_blender.database_settings import Session
from cocktail_blender.models import Drink

cbdb.reset_database()
cbdb.initialize_database()
session = Session()
tmp_drink = Drink()
tmp_drink.drink_name = 'water'
tmp_drink.drink_id = 123
tmp_drink.drink_type = 'Soft'
session.add(tmp_drink)
session.commit()

added_drink = session.query(Drink).filter_by(drink_name='water').first()

print(added_drink.drink_name)

session.close()
