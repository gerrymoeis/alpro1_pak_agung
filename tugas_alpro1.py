"""
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
    Kelompok: 1

    Nama Anggota:
    1. Gerry Moeis M.D.P - 23091397164
    2. M. Faiz Noer Rizky - 23091397147
    3. Dea Ayu Novita Putri - 23091397173
"""

toppings_pizza = ["Frankfurter BBQ", "Meat Monsta", "Super Supreme", "Super Supreme Chicken"]
crusts_pizza = {
    "Pan": {
        "Personal": 43_637,
        "Regular": 100_910,
        "Large": 132_728
    },
    "StuffedCrust Cheese": {
        "Personal": 55_455,
        "Regular": 120_910,
        "Large": 160_000
    },
    "StuffedCrust Sausage": {
        "Personal": 52_728,
        "Regular": 117_273,
        "Large": 155_455
    },
    "Cheesy Bites": {
        "Personal": 57_273,
        "Regular": 123_637,
        "Large": 164_546
    },
    "Crown Crust": {
        "Personal": 55_455,
        "Regular": 120_910,
        "Large": 160_000
    }
}
extra_cheese = {
    "Personal": 13_636,
    "Regular": 16_364,
    "Large": 19_091
}

pizzas = {}
for crust in crusts_pizza:
    for size, cheese_price in extra_cheese.items():
        crust_price = crusts_pizza[crust][size]
        crusts_pizza[crust][size] = {"extra_cheese": cheese_price, "price": crust_price}
for topping in toppings_pizza:
    pizzas[topping] = crusts_pizza
