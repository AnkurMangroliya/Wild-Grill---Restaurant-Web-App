from app import create_app, db
from app.models import FoodItem
import os
import shutil
from PIL import Image

def set_burger_image():
    app = create_app()
    with app.app_context():
        # Source image path
        source_image = 'burger-screenshot.jpg'
        
        # Ensure uploads directory exists and create it if it doesn't
        upload_dir = os.path.join(app.root_path, 'static', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Create a single optimized burger image
        target_filename = 'burger-menu.jpg'
        target_path = os.path.join(upload_dir, target_filename)
        
        # Process and save the image once
        with Image.open(source_image) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Resize image to a good size for menu items
            target_size = (400, 300)  # Smaller size for better performance
            img = img.resize(target_size, Image.Resampling.LANCZOS)
            
            # Save with good quality
            img.save(target_path, 'JPEG', quality=90, optimize=True)
        
        # Update all burger items to use this image
        burger_items = FoodItem.query.filter_by(category='burgers').all()
        for burger in burger_items:
            burger.image_path = os.path.join('uploads', target_filename)
        
        # Save changes
        db.session.commit()
        print("All burger images updated successfully!")

if __name__ == '__main__':
    set_burger_image() 