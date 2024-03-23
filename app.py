from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from flask_graphql_auth import GraphQLAuth
from config import Config
from schema import schema
from models import *


# Create Flask application
app = Flask(__name__)
cors = CORS(app)
# Load database configurations from Config class
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Initialize Flask-Migrate
migrate = Migrate(app, db)

auth = GraphQLAuth(app) 
# Define the route for GraphiQL
app.add_url_rule(
    '/api/',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enable GraphiQL interface
    )
)



# Define a route for the homepage
@app.route('/')
def index():
    return 'API TEST RUNNING'    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
