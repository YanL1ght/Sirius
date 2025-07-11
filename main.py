from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/home', methods=["POST", 'GET'])
@app.route('/', methods=["POST", 'GET'])
def index():
    if request.method == "POST":
        print(request.form.keys())
        return redirect('/home')
    elif request.method == 'GET':
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
