import pytest
from musics.models import Music, Sheet
from django_pytest_tutorial import settings
from django_pytest_tutorial.settings import BASE_DIR

class TestUseExistDB:
  # 使用既有存在的 database
  @pytest.fixture(scope='session')
  def django_db_setup(self):
      settings.DATABASES['default'] = {
          "ENGINE": "django.db.backends.sqlite3",
          "NAME": BASE_DIR / "db.sqlite3",
      }

  @pytest.mark.django_db
  def test_check_external_db_music_count(self, django_db_setup):
    # 目前我在這db放了一比 Music 資料
    assert Music.objects.count() == 1

  @pytest.mark.django_db
  def test_check_external_db_sheet_count(self, django_db_setup):
    # 目前我在這db放了一比 Sheet 資料
    assert Sheet.objects.count() == 1


class Test:
  @pytest.fixture
  def create_music(self):
      Music.objects.create(song='john')

  @pytest.mark.django_db
  def test_music_song(self, create_music):
      music = Music.objects.filter(song='john')
      assert music[0].song == 'john'

  @pytest.mark.django_db
  def test_music_count(self, create_music):
    assert Music.objects.count() == 1

