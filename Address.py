class Address:
    def __init__(self, city, district, street, house_number, entrance_number, apartment_number, house_type,
                 entrance_count):
        self.city = city
        self.district = district
        self.street = street
        self.house_number = house_number
        self.entrance_number = entrance_number
        self.apartment_number = apartment_number
        self.house_type = house_type
        self.entrance_count = entrance_count

    def show_full_address(self):
        return f"{self.city}, {self.district}, {self.street}, {self.house_number}, {self.entrance_number}, {self.apartment_number}"

    def get_city(self):
        return self.city

    def set_city(self, new_city):
        self.city = new_city

    def get_district(self):
        return self.district

    def set_district(self, new_district):
        self.district = new_district

    def get_street(self):
        return self.street

    def set_street(self, new_street):
        self.street = new_street

    def get_house_number(self):
        return self.house_number

    def set_house_number(self, new_house_number):
        self.house_number = new_house_number

    def get_entrance_number(self):
        return self.entrance_number

    def set_entrance_number(self, new_entrance_number):
        self.entrance_number = new_entrance_number

    def get_apartment_number(self):
        return self.apartment_number

    def set_apartment_number(self, new_apartment_number):
        self.apartment_number = new_apartment_number

    def get_house_type(self):
        return self.house_type

    def set_house_type(self, new_house_type):
        self.house_type = new_house_type

    def get_entrance_count(self):
        return self.entrance_count

    def set_entrance_count(self, new_entrance_count):
        self.entrance_count = new_entrance_count

    def print_info(self):
        print("Город:", self.city)
        print("Район:", self.district)
        print("Улица:", self.street)
        print("Номер дома:", self.house_number)
        print("Номер подъезда:", self.entrance_number)
        print("Номер квартиры:", self.apartment_number)
        print("Тип дома:", self.house_type)
        print("Количество подъездов:", self.entrance_count)