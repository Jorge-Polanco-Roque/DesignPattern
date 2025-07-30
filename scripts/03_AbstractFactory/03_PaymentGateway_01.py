from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount:float) -> str:
        pass


class CreditCard(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Credit Card")

class DebitCard(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Debit Card")

class Cash(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Cash")

################### PAYMENT FACTORY ###################

# create_payment se heredará al resto de sub-clases
class PaymentFactory(ABC):
    def create_payment(self, payment_method):
        if payment_method in self.payments:
            return self.payments.get(payment_method)()

class USPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, debit_Card=DebitCard, cash=Cash)

        
# Esta clase puede manejar diferentes formas de pago
class CanadaPaymentFactory(PaymentFactory):
    def _init__(self):
        self.payments = dict(credit_card=CreditCard, debit_Card=DebitCard)
    

class Client:
    def __init__(self):
        self.factory = None

    def get_factory(self):
        country_factory = dict(us=USPaymentFactory, canada=CanadaPaymentFactory)

        flist = " ,".join(country_factory)
        while not self.factory:
            country = input(f"Enter Country Payment ({flist}): ")

            if country in country_factory:
                self.factory = country_factory.get(country)()
                break
            print(f"You need to enter one of the countries listed ({flist})")

    def do_payment(self):
        if self.factory:
            amount = float(input("How much are you paying: "))
            available_payments = ", ".join(self.factory.payments)
            payment_method = input(f"Enter your payment method ({available_payments}): ")
            if payment_method in self.factory.payments:
                payment = self.factory.payments.get(payment_method)()
                payment.make_payment(amount)
            else:
                print(f"PAYMENT ERROR: You cannot use this type of payment")
        else:
            print(f"ERROR: Country Factory not properly created")

    def run_payments(self):
        self.get_factory()
        self.do_payment()

if __name__ == "__main__":
    client=Client()
    client.run_payments()



