import pytest
from diaryApp.diary import Diary


def test_that_diary_is_locked_by_default():
    diary = Diary("username", "password")
    assert diary.is_locked() == True


def test_that_diary_can_be_unlocked():
    diary = Diary("username", "password")
    diary.unlocked_diary("password")
    assert diary.is_locked() == False


def test_that_diary_can_be_locked():
    diary = Diary("username", "password")
    diary.unlocked_diary("password")
    assert diary.is_locked() == False
    diary.locked_diary()
    assert diary.is_locked() == True


def test_that_i_can_craete_gist():
    diary = Diary("username", "password")
    diary.unlocked_diary("password")
    assert diary.is_locked() == False
    diary.create_gist("title", "body")
    assert diary.gist_count() == 1

def test_that_i_can_delete_gist():
    diary = Diary("username", "password")
    diary.unlocked_diary("password")
    assert diary.is_locked() == False
    diary.create_gist("title", "body")
    diary.create_gist("title1", "body")
    assert diary.gist_count() == 2
    diary.delete_gist("title")
    assert diary.gist_count() == 1