from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
    return "<h1>Home page</h1>"

@app.route('/hello')
def Hello():
    return "<h1>Hello</h1>"

@app.route('/hello/<string:name>')
def Hi(name):
    return ("<h1>Hi %s!! </h1>" % name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0' ,port=80)