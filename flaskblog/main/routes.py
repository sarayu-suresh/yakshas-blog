from flask import render_template, request, Blueprint
from flaskblog.models import Post,User


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/gallery')
def gallery():
    return render_template('gallery.html', title='Gallery')

@main.route('/bloggers')
def bloggers():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=60)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('bloggers.html', title='bloggers', users=users, posts=posts)

@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
