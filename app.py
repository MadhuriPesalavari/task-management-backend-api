from flask import Flask
from extensions import db, migrate, jwt


def create_app():

    app = Flask(__name__)

    # =========================
    # CONFIGURATION
    # =========================
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres1234@localhost/taskdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'mysecretkey'

    # =========================
    # INITIALIZE EXTENSIONS
    # =========================
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # =========================
    # HOME ROUTE
    # =========================
    @app.route("/")
    def home():
        return {"message": "Task API is running"}

    # =========================
    # IMPORT & REGISTER BLUEPRINTS
    # =========================
    from routes.auth import auth_bp
    from routes.task import task_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app


# =========================
# CREATE APP INSTANCE
# =========================
app = create_app()

# =========================
# IMPORT MODELS (FOR MIGRATIONS)
# =========================
from models.user import User
from models.task import Task

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)