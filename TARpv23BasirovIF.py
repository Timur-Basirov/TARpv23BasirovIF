#from ipaddress import summarize_address_range
#from random import *
##Juku läheb kinno  # 1                                                                            
#Eesnimi=input("Mis on sinu nimi? ").capitalize()
#print("Tere, ",Eesnimi)
#if Eesnimi=="Juku":
#    print("Lahme kinno!!!")
#    vanus=int(input("Kui vana sa oled?"))
#    if vanus<0 or vanus>100:
#        pilet="vale vanus"
#    elif vanus<6:
#        pilet="tasuta pilet"
#    elif vanus<=14:
#        pilet="lastepilet"
#    elif vanus<=65:
#        pilet="täispilet"
#    elif vanus<=100:
#        pilet="sooduspilet"
#    print(pilet) #Ilus vastus ja õige vastus
#else:
#    print("Ma ootan Jukut")

#print ()
##2
#a1=input("nimetage üks sõber ")
#a2=input("nimetage veel üks sõber ")
#print(a1,"ja",a2,"nad on täna pinginaabrid")

##3
#length=float(input("ruumi pikkus meetrites: "))
#width=float(input("ruumi laius meetrites: "))
#P=2*(length+width)
#print("Teie põranda pindala: ")
#answer=input("Kas soovite oma põrandat renoveerida?",)
#answer=answer.lower
#if answer=="jah":
#    x1=input("Kui palju maksab üks ruutmeeter?")
#    price=P*x1
#    print("põranda asendamine maksab",x1)
#else:
#    print("Okei.")
#print()


    

#from datetime import *
#from random import *
##poes
#arve_nr= date.today()
#print (arve_nr)
#tsekk="arve: "+str(arve_nr)+"Toode hing kogus summa"
#summa=0

#toode="piim"
#hind=randint(50,100)/100
#v=input("Toode: "+toode+"Hind: "+str(hind)+"\nKas tahad osta?").lower
#if v=="jah":
#    mitu=int(input("Mitu? "))
#    tsekk=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#toode="Leib"
#hind=randint(50,100)/100
#v=input("Toode: "+toode+"Hind: "+str(hind)+"\nKas tahad osta?").lower
#if v=="jah":
#    mitu=int(input("Mitu? "))
#    tsekk=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#toode="Kommid"
#hind=randint(50,100)/100
#v=input("Toode: "+toode+"Hind: "+str(hind)+"\nKas tahad osta?").lower
#if v=="jah":
#    mitu=int(input("Mitu? "))
#    tsekk=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#raha=float(input("Maksa "+str(summa)))
#if raha==summa:
#    print("Tänan ostu eest!")
#elif raha>summa:
#    print("Tänan ostu eest! Tagasi"+str(raha-summa))
#else:
#    print("Maksa veel"+str(summa-raha))




#print()
#from datetime import *
#from random import *
##8.2poes
#arve_nr= date.today()
#print (arve_nr)
#tsekk="arve: "+str(arve_nr)+"\nToode hing kogus summa\n"
#summa=0
#for toode in ["Piim","Leib","Komm"]:
#    hind=randint(50,100)/100       
#    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
#    if v=="jah":
#        mitu=int(input("Mitu?"))
#        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#        summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#while True:
#    raha=float(input("Maksa "+str(summa)))
#    if raha==summa:
#        print("Tänan ostu eest!")
#        break
#    elif raha>summa:
#        print("Tänan ostu eest! Tagasi"+str(raha-summa))
#        break
#    else:
#        summa-=raha
#        print("Maksa veel"+str(summa))






# protsent=randint(-100,500) #0-100 0-60-"2", 61-75-"3", 76-89-"4", 90-100-"5"
# print(protsent, "% on testi tulemus")
# if protsent<0 or protsent>100:
#     tulemus="valed andmed"
# elif 0<=protsent<60: #protsent>0 and protsent<60, protsent<60,
#     tulemus="hinne 2"
# elif 60<=protsent<75:
#     tulemus="hinne 3"
# elif 75<=protsent<90:
#     tulemus="hinne 4"
# else:
#     tulemus="hinne 5"
# print (tulemus)
# print()






# arv=randint(0,100) #Juhuslik täisarv vahemikust 0..100
# print(arv)
# if arv%2==0:
#     print(arv,"on paaris arv")
# else:
#     print(arv,"on paaritud arv")
# print()




# print("tund on alanud")
# hilinemine=input("Kas õpilane on hilinenud ")
# # "JAH"-a.upper(), "Jah"-a.capitalize(), "jah"-a.lower()
# if hilinemine.capitalize()=="Jah":
#     print("Õpiane ootab 30 min")
# print("Õpilane astub klassi")

#from datetime import*
#from random import*
##11
#ta=date.today().year
#sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev"))).year
#if (ta-sp)%5==0:
#    print("Juubell")
#else:
#    print("Tavaline sünnipäev")

from datetime import*
from random import*
#14
maht=int(input("Bussi maht: "))
i=int(input("Inimeste arv: "))
ba=i/maht
if i%maht!=0:
    ba+=1
vb=i%maht
print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))

