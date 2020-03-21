# CarPrice

## Установка

```
git clone git@github.com:moskrc/carprice.git
cd carprice
pipenv install
# если нет такой версии python то
brew update && brew upgrade pyenv
# и затем повторить pipenv install

# Настройки по умолчанию
cp .env.example .env
# Миграции
pipenv run migrate
# Создание администратора
pipenv run createsuperuser
# Запуск
pipenv run runserver


# В отдельно вкладке запустить webpack
cd assets
npm install
npm run dev
```
