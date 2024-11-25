# **Alexandrian Librarian**
### **Описание**



## Запуск

**Стандартный запуск**
<br>
1. Скачайте или кронируйте папку проекта (`git clone https://github.com/ReptiloidAnunak/joker_batman_ai`)<br>
2. Перейдите в коревую папку проекта (`cd joker_batman_ai`) и запустите команду установки виртуального окружения `python3 -m venv .venv`<br>
3. Активируйте виртуальное окружение 
Linux/Mac: `source .venv/bin/activate`<br>
Windows (Command Prompt): `.venv\Scripts\activate`<br>
Windows (PowerShell): `.venv\Scripts\Activate.ps1`<br>
<br>
4. Установите необходимые библиотеки
`pip install -r requirements.txt`<br>
5. Запустите код `python run.py`
<br><br>

**Запуск с помощью Docker**

Если на вашем компьютере не установлен Docker, скачайте его по инструкции на [официальном сайте](https://www.docker.com/get-started/)
1. Скачайте или кронируйте папку проекта (git clone https://github.com/ReptiloidAnunak/joker_batman_ai)
3. Убедитесь, что вы находитесь в корневой директории, где расположен [Dockerfile](Dockerfile)<br>Запустите команду сбора докер-контейнера `docker build -t alexandrian_librarian .`
4. Запустите докер-контейнер<br>`docker run -it alexandrian_librarian`
