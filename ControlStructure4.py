def print_odd_numbers(n): #mendefinisikan untuk mencetak bilangan ganjil dimulai dari 1 sampai n
    for i in range(1, n+1): #memastikan angka yang ada 
        if i % 2 != 0:
            print(i, end=" ")

n = int(input("Masukkan batas bilangan ganjil: "))
print_odd_numbers(n)