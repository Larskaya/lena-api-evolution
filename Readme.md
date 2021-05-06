Evolution 

Игровое приложение на python, flask с бд postgresql

Запуск основного кода происходит командой python main.py из основной дирректории.
Так же надо запускать методы обновления количества существ и еды в секторах python /methods/start.py


Все урлы приложения

user/
    POST - добавляет пользователя 
    GET - много либо один

    /{user_id}/profile 
        PATCH - меняет настройки одного профиля, добавляет цвет и скилл существу (профиль)

    /{user_id}/add_skill 
        PATCH - меняет настройки скиллов (add_skill)

    /{user_id}/occupy
        POST - добавление юзера в сектор 

auth/
    login 
        POST - авторизация 
    logout 
        POST - разлогиниться 
    logout_full
        POST - разлогиниться


message/ 
    POST - добавляет сообщение 
    GET - получает последние 100 сообщений из всех


sector/
    POST - добавляет сектор 
    GET - достает сектора 



SKILLS

0 - движение
1 - кушоц растения
2 - кушоц существ
3 - быстрый обмен веществ
4 - крылья/плавники
5 - прятать запасы (только для кушоющих растения)
6 - крупный размер
7 - броня (повышает вес)
8 - половое размножение (увеличивает количество мутаций)
9 - впадать в спячку (если еды не хватает)
10 - стайность (плюс к обороне, минус к плодовитости)
11 - нервная система для дружбы (пользователь  может предложить дружбу)
12 - нервная система для еды (пользователь может замедлить питание)


    


Идея игры заключается в развитии существ. Каждый пользователь начинает с абиогенеза - теории о происхождении живого из неживого - и пытается развить существ этого вида, количество которых постоянно увеличивается из-за автоматического поедания пищи, до следующего на пути становления человека (аналогично Земле). 

Игровое поле делится на сектора: водный (стартовый), лесной (основной) и три последних, усложненных, где холод, песок, тайга (по выбору).

После завершения развития в водном секторе пользователь по выбору получает тип своих существ - плотоядный или травоядный. 
У каждого типа свои преимущества и недостатки.


При попадании на сайт пользователь проходит регистрацию, затем логиниться и получает возможность создать профиль, в котором появится изображение существа, их количевство в секторе, две шкалы голода и здоровья.