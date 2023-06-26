import datetime


class Entry:
    def __init__(self, title, body):
        self.__title = title
        self.__body = body
        self.__gist_id = 0
        self.__time_created = datetime.datetime.now()

    def set_title(self, title):
        self.__title = title

    def set_body(self, body):
        self.__body = body

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def set_id(self, gist_id):
        self.__gist_id = gist_id

    def get_id(self):
        return self.__gist_id

    def get_time_created(self):
        return self.__time_created
