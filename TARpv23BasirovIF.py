from random import *
#Juku läheb kinno  # 1                                                                            
Eesnimi=input("Mis on sinu nimi? ").capitalize()
print("Tere, ",Eesnimi)
if Eesnimi=="Juku":
    print("Lahme kinno!!!")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14:
        pilet="lastepilet"
    elif vanus<=65:
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) #Ilus vastus ja õige vastus
else:
    print("Ma ootan Jukut")

print ()
#2
a1=input("nimetage üks sõber ")
a2=input("nimetage veel üks sõber ")
print(a1,"ja",a2,"nad on täna pinginaabrid")

#3
length=float(input("ruumi pikkus meetrites: "))
width=float(input("ruumi laius meetrites: "))
P=2*(length+width)
print("Teie põranda pindala: ")
answer=input("Kas soovite oma põrandat renoveerida?",)
answer=answer.lower
if answer=="jah":
    x1=input("Kui palju maksab üks ruutmeeter?")
    price=P*x1
    print("põranda asendamine maksab",x1)
else:
    print("Okei.")
print()


    









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