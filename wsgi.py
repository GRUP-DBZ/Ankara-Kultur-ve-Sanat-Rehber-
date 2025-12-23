from app import create_app
import os

app = create_app()

# Auto-initialize database with seed on startup
with app.app_context():
    from models import db, Event, Category
    from datetime import datetime, timedelta
    
    db.create_all()
    
    # Seed if empty
    if db.session.query(Event).count() == 0:
        categories_data = ['Konser', 'Tiyatro', 'Sergi', 'Konferans', 'Spor']
        categories = []
        for cat_name in categories_data:
            cat = Category(name=cat_name)
            db.session.add(cat)
            categories.append(cat)
        db.session.commit()
        
        base = datetime.utcnow()
        events_data = [
            Event(
                title='Açık Hava Konser',
                description='Müzik festivali',
                location='Ankara Park',
                start_time=base + timedelta(days=1, hours=13),
                end_time=base + timedelta(days=1, hours=16),
                image_url='https://images.unsplash.com/photo-1459749411175-04bf5292ceea?auto=format&fit=crop&w=900&q=80',
                categories=[categories[0]]
            ),
            Event(
                title='Sanat Sergisi',
                description='Modern sanat sergisi',
                location='Resim Galerisi',
                start_time=base + timedelta(days=3, hours=10),
                end_time=base + timedelta(days=3, hours=18),
                image_url='https://images.unsplash.com/photo-1578149381288-8bfc85f0a18e?auto=format&fit=crop&w=900&q=80',
                categories=[categories[2]]
            ),
            Event(
                title='Klasik Tiyatro Oyunu',
                description='Meşhur klasik bir oyunun modernleştirilmiş versiyonu',
                location='Devlet Tiyatrosu',
                start_time=base + timedelta(days=5, hours=19),
                end_time=base + timedelta(days=5, hours=21),
                image_url='https://images.unsplash.com/photo-1524306087590-cc92b1b0d67a?auto=format&fit=crop&w=900&q=80',
                categories=[categories[1]]
            ),
            Event(
                title='Fotografi Sergisi',
                description='Türkiye\'nin en güzel doğal manzaralarının sergisi',
                location='Ankara Sanat Merkezi',
                start_time=base + timedelta(days=7, hours=14),
                end_time=base + timedelta(days=7, hours=18),
                image_url='https://images.unsplash.com/photo-1561070791-2526d30994b5?auto=format&fit=crop&w=900&q=80',
                categories=[categories[2]]
            ),
            Event(
                title='Jazz Müzik Gecesi',
                description='Ünlü caz müzisyenlerin birlikte performansı',
                location='Ankara Caz Kulübü',
                start_time=base + timedelta(days=10, hours=20),
                end_time=base + timedelta(days=10, hours=23),
                image_url='https://images.unsplash.com/photo-1494700049270-c10122d29d44?auto=format&fit=crop&w=900&q=80',
                categories=[categories[0]]
            ),
        ]
        db.session.add_all(events_data)
        db.session.commit()
        print("Database seeded successfully with 5 events!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
