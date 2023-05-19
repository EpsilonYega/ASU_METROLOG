import pandas as pd
class Controller():
    def __init__(self, client):
        self.client = client
    #Метод/ы для загрузки данных
    def load_excel(self, path):
        #Для считывания файлов из excel используется библиотека pandas
        #Не забудьте поставить пакет openpyxl!
        df = pd.read_excel(path)
        print(df)

    #методы манипуляции с информацией о пользователе
    def insert_client_data(self, client):
        #запрос к БД для вставки данных клиента
        return
    def update_client_data(self, client):
        #запрос к БД для обновления данных клиента
        return
    def delete_client_data(self):
        #запрос к БД для удаления данных клиента
        return

    #Методы вывода данных о клиенте на основе входящих параметров
    def output_data_by_address(self, address):
        clientAddress = self.client.address.show_full_address()
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
        clientName = self.client.get_full_name()
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

from datetime import datetime
from Client import Client
from Address import Address


address1 = Address('Ростов-на-Дону', 'Ворошиловский', 'Мечникова', 79, 1, 203, 'Общежитие', '')
list1 = [datetime.strptime('09/03/22 13:55:26', '%m/%d/%y %H:%M:%S'), datetime.strptime('05/10/23 14:16:21', '%m/%d/%y %H:%M:%S'),datetime.strptime('05/18/23 17:21:06', '%m/%d/%y %H:%M:%S')]
client1 = Client(address1, list, 25, '+79891233424', 'Орлов Владислав Сергеевич', 'ТСЖ метеор')
controller = Controller(client1)