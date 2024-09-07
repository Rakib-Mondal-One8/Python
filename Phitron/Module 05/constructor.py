class Phone:
    manufec : 'India'

    def __init__(self, owner,brand,price): # Constructor of python
        self.owner = owner
        self.brand = brand
        self.price = price
    def send_sms(self,phone,sms):
        text = f'sending to : {phone} {sms}'
        print(text)

my_phone = Phone('Rakib','Realme',22000)
print(my_phone.owner, my_phone.brand, my_phone.price)

my_phone.send_sms('1234','1234') 