import pandas as pd

from datetime import datetime
from Client import Client
from Address import Address
from FIO import FIO

class Controller():
    def __init__(self):
        self._client = []
    #Метод/ы для загрузки данных
    def load_excel(self, path):
        #Для считывания файлов из excel используется библиотека pandas
        #Не забудьте поставить пакет openpyxl!
        df = pd.read_excel(path)
        print(df)

    #методы манипуляции с информацией о пользователе
    #get и set методы
    def get_address(self, id):
        return self._client[id].address
    def set_address(self, id, city, district, street, house_number, entrance_number, apartment_number, house_type,
                    entrance_count):
        self._client[id].address = Address(city, district, street, house_number, entrance_number, apartment_number, house_type, entrance_count)
    def get_verification_list(self, id):
        return self._client[id].verification_list
    def set_verification_list(self, id, verification_list):
        self._client[id].verification_list = verification_list
    def get_FIO(self, id):
        return self._client[id].FIO
    def set_FIO(self, id, surname, name, patronymic):
        self._client[id].FIO = FIO(surname, name, patronymic)
    def insert_client_data(self, city, district, street, house_number, entrance_number, apartment_number, house_type, entrance_count, verification_list, device_count, phone_number, surname, name, patronymic, servicing_company):
        clientAddress = Address(city, district, street, house_number, entrance_number, apartment_number, house_type, entrance_count)
        clientVerificationList = verification_list
        clientFIO = FIO(surname, name, patronymic)
        self._client.append(Client(clientAddress, clientVerificationList, device_count, phone_number, clientFIO, servicing_company))
    def update_client_data(self, id, city, district, street, house_number, entrance_number, apartment_number, house_type, entrance_count, verification_list, device_count, phone_number, surname, name, patronymic, servicing_company):
        clientAddress = Address(city, district, street, house_number, entrance_number, apartment_number, house_type,
                                entrance_count)
        clientVerificationList = verification_list
        clientFIO = FIO(surname, name, patronymic)

        self._client[id].address = clientAddress
        self._client[id].verification_list = clientVerificationList
        self._client[id].device_count = device_count
        self._client[id].phone_number = phone_number
        self._client[id].FIO = clientFIO
        self._client[id].servicing_company = servicing_company
    def delete_client_data(self, id):
        #запрос к модели для удаления данных клиента
        self._client.pop(id)

    #Методы вывода данных о клиенте на основе входящих параметров
    def output_data_by_address(self, id, address):
        clientAddress = self._client[id].address.show_full_address()
        if address in clientAddress:
            self._client[id].print_info()
        else:
            print('Совпадений по указанному адресу не нашлось.')
    def output_data_by_phone_number(self, id, number):
        if number == self._client[id].phone_number:
            self._client[id].print_info()
        else:
            print('Совпадений по указанному номеру не нашлось.')
    def output_data_by_FIO(self, id, FIO):
        clientName = self._client[id].FIO.get_full_name()
        if FIO in clientName:
            self._client[id].print_info()
        else:
            print('Совпадений по указанному ФИО не нашлось.')

    def show_client_list(self):
        for i in range(len(self._client)):
            print(f'Клиент {i+1}: (id = {i})')
            self._client[i].print_info()
            print()

    #Методы сортировки данных о клиентах на основе входящих параметров
    def sort_by_month(self):
        return
    def sort_by_address(self):
        return
    def sort_by_district(self):
        return
    def sort_by_company_name(self):
        return

    #Напоминание в зависимости от числа дней
    def notification(self, day):
        return


vlist = [datetime.strptime('09/03/22 13:55:26', '%m/%d/%y %H:%M:%S'), datetime.strptime('05/10/23 14:16:21', '%m/%d/%y %H:%M:%S'),datetime.strptime('05/18/23 17:21:06', '%m/%d/%y %H:%M:%S')]
controller = Controller()
controller.insert_client_data('Ростов-на-Дону', 'Ворошиловский', 'Мечникова', 79, 1, 203, 'Общежитие', 1, vlist, 25, '+79891233424', 'Орлов','Владислав','Сергеевич', 'ТСЖ метеор')
controller.insert_client_data('Ростов-на-Дону', 'Ворошиловский', 'Мечникова', 79, 1, 204, 'Общежитие', 1, vlist, 25, '+79891233425', 'Бабаян>','Бибизян','Макакович', 'ТСЖ метеор')
controller.show_client_list()
