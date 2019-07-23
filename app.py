from flask import Flask, redirect, request, url_for
from flask.templating import render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://home/nehe/Documents/vishakha/flask_blog/flask_blog.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/flask_blog.db"

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:////home/jisoo/totalAirQREST/totalAirRunDB/airQuality.db
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:////home/nehe/Documents/vishakha/flask_blog/flask_blog.db


# db = SQLAlchemy(app)

# class Blogpost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     subtitle = db.Column(db.String(50))
#     author = db.Column(db.String(20))
#     date_posted = db.Column(db.DateTime)
#     content = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug = True)