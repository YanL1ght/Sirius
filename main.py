from flask import Flask, render_template
from BP_review import blueprint
from flask_wtf.csrf import CSRFProtect
from db_models.db_session import global_init

csrf = CSRFProtect()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Сверхсекретный ключ, который никто и никогда не угадает'
csrf.init_app(app)


@app.route('/', methods=["POST", 'GET'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    global_init('db/database.sqlite')
    app.register_blueprint(blueprint)
    app.run(debug=True)
