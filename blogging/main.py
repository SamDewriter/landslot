from flask import Blueprint, flash, render_template, request, abort
from flask_login import login_required, current_user
from . import db
from .models import Blog
from .forms import PostForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    blogs = Blog.query.all()
    css = "static/css/index.css"
    return render_template('index.html', blogs=blogs, css=css)

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        
        blog = Blog(title=form.title.data, 
                    content=form.content.data, 
                    image_url=form.image_url.data, 
                    author=current_user.id)
          
        db.session.add(blog)
        db.session.commit()
    
        flash('Blog post created', 'success')
    
    posts = Blog.query.filter_by(author=current_user.id).all()
    name = f"{current_user.first_name} {current_user.last_name}"
    return render_template('profile.html', name=name, form=form, posts=posts)

@main.route('/post/<int:id>')
def specific_post(id):
    path = f"/static/css/index.css"
    blogs = Blog.query.all()
    post = Blog.query.filter(Blog.id == id).one_or_none()
    title = post.title
    if post is None:
            abort(404)
    else:
        return render_template('post.html', post=post, path=path, title=title, blogs=blogs)

# def post():
#     form = PostForm()
#     if form.validate_on_submit():
#         blog = Blog(title=form.title.data, 
#                     content=form.content.data, 
#                     image_url=form.image_url.data, 
#                     author=current_user)
#         db.session.add(blog)
#         db.session.commit()
#     return render_template('profile.html', form=form)


# @app.route('/plants/<int:plant_id>', methods=['GET'])
#     def get_specific_plant(plant_id):
#         plant = Plant.query.filter(Plant.id == plant_id).one_or_none()
        
#         if plant is None:
#             abort(404)
#         else:
#             return jsonify({
#             'success': True,
#             'plant': plant.format()
#             })