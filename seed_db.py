from app import create_app
from models import db, Event, Category
from datetime import datetime, timedelta


def ensure_categories(names):
    out = []
    for name in names:
        cat = Category.query.filter_by(name=name).first()
        if not cat:
            cat = Category(name=name)
            db.session.add(cat)
        out.append(cat)
    return out


events_data = [
    {
        'title': 'Genç Sanatçılar Karma Sergisi',
        'description': (
            'Genç ressam ve heykeltıraşların ortak seçkisi; dijital işler '
            've klasik teknikler bir arada.'
        ),
        'location': 'Kültür ve Sanat Merkezi, Çankaya',
        'days': 3,
        'hours': 18,
        'categories': ['Sergi', 'Görsel Sanatlar'],
        'image': (
            'https://images.unsplash.com/photo-1526498460520-4c246339dccb'
            '?auto=format&fit=crop&w=900&q=80'
        )
    },
    # (kept short) reuse same sample set from init_db.py if needed
]


def seed():
    # This script is idempotent: it will not duplicate events with same title.
    app = create_app()

    with app.app_context():
        # create tables if missing
        db.create_all()

        base = datetime.utcnow()

        created = 0
        for data in events_data:
            # skip if event title already exists
            existing = Event.query.filter_by(title=data['title']).first()
            if existing:
                continue

            cats = ensure_categories(data['categories'])
            ev = Event(
                title=data['title'],
                description=data['description'],
                location=data['location'],
                start_time=base + timedelta(days=data['days'], hours=data['hours']),
                end_time=base + timedelta(days=data['days'], hours=data['hours'] + 2),
                image_url=data['image']
            )
            ev.categories.extend(cats)
            db.session.add(ev)
            created += 1

        if created > 0:
            db.session.commit()
            print(f"Seed complete: {created} new events added.")
        else:
            print("Seed complete: no new events to add.")


if __name__ == '__main__':
    seed()
