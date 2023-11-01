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

for i, pizza in enumerate(pizzas):
    print(f"{i+1}. {pizza}")
topping_pizza = toppings_pizza[int(input("Pilih Topping Pizza: ")) - 1]
print()
for i, crust in enumerate(crusts_pizza):
    print(f"{i+1}. {crust}")
crust_pizza = [*crusts_pizza.keys()][int(input("Pilih Crust/Tepian Pizza: ")) - 1]
print()
for i, size in enumerate(extra_cheese):
    print(f"{i+1}. {size}")
size_pizza = [*extra_cheese.keys()][int(input("Pilih Ukuran Pizza: ")) - 1]
print()
extra_cheese = True if input("Pakai Tambahan Keju (y/n): ").lower() == "y" else False

pizza = pizzas[topping_pizza][crust_pizza][size_pizza]
total_harga = pizza["price"]
if extra_cheese: total_harga += pizza["extra_cheese"]

print("\nTerima Kasih telah membeli Pizza di Pizza Hut")
print(f"Pesanan Anda Pizza dengan Topping {topping_pizza}")
print(f"Crust/Pinggiran {crust_pizza}")
print(f"Ukuran {size_pizza} dan")
print(f"{'dengan' if extra_cheese else 'tanpa'} Tambahan Keju")
print(f"Total Harga: Rp {total_harga}")
