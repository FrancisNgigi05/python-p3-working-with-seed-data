#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Game).delete()
    session.commit()

    botw = Game(title="Breath of the wild", platform="Switch", genre="Adventure", price = 60)
    ffvi = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
    css = Game(title="Candy Crush Saga", platform="Switch", genre="Puzzle", price=0)

    session.bulk_save_objects([botw, ffvi, mk8])
    session.commit()
    print(session.query(Game).count())
    print(session.query(Game)[-1])
    
    session.query(Game).delete()
    session.commit()

    session.bulk_save_objects([botw, ffvi, mk8, css])
    print(session.query(Game).count())
    print(session.query(Game)[-1])

    session.query(Game).delete()
    session.commit()

    # Add a console message so we can see output when the seed file runs
    print("Seeding games...")

    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
    for i in range(50)]


    session.bulk_save_objects(games)

    print(session.query(Game).count())
    print(session.query(Game).first())
    print(session.query(Game)[-1])

    session.commit()