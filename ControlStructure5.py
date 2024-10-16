def print_pattern(n): #mencetak bola sesuai atau sampai n
    for i in range(1, n+1): #perulangan rentang angkanya sampai ke n
        print(f"{i}"*i) #mencetak nilai yang ditulis sebanyak nilainya, jadi misal 7, akan muncul 7 angka.

n = int(input("Masukkan nilai n:")) #Menerima angka yang akan dimasukkan
print_pattern(n) #memanggil fungsi agar tercetak pola dengan jumlah baris yang sesuai dengan nilai n, jadi jika memasukkan n yaitu 10, maka akan 