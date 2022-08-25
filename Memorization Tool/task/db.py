from sqlalchemy import create_engine, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from enums import LeitnerBox

DB_FILENAME = "flashcard.db"
engine = create_engine(f'sqlite:///{DB_FILENAME}?check_same_thread=False')
Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    leitner_box = Column(Enum(LeitnerBox))


Base.metadata.create_all(engine)


def get_all_flashcards():
    with Session(engine) as session:
        flashcards = session.query(Flashcard).all()
        return flashcards


def create_flashcard(question, answer):
    with Session(engine) as session:
        new_flashcard = Flashcard(question=question, answer=answer, leitner_box=LeitnerBox.DIFFICULT)
        session.add(new_flashcard)
        session.commit()


def update_flashcard(flashcard):
    if flashcard.leitner_box == LeitnerBox.TO_DELETE:
        delete_flashcard(flashcard)
        return

    with Session(engine) as session:
        query = session.query(Flashcard)
        card_filter = query.filter(Flashcard.id == flashcard.id)
        card_filter.update({'question': flashcard.question,
                            'answer': flashcard.answer,
                            'leitner_box': LeitnerBox(flashcard.leitner_box)})
        session.commit()


def delete_flashcard(flashcard):
    with Session(engine) as session:
        query = session.query(Flashcard)
        query.filter(Flashcard.id == flashcard.id).delete()
        session.commit()
