from flask import render_template, request, Blueprint
from flaskblog import firebase_storage
from flaskblog.models import Post,User
from flask_login import current_user


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

    # if current_user.is_authenticated:
    #     prof_pic = firebase_storage.prof_pic(current_user.image_file)
    # else:
    #     prof_pic = None

    return render_template('home.html', posts=posts, prof_pic=firebase_storage.prof_img(current_user), firebase_storage=firebase_storage)


@main.route('/about')
def about():
    return render_template('about.html', title='About', prof_pic=firebase_storage.prof_img(current_user))


@main.route('/gallery')
def gallery():
    return render_template('gallery.html', title='Gallery', prof_pic=firebase_storage.prof_img(current_user))


@main.route('/bloggers')
def bloggers():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=60)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('bloggers.html', title='bloggers', users=users, posts=posts, prof_pic=firebase_storage.prof_img(current_user))


@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact', prof_pic=firebase_storage.prof_img(current_user))
