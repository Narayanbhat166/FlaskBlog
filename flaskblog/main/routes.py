from flask import render_template, request, Blueprint, send_from_directory
from flaskblog.models import Post
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(per_page=3, page=page)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title="Narayan")

@main.route('/debug')
def debug():
    raise Exception()
