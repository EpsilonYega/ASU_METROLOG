class Verification:
    def __init__(self, date, client, is_completed):
        self.date = date
        self.client = client
        self.is_completed = is_completed

    def set_verification_completed(self):
        self.is_completed = True

    def print_info(self):
        print("Date:", self.date.strftime("%d/%m/%Y"))
        print("Client:", self.client)
        print("Verification completed:", self.is_completed)