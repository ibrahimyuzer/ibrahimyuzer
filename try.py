try:
    a = int(input("Bir sayı giriniz: "))
    b = int(input("İkinci bir sayı giriniz: "))
    print(a/b)

except ValueError:
    print("Hata")
except ZeroDivisionError:
    print("0 olamaz")

finally:
    print("Bir deneme")


def hosgeldin(isim):
    if (type(isim) != str):
        raise ValueError("Hata")
    else:
        print("Hoşgeldin",isim)

print(hosgeldin("bunyad"))
