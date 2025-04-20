from app import create_app, db
from app.models import FoodItem
import os

def fix_image_paths():
    app = create_app()
    with app.app_context():
        # Get all food items
        food_items = FoodItem.query.all()
        
        # Check and fix each item's image path
        for item in food_items:
            if item.image_path:
                # Remove any leading 'static/' from the path
                if item.image_path.startswith('static/'):
                    item.image_path = item.image_path[7:]  # Remove 'static/'
                
                # Check if file exists
                full_path = os.path.join(app.root_path, 'static', item.image_path)
                if not os.path.exists(full_path):
                    print(f"Warning: Image not found for {item.name}: {full_path}")
                else:
                    print(f"Image path verified for {item.name}: {item.image_path}")
        
        # Save changes
        db.session.commit()
        print("Image paths updated successfully!")

if __name__ == '__main__':
    fix_image_paths() 