import tkinter


# board

window = tkinter.Tk()
window.minsize(width=200, height=200)
window.title("Vücut Kitle Endeksi Hesaplayıcı")
window.config(background="#E3D7CB")

# ui

label = tkinter.Label(text="VKİ Hesaplayıcı")
label.config(bg="#E3D7CB", fg="black")
label.pack()


label_2 = tkinter.Label()
label_2.config(bg="#E3D7CB",fg="#E3D7CB")
label_2.pack()

"""
<18.5        zayıf
18.5-24.9    normal
25-29.9      kilolu
30-34.9      obez 1.sınıf
35-39.9      obez 2.sınıf
>40          Aşırı obez

"""

# functions


def bmi_sonuc():
    kilo = entry_weight.get()
    boy = entry_height.get()

    if kilo == "" or boy == "":
        label_bmi.config(text="Lütfen boyunuzu ve kilonuzu giriniz!!! ")
    else:
        try:
            bmi = float(kilo) / ((float(boy)/100) ** 2)
            sonuç_metni = sonuç_yazdırma(bmi)
            label_bmi.config(text=sonuç_metni)
        except:
            pass
def sonuç_yazdırma(vki):
    sonuç_metni = f"VKİ'niz {round(vki, 2)}. "
    if vki <= 16:
        sonuç_metni += "Çok zayıfsınız."
    elif 16 < vki <= 17:
        sonuç_metni += "Biraz zayıfsınız."
    elif 17 < vki <= 18.5:
        sonuç_metni += "Zayıfsınız."
    elif 18.5 < vki <= 25:
        sonuç_metni += "Normal kilodasınız."
    elif 25 < vki <= 30:
        sonuç_metni += "Kilolusunuz."
    elif 30 < vki <= 35:
        sonuç_metni += "1. sınıf obezsiniz."
    elif 35 < vki <= 40:
        sonuç_metni += "2. sınıf obezsiniz."
    else:
        sonuç_metni += "3. sınıf obezsiniz."
    return sonuç_metni

# weight entry
label_weight = tkinter.Label(text="Kilonuzu giriniz (kg):")
label_weight.pack()
entry_weight = tkinter.Entry(width=20)
entry_weight.pack()

# height entry
label_height = tkinter.Label(text="Boyunuzu giriniz (cm):")
label_height.pack()
entry_height = tkinter.Entry(width=20)
entry_height.pack()

entry_button = tkinter.Button(text="Hesapla", command=bmi_sonuc)
entry_button.pack()

label_3 = tkinter.Label()
label_3.config(bg="#E3D7CB",fg="#E3D7CB")
label_3.pack()

# bmi-vki hesaplama
label_bmi = tkinter.Label(text="Sonuç:", )
label_bmi.pack()







window.mainloop()