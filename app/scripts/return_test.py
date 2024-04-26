from sqlalchemy import func

from app import db, create_app
from app.models import Verb
import random

app = create_app()
app.app_context().push()


if __name__ == '__main__':
    verb = Verb.query.order_by(func.random()).first()
    # if verb:
    #     print(verb.conjugations)
    for i in range(10):
        print(Verb.query.order_by(func.random()).first())
