from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,SubmitField,StringField,DateField,SelectField,BooleanField,IntegerField;
from wtforms.validators import DataRequired,Length,EqualTo,Email
from wtforms.widgets import TextArea

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    psw=PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField("Remember Me", default=True)
    submit=SubmitField("Login");


class RegisterForm(FlaskForm):
    name=StringField("Enter Name")
    date=DateField("Select Date of Birth")
    gender=SelectField("Gender",choices=['Male','Female','Other'])
    email = EmailField("Enter Email Address", validators=[DataRequired(), Email()])
    psw = PasswordField("Enter Password", validators=[DataRequired()])
    rpsw = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('psw')])
    mob = StringField("Enter Mobile", validators=[DataRequired(), Length(min=10, max=10)])
    submit = SubmitField("Register")


class ContactForm(FlaskForm):
    fname = StringField("Enter Name", validators=[DataRequired()])
    lname = StringField("Enter Last Name", validators=[DataRequired()])
    email = EmailField("Enter Email Address", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()],widget=TextArea())
    submit = SubmitField("Submit")



class ProductForm(FlaskForm):
    name = StringField("Enter Product Name", validators=[DataRequired()])
    description = StringField("Product Description", validators=[DataRequired()], widget=TextArea())
    category = SelectField("Category", choices=['DSLR Camera', 'Mirrorless Camera', 'Action Camera'])
    image = StringField("Enter Image Name with extension", validators=[DataRequired()])
    price = IntegerField("Enter Price", validators=[DataRequired()])
    submit = SubmitField("Add Product")


class SearchForm(FlaskForm):
    searched =StringField("Searched", validators=[DataRequired()])
    submit=SubmitField("Search");