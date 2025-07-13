from flask import Flask
from Blueprints import BP_review, BP_home, BP_place, BP_list_of_reviews, BP_all_places
from flask_wtf.csrf import CSRFProtect
from db_models.db_session import global_init
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_folder = os.path.join(basedir, 'db')
os.makedirs(db_folder, exist_ok=True)

db_path = os.path.join(db_folder, 'database.sqlite')

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Сверхсекретный ключ, который никто и никогда не угадает'
csrf.init_app(app)


if __name__ == "__main__":
    global_init(db_path)
    app.register_blueprint(BP_review.blueprint_review)
    app.register_blueprint(BP_home.blueprint_home)
    app.register_blueprint(BP_place.blueprint)
    app.register_blueprint(BP_list_of_reviews.blueprint)
    app.register_blueprint(BP_all_places.blueprint)
    app.run()
