#1-misol
def kafe_buyurtma(kofe):
    if kofe == "espresso":
        return "Tez tayyor, 2 daqiqa!"
    elif kofe == "latte":
        return "San’atli naqsh qo‘shilsinmi?"
    else:
        return "Oddiy kofe, shakar qo‘yasizmi?"

#2-misol
def tinder_tekshiruv(soz_soni):
    if soz_soni < 50:
        return "Bu nimasi, jiddiy emas!"
    elif 50 <= soz_soni <= 100:
        return "Yaxshi, lekin yanada qiziqroq qil!"
    else:
        return "Vau, roman yozdingizmi?"

#3-misol
def daraja(tajriba):
    if tajriba == "yangi":
        return "Oson rejim, qo‘rqma!"
    elif tajriba == "o‘rtacha":
        return "Normal rejim, sinovdan o‘tasan!"
    elif tajriba == "professional":
        return "Hardkor rejim, tayyor bo‘l!"
