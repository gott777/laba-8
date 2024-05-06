import random

def computer_question():
    questions = [
        "Что делаешь?",
        "Ты видел последний фильм про котиков?",
        "Как прошел твой день?",
        "Какое твое любимое блюдо?",
        "Что ты думаешь о космосе?",
        "Сколько звезд на небе ты смог бы сосчитать?",
        "Какие фильмы ты любишь смотреть?",
        "Как тебе погода сегодня?",
        "Какая твоя любимая книга?",
        "Что тебе снилось на прошлой неделе?"
    ]
    return random.choice(questions)

def computer_answers():
    questions = [
        "Не люблю шоколад",
        "99 копеек",
        "Марс назодится в Албании",
        "Я не осьминог у меня 3 юзб порта",
        "Мое имя не Джохабар Мурабиби",
        "Плутон не планета",
        "Тридцать пять",
        "Я выращиваю гипсофилы",
        "Я не видел здесь кошку",
        "Я вижу"
    ]
    return random.choice(questions)

def player_question():
    return input("Твой вопрос: ")

def play():
    computer_score = 0
    player_score = 0
    turns = 10

    print("Давай поиграем в Мячик-вопросик!")

    for turn in range(turns):
        r = random.randint(1,10)
        print("\nХод", turn + 1)
        print("Компьютер бросает мячик...")
        if r <= 7:
            player_score += 1
            print('Бросок, вы помали мяч')
            print('Вопрос : '+computer_question())
            yourAnswer = str(input('Ответ : '))
            print('Вы бросаете мяч:')
        else:
            computer_score += 1
            print('Бросок, вы не помайли мяч')
            question = str(input('Вопрос : '))
            print('Ответ компьютера : '+computer_answers())
    print("Результаты:")
    print("Твои очки:", player_score)
    print("Очки компьютера:", computer_score)
play()