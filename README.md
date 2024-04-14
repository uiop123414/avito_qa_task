# Чтобы запусть тест кейс нужно выполнить следующую последовательность команд

py -m venv venv 

venv\Scripts\activate

pip install -r requirements.txt

playwright intstall 

# Чтобы все тесты корректно отработали , нужно получить данные storage для этого нужно выполнить следующую команду и авторизоваться в ручную за 60 секунд

py get_state.py

# После можно запускать тестирование

pytest ./test/test_main.py


