import re
from turtle import title
from app import app,db,bcrypt
from sqlalchemy import insert,delete
from app.forms.forms import ContactForm, LoginForm,RegisterForm,SearchForm,ProductForm
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,LoginManager,UserMixin,login_required,logout_user,current_user
from app.model.model import Users,Contact,Products,Cart

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('public/404_error.html'), 404


@app.route('/')
def home():
    print(app.config['ENV'])
    return render_template('public/index.html')

@app.route('/index')
def index():
    print(app.config['ENV'])
    return render_template('public/index.html')


@app.route('/contact', methods=['get', 'post'])
def contact():
    form=ContactForm()
    if form.validate_on_submit():
        print("test")
        contact = Contact(fname=form.fname.data, lname=form.lname.data, email=form.email.data, subject=form.subject.data)
        db.session.add(contact)
        db.session.commit()
        form.fname.data=""
        form.lname.data = ""
        form.email.data = ""
        form.subject.data = ""
        flash("Submitted Successfully")
    return render_template('public/contact.html', form=form)

@app.route('/about')
def about():
    return render_template('public/about.html')


@app.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.psw.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
    return render_template('public/login.html', form=form)


@app.route('/logout', methods=['get', 'post'])
@login_required
def logout():
    logout_user()
    form=LoginForm()
    flash("Logged out successfully","Success")
    return render_template('public/login.html',form=form)


@app.route('/register', methods=['get', 'post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.psw.data).decode('utf-8')
        user= Users(name=form.name.data,dob=form.date.data,gender=form.gender.data,email=form.email.data, password=pw_hash,mobile=form.mob.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('public/sign_up.html',form=form)


@app.route('/products')
def products():
    return render_template('public/products.html')


@app.route('/product_gallery/<cat>')
def product_gallery(cat):
    products = Products.query.filter_by(category=cat)
    return render_template('public/product_gallery.html', products=products,heading=cat)



@app.route('/product_specs/<int:id>')
def product_specs(id):
    products = Products.query.get_or_404(id)
    return render_template('public/product_specs.html', products=products)



@app.context_processor 
def base():
    form = SearchForm()
    if current_user.is_authenticated:
        poster = current_user.id
        results = db.session.query(Users, Cart, Products).select_from(Users).join(Cart).join(Products).filter(Users.id == poster).all()
        return dict(form=form,results=results)
    return dict(form=form)


@app.route('/search', methods=['post'])
def search():
    form=SearchForm()
    products=Products.query
    if form.validate_on_submit():
        searched=form.searched.data
        products=products.filter(Products.pname.like('%'+ searched +'%'))
        products=products.order_by(Products.pname).all()
        return render_template('public/search.html',form=form,searched=searched,products=products)


@app.route('/select_product/<int:id>', methods=['GET', 'POST'])
@login_required
def select_product(id):
    form=ProductForm()
    poster=current_user.id
    products=Products.query.all()
    cs=(insert(Cart).values(product_id=id,user_id=poster))
    db.session.execute(cs)
    db.session.commit()
    flash("Product added to cart", "Success")
    return render_template('public/cart.html', products=products, form=form)


@app.route('/cart')
@login_required
def cart():
    total=0
    poster = current_user.id
    results = db.session.query(Users, Cart, Products).select_from(Users).join(Cart).join(Products).filter(Users.id == poster).all()
    for row in results:
        total=total+row[3].price
    return render_template('public/cart.html',results=results,total=total)


@app.route('/remove_product/<int:id>')
@login_required
def remove_product(id):
    dl=delete(Cart).where(Cart.c.product_id==id)
    print(dl)
    db.session.execute(dl)
    db.session.commit()
    flash("Product removed from cart", "Success")
    return redirect(url_for('cart'))



            
            
            
            
        
