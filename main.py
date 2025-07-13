from flask import Flask
from Blueprints import BP_review, BP_home, BP_place, BP_list_of_reviews, BP_all_places
from flask_wtf.csrf import CSRFProtect
from db_models.db_session import global_init

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Сверхсекретный ключ, который никто и никогда не угадает'
csrf.init_app(app)


if __name__ == "__main__":
    global_init('db/database.sqlite')
    app.register_blueprint(BP_review.blueprint_review)
    app.register_blueprint(BP_home.blueprint_home)
    app.register_blueprint(BP_place.blueprint)
    app.register_blueprint(BP_list_of_reviews.blueprint)
    app.register_blueprint(BP_all_places.blueprint)
    app.run(debug=True)
