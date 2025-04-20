from app import create_app, db
from app.models import FoodItem
import os
import shutil

def update_menu_images():
    app = create_app()
    with app.app_context():
        # Get all menu items
        menu_items = FoodItem.query.all()
        
        # Set default image path for each category
        category_images = {
            'burgers': 'images/burger-default.jpg',
            'wraps': 'images/wrap-default.jpg',
            'extras': 'images/extras-default.jpg'
        }
        
        # Update all menu items
        for item in menu_items:
            # Set a default image path based on category
            default_image = category_images.get(item.category, 'images/default-food.jpg')
            item.image_path = default_image
        
        # Save changes
        db.session.commit()
        print("Menu images updated successfully!")

if __name__ == '__main__':
    update_menu_images() 