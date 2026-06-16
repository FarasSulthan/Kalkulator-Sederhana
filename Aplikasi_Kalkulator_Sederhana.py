#Fungsi Penjumlahan 
def tambah (x,y):
    return x + y 

#Fungsi Pengurangan 
def Kurang (x,y):
    return x - y 

#fungsi perkalian
def kali (x,y):
    return x * y

#fungsi pembagian
def bagi (x,y):
    return x / y

def menu ():
#Menu Operasi 
    print ("pilih operasi")
    print ("1.Jumlah")
    print ("2.Kurang")
    print ("3.Kali")
    print("4.Bagi")

def kalkulator():
    menu()
    #Meminta input dari pengguna 
pilihan = input("Masukan pilihan operasi (1/2/3/4) : ")

if pilihan =='1':
    bilangan1 = int(input("Masukan bilangan pertama: "))
    bilangan2 = int(input("Masukan bilangan kedua: "))
    print(bilangan1,"+",bilangan2,"=",tambah (bilangan1,bilangan2))
    
elif pilihan =='2':
    bilangan1 = int(input("Masukan bilangan pertama: "))
    bilangan2 = int(input("Masukan bilangan kedua: "))
    print (bilangan1,"-",bilangan2,"=", Kurang(bilangan1,bilangan2))
elif pilihan == '3':
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    print(bilangan1,"*",bilangan2,"*",kali(bilangan1,bilangan2))    
elif pilihan == '4':
    bilangan1 = int(input("Masukkan bilangan pertama: "))
    bilangan2 = int(input("Masukkan bilangan kedua: "))
    print(bilangan1,"/",bilangan2,"/",bagi(bilangan1,bilangan2))
else:
    print("Input salah")