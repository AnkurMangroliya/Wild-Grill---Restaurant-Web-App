from app import create_app, db
from app.models import FoodItem

def add_menu_items():
    app = create_app()
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()

        # Burgers
        burgers = [
            {
                'name': 'Classic Burger',
                'description': 'Juicy beef patty with fresh lettuce, tomatoes, and our special sauce',
                'price': 12.99,
                'category': 'burgers',
                'image_path': 'uploads/classic-burger.jpg'
            },
            {
                'name': 'Cheese Burger',
                'description': 'Our classic burger topped with melted cheddar cheese',
                'price': 13.99,
                'category': 'burgers',
                'image_path': 'uploads/cheese-burger.jpg'
            },
            {
                'name': 'Bacon Burger',
                'description': 'Classic burger with crispy bacon strips and BBQ sauce',
                'price': 14.99,
                'category': 'burgers',
                'image_path': 'uploads/bacon-burger.jpg'
            },
            {
                'name': 'Mushroom Swiss Burger',
                'description': 'Beef patty with sautéed mushrooms and melted Swiss cheese',
                'price': 14.99,
                'category': 'burgers',
                'image_path': 'uploads/mushroom-burger.jpg'
            }
        ]

        # Wraps
        wraps = [
            {
                'name': 'Chicken Caesar Wrap',
                'description': 'Grilled chicken with romaine lettuce, parmesan, and caesar dressing',
                'price': 11.99,
                'category': 'wraps',
                'image_path': 'uploads/chicken-caesar-wrap.jpg'
            },
            {
                'name': 'Veggie Wrap',
                'description': 'Fresh vegetables with hummus and feta cheese',
                'price': 10.99,
                'category': 'wraps',
                'image_path': 'uploads/veggie-wrap.jpg'
            },
            {
                'name': 'Buffalo Chicken Wrap',
                'description': 'Spicy buffalo chicken with blue cheese and celery',
                'price': 12.99,
                'category': 'wraps',
                'image_path': 'uploads/buffalo-wrap.jpg'
            },
            {
                'name': 'Falafel Wrap',
                'description': 'Crispy falafel with tahini sauce and fresh vegetables',
                'price': 11.99,
                'category': 'wraps',
                'image_path': 'uploads/falafel-wrap.jpg'
            }
        ]

        # Extras
        extras = [
            {
                'name': 'French Fries',
                'description': 'Crispy golden fries with sea salt',
                'price': 4.99,
                'category': 'extras',
                'image_path': 'uploads/french-fries.jpg'
            },
            {
                'name': 'Onion Rings',
                'description': 'Crispy battered onion rings',
                'price': 5.99,
                'category': 'extras',
                'image_path': 'uploads/onion-rings.jpg'
            },
            {
                'name': 'Coleslaw',
                'description': 'Fresh cabbage and carrot slaw with our special dressing',
                'price': 3.99,
                'category': 'extras',
                'image_path': 'uploads/coleslaw.jpg'
            },
            {
                'name': 'Side Salad',
                'description': 'Mixed greens with cherry tomatoes and balsamic dressing',
                'price': 4.99,
                'category': 'extras',
                'image_path': 'uploads/side-salad.jpg'
            }
        ]

        # Add all items to database
        all_items = burgers + wraps + extras
        for item_data in all_items:
            food_item = FoodItem(**item_data)
            db.session.add(food_item)

        db.session.commit()
        print("Menu items added successfully!")

if __name__ == '__main__':
    add_menu_items() 