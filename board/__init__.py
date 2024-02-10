from flask import Flask, url_for
from board import pages, posts, db

import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    
    db.init_app(app)
    
    app.register_blueprint(posts.bp)
    app.register_blueprint(pages.bp)
    
    print(f"Current environment: {os.getenv('ENVIRONMENT')}")
    print(f"Using Database: {app.config.get('DATABASE')}")
    return app