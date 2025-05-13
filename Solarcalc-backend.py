#Energy solution helper
import random
import time

range_list = range(0,99999999)
#Årlig förbrukning per månad baserat på snitt

first_input =input ("Vet du kunds förbrukning månadsvis? Ja/Nej \n")
if first_input != "ja".title():
    user_input = int(input("Okej, vad har kund för årsförbrukning?\n"))    
    annual_consumption = user_input
    january_cons =  annual_consumption * 0.14
    february_cons =  annual_consumption *0.13
    march_cons = annual_consumption * 0.12
    april_cons = annual_consumption * 0.09
    may_cons = annual_consumption * 0.06
    june_cons = annual_consumption * 0.04
    july_cons =  annual_consumption * 0.03
    august_cons =  annual_consumption * 0.04
    september_cons = annual_consumption * 0.05
    october_cons = annual_consumption * 0.08
    november_cons = annual_consumption * 0.11
    december_cons =  annual_consumption * 0.13
else:
    january_cons = input( "Januari - ")
    february_cons = input ("Februari - ") 
    march_cons = input ("Mars - ")
    april_cons = input ("April - ")
    may_cons = input ("Maj - " )
    june_cons = input ("Juni - ")
    july_cons =  input ("Juli - ")
    august_cons = input ("Augusti - ")
    september_cons =input ("September - ")
    october_cons = input ("October - ")
    november_cons = input ("November - ")
    december_cons = input ("December - ")

monthly_prod = [f"Januari",january_cons,"Februari",february_cons,"Mars",march_cons,"April",april_cons,"Maj",may_cons,"Juni",june_cons,"Juli",july_cons,"Augusti",august_cons,"September",september_cons,"oktober",october_cons,"November",november_cons,"December",december_cons]
#Size of solar
for months in monthly_prod:
    print (months)
while True:
    recommended_solar = annual_consumption * 0.4
    print ()

    print (f"Rekommenderad årlig produktion:{recommended_solar}\n")


    #Size of battery
    batterysize = recommended_solar /12
    batterysize = batterysize /30
    print (f"Rekommenderad batteristorlek för daglig användning: {int (batterysize)} \n")

    break