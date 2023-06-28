class CreditCard:
    def __init__(self, number: str, holder_name: str, cvv: str, expr_date: str, pin: str):
        self.number = number  # PUBLIC
        self.holder_name = holder_name
        self.cvv = cvv
        self.expr_date = expr_date
        self._pin = pin  # PROTECTED

    def get_pin(self):
        return self.__pin  # PRIVATE


class OnlineCreditCard(CreditCard):
    def __init__(self, number: str, holder_name: str, cvv: str, expr_date: str, pin: str):
        super().__init__(number, holder_name, cvv, expr_date, pin)


visa = CreditCard("4356767897121223", "Ivan Ivanov", "122", "11/11/2023", "1111")