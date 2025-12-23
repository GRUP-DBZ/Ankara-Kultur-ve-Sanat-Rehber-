from app import create_app
import os

app = create_app()

# Auto-seed database on every startup
with app.app_context():
    from models import db, Event
    
    # Create tables
    db.create_all()
    
    # If no events exist, seed the database
    try:
        if db.session.query(Event).count() == 0:
            from seed_db import seed_database
            seed_database(app)
    except Exception as e:
        print(f"Seed error: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
