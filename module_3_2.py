def send_email(masssage, recpitien, sender="university.help@gmail.com"):
    vaild_sender = sender.endswith((".com", ".ru", ".net")) and "@" in sender
    vaild_recpitien = recpitien.endswith((".com", ".ru", ".net")) and "@" in recpitien
    if not vaild_sender or not vaild_recpitien:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recpitien}")
    elif recpitien == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")
    else:
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
# recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию

# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".

# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"

# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:sender = "university.help@gmail.com".
# "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
#
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.
