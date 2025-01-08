# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Автор', color="#c8ffc8")
define p = Character("[player_name]", color="#c8ffc8")
define m = Character('Мама', color="#c8ffc8")
define character_image = "images/persona1.png"
define gallery = []


init python:
    import os
    import databaseuser   # Импортируем файл databaseuser.py
    import databaseaudio  
    import databasevideo
    saved_images = []  # Список для хранения изображений

    def save_image(image_name):
        if image_name not in saved_images:
            saved_images.append(image_name)

#Эпизоды истории
    completed_episodes = {
        "episode_1": False,
        "episode_2": False,
        "episode_3": False,
    }

    
# Функция для добавления изображения в галерею
    def add_to_gallery(image, description):
        gallery.append((image, description))    


label start:

    show image_3  #выводит изображения на экран
    # Запрос имени у пользователя
    $ player_name = renpy.input("Введите имя вашего персонажа:", default="Имя персонажа")
    if player_name == "":
        $ player_name = "Имя персонажа"  # Установление значение по умолчанию, если пользователь ничего не ввел
    hide image_3
    
    play music "spokoynaya.mp3"     #выводит музыку

  
label main_menuaut:
    show image_4  #фон Горный
    $ add_to_gallery("image_4", "Это описание первого изображения.")
    e "Добро пожаловать! Выберите действие:"
    menu:
        "Регистрация":
            jump register
        "Вход":
            jump login
        "Выход":
            return
    hide image_4
    
    
label register:         #Регистрация пользователя
    show image_4
    $ username = renpy.input("Введите имя пользователя:")
    $ email = renpy.input("Введите адрес электронной почты:")
    $ password = renpy.input("Введите пароль:")
    hide image_4

    if databaseuser.register_user(username, email, password):
        show image_4
        e "Регистрация прошла успешно!"
        hide image_4
        jump storymain_menu
    else:
        show image_4
        e "Пользователь с таким именем или адресом электронной почты уже существует."
        hide image_4
        jump main_menuaut

    jump main_menuaut



label login:      #Вход в систему
    show image_4
    $ username = renpy.input("Введите имя пользователя:")
    $ password = renpy.input("Введите пароль:")
    hide image_4
    if databaseuser.check_user(username, password):
        show image_4
        e "Вы успешно вошли в систему!"
        hide image_4
        jump storymain_menu
    else:
        show image_4
        e "Неправильное имя пользователя или пароль."
        hide image_4
        jump main_menuaut

    jump mmain_menuautenu



label storymain_menu:   #Начальное меню
    show image_4
    e "Куда отправимся?"
    menu:
        "Истории":
            jump story_menu
        "Сменить аккаунт":
            return

label story_menu:
    e "Выберите историю, которую хотите начать:"
    menu:
        "История 1":
            jump story_1
        "История 2":
            jump story_2
        "История 3":
            jump story_3
        "Назад в главное меню":
            jump storymain_menu
hide image_4

label story_1:
    e "Вы выбрали Историю 1."
    # Начало истории 1

    e "Это начало Истории 1."

    # Пример сохранения
    $ renpy.save("story_1_progress")
    e "Ваш прогресс сохранен."
    e "История завершена. Возвращаемся в меню."
    jump story_menu

label story_2:
    # Другие кнопки меню
    show image_4
    menu:
        "Читать историю":
            jump episode_menu
        "Назад":
            jump story_menu

label episode_menu:
    e "Выберите эпизод, который хотите начать:"
    
    # Проверка доступности эпизодов
    if not completed_episodes["episode_1"]:
        menu:
            "Эпизод 1":
                jump episode_1
            "Выход":
                jump story_menu
    elif not completed_episodes["episode_2"]:
        menu:
            "Эпизод 1 (завершен)":
                e "Вы уже завершили Эпизод 1."
                jump episode_1
            "Эпизод 2":
                jump episode_2
            "Выход":
                jump story_menu
    elif not completed_episodes["episode_3"]:
        menu:
            "Эпизод 1 (завершен)":
                jump episode_1
            "Эпизод 2 (завершен)":
                jump episode_2
            "Эпизод 3":
                jump episode_3
            "Выход":
                jump story_menu
    else:
        e "Все эпизоды завершены!"
        menu:
            "Эпизод 1 (завершен)":
                jump episode_1
            "Эпизод 2 (завершен)":
                jump episode_2
            "Эпизод 3 (завершен)":
                jump episode_3
            "Выход":
                jump story_menu
        #jump story_menu
