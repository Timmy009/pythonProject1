from diaryApp.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.__gists: list[Entry] = []
        self.__username = username
        self.__password = password
        self.__is_locked = True

    def is_locked(self):
        return self.__is_locked

    def unlocked_diary(self, password):
        if self.__password == password:
            self.__is_locked = False

    def locked_diary(self):
        self.__is_locked = True

    def create_gist(self, title, body):
        gist: Entry = Entry(title, body)
        self.__gists.append(gist)

    def gist_count(self):
        return len(self.__gists)

    def delete_gist(self, title):
        for entry in self.__gists:
            if entry.get_title() == title:
                self.__gists.remove(entry)
