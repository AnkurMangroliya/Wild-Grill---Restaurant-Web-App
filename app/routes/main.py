from flask import Blueprint, render_template, redirect, url_for, flash, session, jsonify, request
from app.models import FoodItem, CartItem, Order
from app.forms import CartItemForm, OrderForm
from app import db
import json

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    menu_items = FoodItem.query.order_by(FoodItem.category, FoodItem.name).all()
    categories = {}
    for item in menu_items:
        if item.category not in categories:
            categories[item.category] = []
        categories[item.category].append(item)
    form = CartItemForm()
    return render_template('home.html', categories=categories, form=form)

@bp.route('/add-to-cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    form = CartItemForm()
    if form.validate_on_submit():
        food_item = FoodItem.query.get_or_404(item_id)
        
        # Initialize cart in session if it doesn't exist
        if 'cart' not in session:
            session['cart'] = []
        
        # Add item to cart
        cart_item = {
            'id': food_item.id,
            'name': food_item.name,
            'price': food_item.price,
            'quantity': form.quantity.data,
            'special_instructions': form.special_instructions.data
        }
        
        session['cart'].append(cart_item)
        session.modified = True
        
        flash(f'{food_item.name} added to cart!', 'success')
        return redirect(url_for('main.view_cart'))
    
    return redirect(url_for('main.home'))

@bp.route('/cart')
def view_cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    form = OrderForm()
    return render_template('cart.html', cart_items=cart_items, total=total, form=form)

@bp.route('/remove-from-cart/<int:index>')
def remove_from_cart(index):
    cart = session.get('cart', [])
    if 0 <= index < len(cart):
        removed_item = cart.pop(index)
        session['cart'] = cart
        session.modified = True
        flash(f'{removed_item["name"]} removed from cart', 'success')
    return redirect(url_for('main.view_cart'))

@bp.route('/place-order', methods=['POST'])
def place_order():
    form = OrderForm()
    if form.validate_on_submit():
        cart_items = session.get('cart', [])
        if not cart_items:
            flash('Your cart is empty!', 'error')
            return redirect(url_for('main.view_cart'))
        
        total_price = sum(item['price'] * item['quantity'] for item in cart_items)
        
        order = Order(
            items=cart_items,
            total_price=total_price,
            status='pending'
        )
        
        db.session.add(order)
        db.session.commit()
        
        # Clear the cart
        session['cart'] = []
        session.modified = True
        
        flash('Order placed successfully!', 'success')
        return redirect(url_for('main.order_confirmation', order_id=order.id))
    
    return redirect(url_for('main.view_cart'))

@bp.route('/order-confirmation/<int:order_id>')
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_confirmation.html', order=order) 