hide image_4

label episode_1:
    show image_2
    show image_1:
        xpos 0.0 ypos 0.2 # начальная позиция по Х и Y
    #show image_6 at left
    $ add_to_gallery("10", "10")  # Добавляем изображение в галерею
    p "Вот и конец одиннацатого класса... Как быстро пролетело время."
    p "Совсем скоро сдам экзамены и буду отдыхать!"
    p "Осталось только выбрать - куда поступать..?"
    
    # Первый выбор
    menu:
        "Поискать в интернете":
            jump go_to_internet
    
label go_to_internet:
    
    p "Так.. Посмотрим."
    p "Популярные ВУЗы Екатеринбурга..."

    # Второй выбор
    menu:
        "Уральский Государственный Горный Университе?":
            jump collect_uggu

label collect_uggu:
    
    p "Уральский Государственный Горный Университе? Инетресно..."
    p "Первый ВУЗ Урала - такая богатая история!"
    # Второй выбор
    menu:
        "Открыть сайт Уральского Государственного Горного Университета":
            jump read_uggu
    

label read_uggu:
    
    p "Посмотрим (можно выбрать оба варианта по очереди, начиная с первого):"
    menu:
        "Посмотреть проходные баллы":
            jump read_ball
        "Посмотреть направления обучения":
            jump read_napravlenie
    
label read_ball:
    
    p "Проходные баллы возросли по сравнению с прошлым годом("
    p "Ну.. ничего страшного. Я к экзаменам готовилась весь год - сдам хорошо!"
    
    jump read_uggu
    
label read_napravlenie:
    
    p "О, напрвление Информатика и вычислительная техника"
    p "Не зря так усердно готовилась к экзамену по информатике!"
    
    jump end_story
    
label end_story:
    
    p "Ну что, пора и к экзаменам приступать!"
    e "Эпизод закончен. Пора продолжить!"
    $ completed_episodes["episode_1"] = True
    $ renpy.save("story_2_progress")
    hide image_2
    hide image_1  
    jump episode_menu
    
label episode_2:
    if not completed_episodes["episode_1"]:
        e "Вы не можете начать Эпизод 2, пока не завершите Эпизод 1."
        jump episode_menu
    
    show image_6
    show image_5:
        xpos 0.5 ypos 0.1
    m "Ну что, моя хорошая? Уже решила куда будешь поступать?"
    hide image_5

    show image_1:
        xpos 0.0 ypos 0.2
    p "Ну... Дошла до финала - осталось 2 варианта:"
    p "Горный Университет и Институт связи."
    hide image_1
    
    show image_5:
        xpos 0.5 ypos 0.1
    m "И что же больше тебе по душе?"
    hide image_5

    p "Что же?"
    menu:
        "Уральский Государственный Горный Университет":
            jump gorny_uggu
        "Институт связи":
            jump svyas_inst

label gorny_uggu:
    p "Уральский Государственный Горный Университет"
    menu:
        "Отличный выбор!":
            jump end_story1

label svyas_inst:
    p "Институт связи"
    menu:
        "Отличный выбор!":
            jump end_story1

label end_story1:
    e "Эпизод закончен. Пора продолжить!"
    $ completed_episodes["episode_2"] = True
    $ renpy.save("story_3_progress")
    hide image_6
    jump episode_menu


label episode_3:
    if not completed_episodes["episode_2"]:
        e "Вы не можете начать Эпизод 3, пока не завершите Эпизод 2."
        jump episode_menu
    
    e "Вы начали Эпизод 3."
    e "Это начало вашей детективной истории."
    
    # Здесь будут действия и выборы для Эпизода 3
    e "Эпизод 3 завершен."
    
    # Устанавливаем флаг завершения эпизода
    $ completed_episodes["episode_3"] = True
    $ renpy.save("story_4_progress")
    
    jump episode_menu


label story_3:
    e "Вы выбрали Историю 3."
    # Добавьте будет код для истории 3
    e "Это начало Истории 3."
    e "История продолжается..."
    jump story_menu

    return