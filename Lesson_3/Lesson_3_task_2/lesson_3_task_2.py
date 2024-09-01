from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Xiaomi", "Redmi 13", "+79065555555")
phone2 = Smartphone("Sumsung", "Galaxy A12", "+79101111111")
phone3 = Smartphone("Apple", "IPhone 14", "+79601213141")
phone4 = Smartphone("Huawei", "Pura 70", "+79305468912")
phone5 = Smartphone("Honor", "200 PRO", "+79201593575")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"""{phone.phone_brand} - {phone.phone_model}. "
    f"{phone.subscriber_number}""")
