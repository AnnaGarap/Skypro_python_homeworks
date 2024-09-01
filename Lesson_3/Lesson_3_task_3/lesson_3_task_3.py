from address import Address
from mailing import Mailing

to_address = Address("249030", "Обнинск", "Курчатова", "1", "1")
from_address = Address("119180", "Москва", "Большая Полянка", "3/9", "50")
mailing = Mailing(to_address, from_address, 350, "150748986449879")

<<<<<<< HEAD
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
=======
print(f"""Отправление {mailing.track} из {mailing.from_address.index}, "
>>>>>>> e151690edcff970734ef3693ec1b553a2df4f4aa
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
<<<<<<< HEAD
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
=======
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.""")
>>>>>>> e151690edcff970734ef3693ec1b553a2df4f4aa
