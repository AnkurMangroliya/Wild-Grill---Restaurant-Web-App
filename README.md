# WildGrill Restaurant

A modern web application for managing a restaurant's menu and orders.

## Features (Phase 1)

- Display food items on homepage
- Admin interface for menu management
- Image upload functionality
- Responsive design with Bootstrap

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key
```

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Project Structure

```
wildgrill/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       └── admin/
│           └── add_item.html
├── static/
│   ├── css/
│   └── uploads/
├── requirements.txt
└── README.md
```

## Development Roadmap

### Phase 1 (Current)
- Basic menu display
- Admin interface
- Image upload

### Phase 2 (Upcoming)
- User authentication
- Ordering system
- Notifications

### Phase 3 (Planned)
- Dockerization
- Production deployment 