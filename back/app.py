from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import CORS
from views import main_service, like_count, recommend_view
from flask import Flask
from models import db
import os


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@localhost:3306/{os.environ.get('DB_DATABASE')}"
app.secret_key = os.environ.get('SESSION_KEY')

app.register_blueprint(main_service.bp)
app.register_blueprint(like_count.bp)
app.register_blueprint(recommend_view.bp)

CORS(app)

db.init_app(app)
Migrate().init_app(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
