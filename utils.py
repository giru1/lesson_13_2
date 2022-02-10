import json
import os

from werkzeug.utils import secure_filename

from config import FILE_POSTS, UPLOAD_FOLDER, ALLOWED_EXTENSIONS


def read_file_json():
    """
    Читаем файлы json
    :return:
    """
    with open(FILE_POSTS, encoding='utf-8') as f:
        posts = json.load(f)
        if posts:
            return posts
        return []


def get_all_tags(description):
    """
    Собираем все теги в список
    :param description:
    :return: список тегов
    """
    tags = []
    for word in description.split(' '):
        if word.startswith('#'):
            tags.append(word.replace('#', ''))
    return tags


def upload_image(file):
    """
    Сохранение картинки
    :param file:
    :return:
    """
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return file


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
