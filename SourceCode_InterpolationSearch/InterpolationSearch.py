def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Hitung posisi perkiraan menggunakan rumus interpolasi
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        # Jika elemen ditemukan di posisi yang diperkirakan
        if arr[pos] == target:
            return pos
        
        # Jika target lebih besar, cari di bagian kanan
        if arr[pos] < target:
            low = pos + 1
        # Jika target lebih kecil, cari di bagian kiri
        else:
            high = pos - 1

    return -1  # Elemen tidak ditemukan


# Contoh Penggunaan
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 110

result = interpolation_search(arr, target)

if result != -1:
    print(f"Elemen {target} ditemukan di indeks {result}")
else:
    print(f"Elemen {target} tidak ditemukan dalam array")
