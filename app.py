from flask import Flask
from extensions import db
from routes import customers_bp, vehicles_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///garage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(customers_bp)
app.register_blueprint(vehicles_bp)

@app.before_request
def create_tables_once():
    if not getattr(app, '_tables_created', False):
        db.create_all()
        app._tables_created = True

@app.route('/')
def home():
    return "Garage Manager is running!"

if __name__ == '__main__':
    app.run(debug=True)
