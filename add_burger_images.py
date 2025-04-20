from app import create_app, db
from app.models import FoodItem
import os
import shutil
from PIL import Image

def add_burger_images():
    app = create_app()
    with app.app_context():
        # Get all burger items
        burger_items = FoodItem.query.filter_by(category='burgers').all()
        
        # Source image path
        source_image = 'burger-screenshot.jpg'
        
        # Ensure uploads directory exists
        upload_dir = os.path.join(app.root_path, 'static', 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        
        # Copy and rename the image for each burger
        for burger in burger_items:
            # Create a unique filename for each burger
            filename = f"{burger.name.lower().replace(' ', '-')}.jpg"
            target_path = os.path.join(upload_dir, filename)
            
            # Open and resize the image
            with Image.open(source_image) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Calculate dimensions to maintain aspect ratio
                target_width = 800
                target_height = 600
                width, height = img.size
                
                # Calculate scaling factor
                width_ratio = target_width / width
                height_ratio = target_height / height
                ratio = min(width_ratio, height_ratio)
                
                # Calculate new dimensions
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                
                # Resize image
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Create new image with white background
                new_img = Image.new('RGB', (target_width, target_height), (255, 255, 255))
                
                # Paste resized image in center
                paste_x = (target_width - new_width) // 2
                paste_y = (target_height - new_height) // 2
                new_img.paste(img, (paste_x, paste_y))
                
                # Save with high quality
                new_img.save(target_path, 'JPEG', quality=95, optimize=True)
            
            # Update the database record
            burger.image_path = os.path.join('uploads', filename)
        
        # Commit the changes
        db.session.commit()
        print("Burger images added successfully!")

if __name__ == '__main__':
    add_burger_images() 