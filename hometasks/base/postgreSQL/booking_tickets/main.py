import db
from datetime import datetime


def print_menu():
    print("Выберите нужную команду:")
    print("0. Выход")
    print("1. Показать список доступных ивентов")
    print("2. Добавить событие")
    print("3. Изменить событие")
    print("4. Удалить событие")
    print("5. Посмотреть доступные места ивента по ид")
    print("6. Забронировать место на ивент по ид")
    print("7. Отменить бронь билета на событие ID:")
    print("8. Поиск по имени события: ")


def app():
    db.init_db()
    print('Таблицы успешно созданы')

    print("Вас приветствует, IT онлайн школа!")
    while True:
        print_menu()
        cmd = int(input("Введите номер команды: "))
# ------------------------
        if cmd == 0:

            print("До скорой встречи!)")
            break
# ------------------------
        elif cmd == 1:

            print("=" * 20)
            print("Список ивентов:")
            events = db.get_all_events()
            for event in events:
                print(f"ID: {event[0]} - Название: {event[1]}. Время: {event[2]}")
            print("=" * 20)
# ------------------------
        elif cmd == 2:
            print("=" * 20)
            print("Добавление нового ивента:")
            title = input("Название фильма: ")
            date = input("Введите дату в формате год-месяц-день часы:минуты:секунды: ")
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                db.add_event(title, date_obj)
                print("Событие успешно создано!")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
            print("=" * 20)
# ------------------------
        elif cmd == 3:
            print("=" * 20)
            print("Изменение ивента по ID: ")
            ind = int(input("ID: "))

            title = input("Введите новое название (или Enter, чтобы оставить старое): ").strip()
            title = title if title else None

            answer = input("Надо менять дату? (Да/Нет): ").strip().lower()
            date = None
            if answer == 'да':
                date = input("Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ").strip()

            db.change_event(ind, title, date)
# ------------------------
        elif cmd == 4:
            print("=" * 20)
            print("Удаление ивента по ID: ")
            idd = int(input("ID: "))
            db.delete_event(idd)
            print("Список ивентов:")
            events = db.get_all_events()
            for event in events:
                print(f"ID: {event[0]} - Название: {event[1]}. Время: {event[2]}")
            print("=" * 20)
# ------------------------
        elif cmd == 5:
            print("=" * 20)
            print("Посмотреть свободные места на события по ID: ")
            idd = int(input("ID: "))
            seats = db.get_seats(idd)
            print(f'Всего свободно мест на это событие {len(seats)}')
            print('↓'* 20)
            for seat in seats:
                print(f'ряд -> {seat[1]}  номер -> {seat[2]}')
# ------------------------
        elif cmd == 6:
            print("=" * 20)
            print("Забронировать место на событие 'ID': ")
            event_id = int(input(" Event ID: "))
            row_number = int(input('Какой ряд?'))
            seat_number = int(input('Какое место?'))

            db.book_seat(row_number, seat_number, event_id)
# ------------------------
        elif cmd == 7:
            print("=" * 20)
            print('Отменить бронь билета на событие ID: ')
            event_id = int(input(" Event ID: "))
            row_number = int(input('Какой ряд?'))
            seat_number = int(input('Какое место?'))

            db.unbook_seat(row_number, seat_number, event_id)
# ------------------------
        elif cmd == 8:
            print("=" * 20)
            print('Поиск ивента по названию :')
            title = input('Введите название или первые буквы названия: ')
            events = db.search_event(title)
            if not events:
                print("События не найдены.")
            else:
                for event in events:
                    print(f" Название {event[1]} время {event[2]}")

        else:
            print("Вы ввели несуществующею команду. Попробуйте еще раз!")



app()