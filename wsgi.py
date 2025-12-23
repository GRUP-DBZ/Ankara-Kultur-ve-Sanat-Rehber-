from app import create_app
from models import db
from datetime import datetime, timedelta

app = create_app()

# Auto-initialize database on startup
with app.app_context():
    db.create_all()
    # Seed sample data if events table is empty
    from models import Event, Category
    if Event.query.count() == 0:
        categories = [
            Category(name='Konser'),
            Category(name='Tiyatro'),
            Category(name='Sergi'),
            Category(name='Konferans'),
            Category(name='Spor')
        ]
        db.session.add_all(categories)
        db.session.commit()
        
        base = datetime.utcnow()
        events = [
            Event(title='Açık Hava Konser', start_time=base + timedelta(days=1), 
                  end_time=base + timedelta(days=1, hours=3), location='Ankara Park',
                  description='Müzik festivali', categories=[categories[0]]),
            Event(title='Sanat Sergisi', start_time=base + timedelta(days=3),
                  end_time=base + timedelta(days=10), location='Resim Galerisi',
                  description='Modern sanat sergisi', categories=[categories[2]]),
        ]
        db.session.add_all(events)
        db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
