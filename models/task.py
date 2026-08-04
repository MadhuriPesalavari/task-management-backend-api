from extensions import db

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # ✅ FIXED FOREIGN KEY
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)