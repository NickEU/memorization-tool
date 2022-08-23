from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

DB_FILENAME = "flashcard.db"
engine = create_engine(f'sqlite:///{DB_FILENAME}?check_same_thread=False')
Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


Base.metadata.create_all(engine)


def get_all_flashcards():
    with Session(engine) as session:
        flashcards = session.query(Flashcard).all()
        return flashcards


def save_flashcard(question, answer):
    with Session(engine) as session:
        new_flashcard = Flashcard(question=question, answer=answer)
        session.add(new_flashcard)
        session.commit()
