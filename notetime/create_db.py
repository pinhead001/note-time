from notetime.db import engine
from notetime.models import Base

def create_db():
    Base.metadata.create_all(engine)
    print("Database created successfully.")

if __name__ == "__main__":
    create_db()
