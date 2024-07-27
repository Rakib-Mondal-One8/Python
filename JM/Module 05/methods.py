def call():
    print("calling someone")
    return 'call done'
class phone:
    price = 21000
    color = 'black'
    brand = 'samsung'
    features = ['camera','speaker','hammer']

    def call(self): # it is called method
        print('call one person')
    def send_sms(self,phone,sms):
        text = f'send sms to : {phone} and message : {sms}'
        return text


my_phone = phone()
print(my_phone.features)
my_phone.call()
res = my_phone.send_sms(9832760260,'I forgot to miss you')
print(res)