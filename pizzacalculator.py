# pizza calculator
# Enes Tekinbas

# de variabelen geven de waarde aan van de pizza
kleinpizza = int(input("hoeveel klein pizza's wilt u hebben?: "))
prijskleinpizza = int(9)
totaalprijsKP = kleinpizza * prijskleinpizza
mediumpizza = int(input("hoeveel medium pizza's wilt u hebben?: "))
prijsmediumpizza = int(11)
totaalprijsMP = mediumpizza * prijsmediumpizza
grootpizza = int(input("hoeveel groote pizza's wilt u hebben?: "))
prijspizzagroot = int(13)
totaalprijsGP = grootpizza * prijspizzagroot

#deze variabel bevatten het formaat en de prijs van de pizza 
totaleprijs = totaalprijsKP + totaalprijsMP + totaalprijsGP 

# deze print opdracht berekent uiteindelijk hoeveel de totale waarde van aantal bestelde pizza's
print("u heeft",str(kleinpizza), "klein pizza gekozen","u heeft",str(mediumpizza), "medium pizza gekozen", "u heeft",str(grootpizza),"groot pizza gekozen")
print("totale bedrag kleinepizza's € " + str(totaalprijsKP))
print("totale bedrag mediumpizza's € " + str(totaalprijsMP))
print("totale bedrag grootepizza's € " + str(totaalprijsGP))
print("het te totale bedrag is € "     + str(totaleprijs)) 