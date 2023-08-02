import pynecone as pc
from sqlmodel import Field
import datetime


class Speaker(pc.Model, table=True):
    name: str
    bio: str
    date: str


class Attendee(pc.Model, table=True):
    name: str
    email: str
