#Energy solution helper
import random
import time

range_list = range(0,99999999)
#Årlig förbrukning per månad baserat på snitt

first_input =input ("Vet du kunds förbrukning månadsvis? Ja/Nej \n")
if first_input.lower() != "ja":
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
    january_cons = int(input("Januari - "))
    february_cons = int(input("Februari - ")) 
    march_cons = int(input("Mars - "))
    april_cons = int(input("April - "))
    may_cons = int(input("Maj - "))
    june_cons = int(input("Juni - "))
    july_cons = int(input("Juli - "))
    august_cons = int(input("Augusti - "))
    september_cons = int(input("September - "))
    october_cons = int(input("October - "))
    november_cons = int(input("November - "))
    december_cons = int(input("December - "))

    annual_consumption = (
    january_cons + february_cons + march_cons + april_cons + may_cons +
    june_cons + july_cons + august_cons + september_cons +
    october_cons + november_cons + december_cons
)
    print(f"\nTack för att du fyllde i siffrorna!\n\n\n\n")
     
monthly_prod = [f"Januari",january_cons,
                "Februari",february_cons,
                "Mars",march_cons,
                "April",april_cons,
                "Maj",may_cons,
                "Juni",june_cons,
                "Juli",july_cons,
                "Augusti",august_cons,
                "September",september_cons,
                "oktober",october_cons,
                "November",november_cons,
                "December",december_cons]
#Size of solar
for i in range(0, len(monthly_prod), 2):
    month = monthly_prod[i]
    consumption = monthly_prod[i + 1]
    print(f"{month}: {int(consumption)}")
while True:
    print (f"Årlig konsumption: {annual_consumption} kWh")
    recommended_solar = annual_consumption * 0.4
    print ()

    print (f"Rekommenderad årlig produktion:{recommended_solar}\n")


    #Size of battery
    batterysize = recommended_solar /12
    batterysize = batterysize /30
    print (f"Rekommenderad batteristorlek för daglig användning: {int (batterysize)} \n")

    break