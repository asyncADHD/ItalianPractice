# populate_verbs.py
from app import db, create_app
from app.models import Verb

app = create_app()
app.app_context().push()  # This line is necessary to run the script outside of Flask app context

common_verbs = [
    "be", "have", "do", "say", "get", "make", "go", "know", "take", "see",
    "come", "think", "look", "want", "give", "use", "find", "tell", "ask", "work",
    "seem", "feel", "try", "leave", "call", "laugh", "hear", "continue", "buy",
    "stay", "suggest", "open", "watch", "walk", "listen", "run", "answer", "place",
    "travel", "express", "concentrate", "prepare", "plan", "attempt", "marry", "experience",
    "recommend", "ride", "view", "question", "enhance", "purchase", "telephone"
]

def populate_verbs():
    # Check if the table is empty and only then populate it
    if Verb.query.count() == 0:
        verbs_to_add = [Verb(infinitive=verb) for verb in common_verbs]
        db.session.bulk_save_objects(verbs_to_add)
        db.session.commit()
        print("Database populated with common verbs.")
    else:
        print("Database already contains data.")

if __name__ == '__main__':
    populate_verbs()
