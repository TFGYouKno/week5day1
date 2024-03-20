from flask import Flask

app = Flask(__name__)

from resources.posts import routes
from resources.user import routes