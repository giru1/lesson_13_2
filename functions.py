import json
import pprint

from flask import render_template, request

from config import FILE_POSTS, UPLOAD_FOLDER
from utils import upload_image, read_file_json, get_all_tags, allowed_file

posts = read_file_json()


def index_url():
    """
    обработка главной страницы
    :return:
    """
    tags = []
    for post in posts:
        post_description = post.get('content')
        tags_in_description = get_all_tags(post_description)
        for tag in tags_in_description:
            tags.append(tag)

    return render_template('index.html', tags=tags)


def tag_url():
    """
    Обработка страницы поиск по тегу
    :return:
    """
    tag_name = request.args.get('tag')
    select_posts = []

    for post in posts:
        if '#' + tag_name in post.get('content'):
            select_posts.append(post)

    return render_template('post_by_tag.html', posts=select_posts, tagname=tag_name)


def add_post_url():
    """
    Обработка страницы
    :return:
    """
    if request.method == "POST":
        text = request.form.get("content")
        file = request.files.get('picture')

        if file and allowed_file(file.filename):
            upload_image(file)

        else:
            return 'Ошибка загрузки'

        post = {
            "pic": '/' + UPLOAD_FOLDER + '/' + file.filename,
            "content": text
        }
        posts.append(post)
        pprint.pprint(posts)
        with open(FILE_POSTS, 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False)
        return render_template('post_uploaded.html', text=text, file=file)
    return render_template('post_form.html')
