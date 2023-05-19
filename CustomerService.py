class CustomerService:
    def __init__(self):
        self.calls = []

    def add_call(self, call_date, call_info):
        self.calls.append((call_date, call_info))

    def get_last_call_date(self):
        if self.calls:
            return self.calls[-1][0]
        else:
            return None

    def get_call_info(self, call_date):
        for call in self.calls:
            if call[0] == call_date:
                return call[1]
        return None