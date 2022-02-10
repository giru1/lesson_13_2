from flask import Flask, request, render_template, send_from_directory
# from functions import ...

POST_PATH = "static/posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

import views


