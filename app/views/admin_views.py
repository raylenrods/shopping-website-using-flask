from turtle import title
from app import app, db, bcrypt
from app.forms.forms import ContactForm, LoginForm, RegisterForm, SearchForm, ProductForm
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, LoginManager, UserMixin, login_required, logout_user, current_user
from app.model.model import Users, Contact, Products


@app.route('/admin/dashboard', methods=['get', 'post'])
@login_required
def dashboard():
    id = current_user.id
    if id == 1:
        return render_template('admin/dashboard.html')
    else:
        flash("You need to login as admin","Error")
        return redirect(url_for('login'))


@app.route('/admin/profile')
@login_required
def admin_profile():
    return "<h1>Admin Profile Page</h1>"


@app.context_processor
def base():
    products =Products.query.all()
    users=Users.query.all()
    return dict(products=products,users=users)


@app.route('/add_product', methods=['get', 'post'])
@login_required
def add_product():
    id = current_user.id
    if id == 1:
        form = ProductForm()
        if form.validate_on_submit():
            product = Products(pname=form.name.data, description=form.description.data,category=form.category.data, image=form.image.data, price=form.price.data)
            db.session.add(product)
            db.session.commit()
            flash("Added Successfully")
            return redirect(url_for('add_product'))
        return render_template('admin/add_product.html', form=form)
    else:
        flash("You need to login as admin","Error")
        return redirect(url_for('login'))


@app.route('/products/edit/<int:id>', methods=['get', 'post'])
@login_required
def edit_product(id):
    products = Products.query.get_or_404(id)
    form = ProductForm()
    if form.validate_on_submit():
        products.pname = form.name.data
        products.description = form.description.data
        products.category = form.category.data
        products.price = form.price.data
        products.image = form.image.data
        db.session.add(products)
        db.session.commit()
        return redirect(url_for('display_products', id=products.pid))

    form.name.data = products.pname
    form.description.data = products.description
    form.category.data = products.category
    form.price.data = products.price
    form.image.data = products.image
    return render_template('admin/add_product.html', form=form)


@app.route('/products/delete/<int:id>', methods=['get', 'post'])
@login_required
def delete_product(id):
    products = Products.query.get_or_404(id)
    db.session.delete(products)
    db.session.commit()
    return redirect(url_for('display_products'))


@app.route('/display_products')
@login_required
def display_products():
    products = Products.query.all()
    return render_template('admin/display_products.html', products=products)


@app.route('/display_users')
@login_required
def display_users():
    users = Users.query.all()
    return render_template('admin/display_users.html', users=users)
