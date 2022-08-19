sayi = int(input("Test etmek istediğiniz sayıyı giriniz: "))
oz_carpan = 0

def mukemmel_sayi_kontrolu(sayi , oz_carpan):
    for i in range(1, sayi):
        if(sayi % i == 0):
            oz_carpan = oz_carpan + i
    if (oz_carpan == sayi):
        print("Girdiğiniz sayı mükemmel sayıdır.")
    else:
        print("Girdiğiniz sayı mükemmel sayı değildir.")
        
mukemmel_sayi_kontrolu(sayi,oz_carpan)