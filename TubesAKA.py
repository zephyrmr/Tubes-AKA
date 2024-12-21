import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Daftar produk sunscreen awal
sunscreens = [
    {"name": "Sunscreen A", "price": 100000.00, "quality_index": 4},
    {"name": "Sunscreen B", "price": 75000.00, "quality_index": 5},
    {"name": "Sunscreen C", "price": 150000.00, "quality_index": 3},
    {"name": "Sunscreen D", "price": 50000.00, "quality_index": 2},
    {"name": "Sunscreen E", "price": 75000.00, "quality_index": 1},
]

# Fungsi Bubble Sort Iteratif
def bubble_sort_iterative(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (data[j]["price"] > data[j + 1]["price"] or
               (data[j]["price"] == data[j + 1]["price"] and
                data[j]["quality_index"] < data[j + 1]["quality_index"])):
                data[j], data[j + 1] = data[j + 1], data[j]

# Fungsi Bubble Sort Rekursif
def bubble_sort_recursive(data, n=None):
    if n is None:
        n = len(data)
    if n == 1:
        return
    for i in range(n - 1):
        if (data[i]["price"] > data[i + 1]["price"] or
           (data[i]["price"] == data[i + 1]["price"] and
            data[i]["quality_index"] < data[i + 1]["quality_index"])):
            data[i], data[i + 1] = data[i + 1], data[i]
    bubble_sort_recursive(data, n - 1)

# Fungsi untuk mencetak tabel hasil
def print_table(data):
    table = PrettyTable()
    table.field_names = ["Rank", "Name", "Price (Rp)", "Quality Index"]
    for i, item in enumerate(data):
        table.add_row([i + 1, item["name"], f"Rp {item['price']:.2f}", item["quality_index"]])
    print(table)

# Fungsi untuk memperbarui grafik
def update_graph(n_values, iterative_times, recursive_times):
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, iterative_times, label="Iterative Bubble Sort", marker="o", linestyle="-", color="blue")
    plt.plot(n_values, recursive_times, label="Recursive Bubble Sort", marker="o", linestyle="-", color="orange")
    plt.title("Performance Comparison: Iterative vs Recursive Bubble Sort")
    plt.xlabel("Number of Products")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Program utama
n_values = []
iterative_times = []
recursive_times = []

while True:
    try:
        # Input jumlah produk
        n = int(input("Masukkan jumlah produk untuk ditampilkan (atau ketik -1 untuk keluar): "))
        if n == -1:
            print("Program selesai. Terima kasih!")
            break
        if n <= 0 or n > len(sunscreens):
            print("Masukkan jumlah produk yang valid!")
            continue

        # Batasi data yang akan diurutkan
        data_to_sort = sunscreens[:n]

        # Ukur waktu untuk Bubble Sort Iteratif
        iterative_data = data_to_sort.copy()
        start_time = time.perf_counter()
        bubble_sort_iterative(iterative_data)
        iterative_time = time.perf_counter() - start_time
        iterative_times.append(iterative_time)

        # Ukur waktu untuk Bubble Sort Rekursif
        recursive_data = data_to_sort.copy()
        start_time = time.perf_counter()
        bubble_sort_recursive(recursive_data)
        recursive_time = time.perf_counter() - start_time
        recursive_times.append(recursive_time)

        # Tambahkan jumlah data ke daftar
        n_values.append(n)

        # Tampilkan hasil rekomendasi (satu tabel saja, karena hasilnya sama)
        print("\nRekomendasi Produk:")
        print_table(iterative_data)
        print(f"Waktu eksekusi iteratif: {iterative_time:.8f} detik")
        print(f"Waktu eksekusi rekursif: {recursive_time:.8f} detik")

        # Perbarui grafik
        update_graph(n_values, iterative_times, recursive_times)

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
