from flask import send_from_directory

from app import app
import functions


@app.route("/")
def page_index():
    return functions.index_url()


@app.route("/tag/", methods=["GET", "POST"])
def page_tag():
    return functions.tag_url()


@app.route("/post/", methods=["GET", "POST"])
def page_post_form():
    return functions.add_post_url()


@app.route("/uploads/<path:path>", methods=["GET", "POST"])
def static_dir(path):
    return send_from_directory("uploads", path)
