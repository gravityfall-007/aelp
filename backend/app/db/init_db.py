from app.models.base import Base
from app.db.session import engine
from app.models import fleet  # noqa

def init_db():
    Base.metadata.create_all(bind=engine)