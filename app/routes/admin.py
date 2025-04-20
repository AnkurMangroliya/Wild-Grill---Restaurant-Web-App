from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
import os
from app.forms import FoodItemForm
from app.models import FoodItem
from app import db
from PIL import Image

bp = Blueprint('admin', __name__)

def save_image(image_file):
    if not image_file:
        return None
    
    # Ensure upload directory exists
    upload_dir = os.path.join(current_app.root_path, 'static', 'uploads')
    os.makedirs(upload_dir, exist_ok=True)
    
    filename = secure_filename(image_file.filename)
    # Create a unique filename to prevent overwrites
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(os.path.join(upload_dir, filename)):
        filename = f"{base}_{counter}{ext}"
        counter += 1
    
    # Save the original file
    filepath = os.path.join(upload_dir, filename)
    image_file.save(filepath)
    
    # Open and resize the image
    with Image.open(filepath) as img:
        # Resize image to maintain aspect ratio with max dimensions
        max_size = (800, 600)
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        # Save the resized image
        img.save(filepath, quality=85, optimize=True)
    
    # Return the relative path for database storage
    return os.path.join('uploads', filename)

@bp.route('/add', methods=['GET', 'POST'])
def add_item():
    form = FoodItemForm()
    if form.validate_on_submit():
        # Handle image upload
        image_path = save_image(form.image.data)
        
        # Create new food item
        food_item = FoodItem(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            category=form.category.data,
            image_path=image_path
        )
        
        db.session.add(food_item)
        db.session.commit()
        
        flash('Menu item added successfully!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('admin/add_item.html', form=form) 