from backend.app.database.connection import Base, engine
from backend.app.models.user import User
from backend.app.models.student_profile import StudentProfile


def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    initialize_database()