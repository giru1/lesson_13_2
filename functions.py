import os

from flask import render_template, request, redirect, url_for

from utils import upload_image, read_file_json


posts = read_file_json()


def index_url():
    """

    :return:
    """
    tags = []
    for post in posts:
        for key, value in post.items():
            if key == 'content':
                temp_list = value.split()
                for item in temp_list:
                    if '#' in item:
                        tags.append(item.replace('#', '').capitalize())

    return render_template('index.html', tags=tags)


def tag_url():
    tag_name = request.args.get('tag')
    select_posts = []

    for post in posts:
        for key, value in post.items():
            if key == 'content':
                temp_list = value.split()
                for item in temp_list:
                    if '#' + tag_name.lower() == item.lower():
                        select_posts.append(post)

    return render_template('post_by_tag.html', posts=select_posts, tagname=tag_name)


def add_post_url():
    if request.method == "POST":
        text = request.form.get("content")
        file = upload_image()

        if file:
            return render_template('post_uploaded.html', text=text, file=file)
        else:
            return '<h1>ошибка загрузки</h1>'

    return render_template('post_form.html')
