# django_pytest_tutorial

本篇文章要介紹 django + pytest

如果不了解 pytest, 可參考之前寫的 [pytest 教學](https://github.com/twtrubiks/python-notes/tree/master/pytest_tutorial)

使用 [pytest-django](https://pytest-django.readthedocs.io/en/latest/) 這個套件

安裝套件

```cmd
pip install -r requirement.txt
```

先 migrate 一下 (非必要)

```cmd
python3 manage.py makemigrations
python3 manage.py migrate
```

記得要把要測試的 app 加到 `INSTALLED_APPS` 中, 像這邊要測試 `musics`.

pytest 設定檔可參考 [pytest.ini](https://github.com/twtrubiks/django_pytest_tutorial/blob/main/pytest.ini)

```ini
[pytest]
DJANGO_SETTINGS_MODULE = django_pytest_tutorial.settings
python_files = tests.py test_*.py *_tests.py
```

設定 DJANGO_SETTINGS_MODULE 以及要測試的檔案.

使用方法很簡單, 執行輸入 `pytest -s -v` 即可.

範例的測試都在 [tests.py](https://github.com/twtrubiks/django_pytest_tutorial/blob/main/musics/tests.py) 這邊

先來看這段

```python
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
```

透過 `@pytest.mark.django_db` 讓我們可以 access db,

也可以連接已經建立好的 db 來進行測試

```python
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
```

