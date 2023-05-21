import pandas as pd

from datetime import datetime
from Client import Client
from Address import Address
from FIO import FIO

class Controller():
    def __init__(self):
        self._address = None
        self._verification_list = None
        self._FIO = None
        self._client = None
    #Метод/ы для загрузки данных
    def load_excel(self, path):
        #Для считывания файлов из excel используется библиотека pandas
        #Не забудьте поставить пакет openpyxl!
        df = pd.read_excel(path)
        print(df)

    #методы манипуляции с информацией о пользователе
    def get_address(self):
        if self._address is not None:
            return self._address
        return 'На данный момент адрес не указан'
    def set_address(self, city, district, street, house_number, entrance_number, apartment_number, house_type,
                    entrance_count):
        self._address = Address(city, district, street, house_number, entrance_number, apartment_number, house_type, entrance_count)
    def get_verification_list(self):
        return self._verification_list
    def set_verification_list(self, verification_list):
        self._verification_list = verification_list
    def get_FIO(self):
        return self._FIO
    def set_FIO(self, surname, name, patronymic):
        self._FIO = FIO(surname, name, patronymic)
    def insert_client_data(self, device_count, phone_number, servicing_company):
        self.client = Client(self._address, self._verification_list, device_count, phone_number, self._FIO, servicing_company)
    def update_client_data(self, client, address, verification_list, device_count, phone_number, full_name, servicing_company):
        client.set_full_name(full_name)
        client.set_phone_number(phone_number)
        client.set_address(address)
        client.set_device_count(device_count)
        client.set_servicing_company(servicing_company)
        client.set_verification_list(verification_list)
        return
    def delete_client_data(self):
        #запрос к модели для удаления данных клиента
        return

    #Методы вывода данных о клиенте на основе входящих параметров
    def output_data_by_address(self, address):
        clientAddress = self._address.show_full_address()
        if address in clientAddress:
            self.client.print_info()
        else:
            print('Совпадений по указанному адресу не нашлось.')
    def output_data_by_phone_number(self, number):
        if number == self.client.phone_number:
            self.client.print_info()
        else:
            print('Совпадений по указанному номеру не нашлось.')
    def output_data_by_FIO(self, FIO):
        clientName = self._FIO.get_full_name()
        if FIO in clientName:
            self.client.print_info()
        else:
            print('Совпадений по указанному ФИО не нашлось.')

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
controller.set_address('Ростов-на-Дону', 'Ворошиловский', 'Мечникова', 79, 1, 203, 'Общежитие', 1)
controller.set_verification_list(vlist)
controller.set_FIO('Орлов','Владислав','Сергеевич')
controller.insert_client_data(25, '+79891233424', 'ТСЖ метеор')