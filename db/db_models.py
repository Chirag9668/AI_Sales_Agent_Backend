from sqlalchemy import Column, Integer, String, Text

from db.database import base, engine


class Conversation(base):

    __tablename__ = "conversations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        String,
        index=True
    )

    role = Column(
        String
    )

    message = Column(
        Text
    )