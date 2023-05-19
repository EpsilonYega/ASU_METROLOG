class Call:
    def __init__(self, call_date, incoming, result, discount_system, manager):
        self.call_date = call_date
        self.incoming = incoming
        self.result = result
        self.discount_system = discount_system
        self.manager = manager

    def get_call_date(self):
        return self.call_date

    def set_call_date(self, call_date):
        self.call_date = call_date

    def is_incoming(self):
        return self.incoming

    def set_incoming(self, incoming):
        self.incoming = incoming

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def get_discount_system(self):
        return self.discount_system

    def set_discount_system(self, discount_system):
        self.discount_system = discount_system

    def get_manager(self):
        return self.manager

    def set_manager(self, manager):
        self.manager = manager

    def print_info(self):
        print("Call date:", self.call_date)
        print("Incoming:", self.incoming)
        print("Result:", self.result)
        print("Discount system:", self.discount_system)
        print("Manager:", self.manager)