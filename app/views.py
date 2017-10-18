from app import app

@app.route('/')
@app.route('/index')

@app.route("/")
def hello():
    return "Hello World!"