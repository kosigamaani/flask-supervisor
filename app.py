from flask import Flask, make_response, jsonify, render_template

app = Flask(__name__)

data = {
    "user_info": 9898,
    "app_info": "Flask Application with Gunicorn"
}


@app.route("/user-info", methods=['GET'])
def get_user_info():
    return make_response(jsonify(data), 200)


@app.route("/solar-system", methods=['GET'])
def get_html():
    return render_template("hello-world.html")
