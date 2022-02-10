import json
import os

from flask import request, flash, redirect, url_for
from werkzeug.utils import secure_filename

from config import *


def read_file_json():
    with open(FILE_POSTS, encoding='utf-8') as f:
        posts = json.load(f)
        if posts:
            return posts
        return []


def get_posts_by_tag():
    pass


def get_all_tags(description):
    tags = []
    for word in description.split(' '):
        if word.startwith('#'):
            tags.append(word[1:])
    return tags



def upload_image():
    if 'picture' in request.files:
        # После перенаправления на страницу загрузки
        # покажем сообщение пользователю
        flash('Не могу прочитать файл')
        return '<h1>ошибка загрузки</h1>'

    file = request.files.get("picture")

    if file.filename == '':
        return '<h1>ошибка загрузки</h1>'

    if file and allowed_file(file.filename):
        # безопасно извлекаем оригинальное имя файла
        filename = secure_filename(file.filename)
        # сохраняем файл
        file.save(os.path.join(UPLOAD_FOLDER, filename))


    return file


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


