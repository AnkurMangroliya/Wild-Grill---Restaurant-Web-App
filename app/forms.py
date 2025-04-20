from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, FloatField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class FoodItemForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    description = TextAreaField('Description', validators=[
        DataRequired(),
        Length(min=10, message='Description must be at least 10 characters')
    ])
    price = FloatField('Price', validators=[
        DataRequired(),
        NumberRange(min=0.01, message='Price must be greater than 0')
    ])
    category = SelectField('Category', choices=[
        ('burgers', 'Burgers'),
        ('wraps', 'Wraps'),
        ('extras', 'Extras')
    ], validators=[DataRequired()])
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    submit = SubmitField('Add Item')

class CartItemForm(FlaskForm):
    quantity = IntegerField('Quantity', default=1, validators=[
        DataRequired(),
        NumberRange(min=1, max=10, message='Quantity must be between 1 and 10')
    ])
    special_instructions = TextAreaField('Special Instructions')
    submit = SubmitField('Add to Cart')

class OrderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = TextAreaField('Delivery Address', validators=[DataRequired()])
    special_instructions = TextAreaField('Special Instructions')
    submit = SubmitField('Place Order') 