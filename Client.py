class Client:
    def __init__(self, address, verification_list, device_count, phone_number, full_name, servicing_company):
        self.address = address
        self.verification_list = verification_list
        self.device_count = device_count
        self.phone_number = phone_number
        self.full_name = full_name
        self.servicing_company = servicing_company

    def check_address_duplicate(self, new_address):
        if self.address == new_address:
            return True
        else:
            return False

    def get_address(self):
        return self.address

    def set_address(self, new_address):
        self.address = new_address

    def get_verification_list(self):
        return self.verification_list

    def set_verification_list(self, new_verification_list):
        self.verification_list = new_verification_list

    def get_device_count(self):
        return self.device_count

    def set_device_count(self, new_device_count):
        self.device_count = new_device_count

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, new_full_name):
        self.full_name = new_full_name

    def get_servicing_company(self):
        return self.servicing_company

    def set_servicing_company(self, new_servicing_company):
        self.servicing_company = new_servicing_company

    def print_info(self):
        print("Адрес:", self.address.show_full_address())
        print("Список поверок:", self.verification_list)
        print("Количество приборов:", self.device_count)
        print("Телефон клиента:", self.phone_number)
        print("ФИО клиента:", self.full_name)
        print("Название обслуживающей дом организации:", self.servicing_company)