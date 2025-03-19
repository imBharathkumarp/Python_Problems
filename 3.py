#Dictionary is a Keyvalue Pairs

birthday = {
    "Bhathu" : "03-01-2023",
    "Bhanu" : "14-04-1999"
}
print(birthday.get("Bhanu","Not Found"))        #Accessing Dict Elements

birthday['Hemanth'] = '24-08-1995'      #Adding Keyvalues in Runtime

print(birthday)

birthday['Bhathu'] = '03-01-2003'       #Update/Modify Keyvalues
print(birthday)

x = birthday.pop("Bhathu")          #Deletes/pop the keyvalues
print(x)

print(birthday)

#Dictionary Methods

print(birthday.keys())
print(birthday.values())

print(birthday.items())     
