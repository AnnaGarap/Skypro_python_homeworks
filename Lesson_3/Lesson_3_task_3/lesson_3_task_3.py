from address import Address
from mailing import Mailing

to_address = Address("249030", "Обнинск", "Курчатова", "1", "1")
from_address = Address("119180", "Москва", "Большая Полянка", "3/9", "50")
mailing = Mailing(to_address, from_address, 350, "150748986449879")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
