from datetime import datetime  # Импорт модуля datetime для проверки даты


class Date:
    def __init__(self, text):
        self.text = text

    @classmethod
    def my_m(cls, param):
        """Метод проверяет корректность введённых значений."""
        if all([i.isdigit() for i in param.split("-")]):
            return Date.valid(param)
        else:
            return f"{param} - Некорректная дата!"

    @staticmethod
    def valid(date):
        """Валидация даты. Проверяет есть ли такая дата в календаре через datetime."""
        try:
            valid_date = datetime.strptime(date, '%d-%m-%Y')
            return datetime.date(valid_date)
        except ValueError:
            return 'Такой даты нет!'


date = Date("25-03-2020")
print(date.my_m(date.text))
