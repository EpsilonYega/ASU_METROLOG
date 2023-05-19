class DiscountSystem:
    def __init__(self, start_date, end_date, discount, conditions, current_price):
        self.start_date = start_date
        self.end_date = end_date
        self.discount = discount
        self.conditions = conditions
        self.current_price = current_price

    def get_start_date(self):
        return self.start_date

    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def get_conditions(self):
        return self.conditions

    def set_conditions(self, conditions):
        self.conditions = conditions

    def get_current_price(self):
        return self.current_price

    def set_current_price(self, current_price):
        self.current_price = current_price

    def print_info(self):
        print("Start date:", self.start_date)
        print("End date:", self.end_date)
        print("Discount:", self.discount)
        print("Conditions:", self.conditions)
        print("Current price:", self.current_price)