from datetime import datetime
from модуль1 import*
while True:
    ik=input("Isikukood: ")
    if len(ik)==11:
        try:
            ik_list=list(ik) #ik_list["4","9","9"...,...]
            if int(ik_list[0]) in [1,2,3,4,5,6]:
                if int(ik_list[0]) in [1,2]:
                    a=1800
                elif int(ik_list[0]) in [3,4]:
                    a=1900
                else:
                    a=2000
                aasta=a+int(ik_list[1]+ik_list[2])
                kuu=int(ik_list[3]+ik_list[4])
                paev=int(ik_list[5]+ik_list[6])
                if datetime(aasta,kuu,paev):
                    vastus=Kontroll(ik)   #                 
                    if type(vastus)==int:
                        ik3=int(ik[7:10])
                        haigla=Haigla(ik3)
                        print(haigla)
                        sugu=Sugu(int(ik_list[0]))
                        print(sugu)
                    else:
                        print(vastus) #

            else:
                print("Esimene sümbol/arv on vale ")
        except:
            print("Andmetüüp on vale, On vaja numbreid sisestada")
    else:
        print("Sümbolite arv peab 11 olema ")
#50304273717