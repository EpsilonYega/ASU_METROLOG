class FIO:
    def __init__(self, surname, name, patronymic=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def get_full_name(self):
        if self.patronymic:
            return f"{self.surname} {self.name} {self.patronymic}"
        else:
            return f"{self.surname} {self.name}"

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_patronymic(self):
        return self.patronymic

    def set_patronymic(self, new_patronymic):
        self.patronymic = new_patronymic

    def print_info(self):
        print("Фамилия:", self.surname)
        print("Имя:", self.name)
        if self.patronymic:
            print("Отчество:", self.patronymic)