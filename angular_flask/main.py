import os
from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

app = Flask(__name__)

app.url_map.strict_slashes = False

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/mission')
@app.route('/programs')
@app.route('/people')
def basic_pages(**kwargs):
        return make_response(open(os.path.join(app.root_path, 'templates', 
                                               'index.html')).read())

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                               'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'), 404

def runserver():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    runserver()
