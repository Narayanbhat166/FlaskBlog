from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint,jsonify,current_app)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
from flaskblog.users.utils import save_picture
from PIL import Image
import os,secrets


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash(f'Your post has been submitted')
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Create Post', form=form, legend='Create pos')


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        flash('Your post has been updated successfully!', 'info')
        db.session.commit()
        return redirect(url_for('posts.post', post_id=post.id))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post', post=post)


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Your post has been Deleted!', 'info')
    return redirect(url_for('main.home'))

@posts.route('/upload',methods=['POST'])
@login_required
def save_image():
    image = request.files['file']
    random_hex = secrets.token_hex(8)
    fileName = image.filename
    _, f_ext = os.path.splitext(fileName)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/post', picture_fn)
    location = url_for('static',filename='post/'+picture_fn,_external = True)

    #Resize
    ratio = 0.7
    i = Image.open(image)
    image_size = i.size

    output_size = (768, 432)
    if image_size > output_size:
        i = i.resize(output_size,Image.ANTIALIAS)
        print("Large")
    else:
        i = i.thumbnail(image_size,Image.ANTIALIAS)
    
    i.save(picture_path)

    if image:
        location = {'location':location}
        return jsonify(location)
    else:
        return 'error'
        
