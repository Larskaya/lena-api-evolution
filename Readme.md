Evolution 

Игровое приложение на python, flask с бд postgresql

Запуск основного кода происходит командой python main.py из основной дирректории.
Так же надо запускать методы обновления количества существ и еды в секторах python /methods/start.py


Все урлы приложения

/sector
GET (добавить), POST 

/sectors 
GET

/login 
POST

/messages 
GET, POST

/profile 
POST, GET (добавить)

/registration 
POST


Идея игры заключается в развитии существ. Каждый пользователь начинает с абиогенеза - теории о происхождении живого из неживого - и пытается развить существ этого вида, количество которых постоянно увеличивается из-за автоматического поедания пищи, до следующего на пути становления человека (аналогично Земле). 

Игровое поле делится на сектора: водный (стартовый), лесной (основной) и три последних, усложненных, где холод, песок, тайга (по выбору).

После завершения развития в водном секторе пользователь по выбору получает тип своих существ - плотоядный или травоядный. 
У каждого типа свои преимущества и недостатки.


При попадании на сайт пользователь проходит регистрацию, затем логиниться и получает возможность создать профиль, в котором появится изображение существа, их количевство в секторе, две шкалы голода и здоровья.