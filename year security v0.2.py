import datetime
current_year = datetime.datetime.now().year # визначення теперешьного року
while True: # перевірка введених даних
    try:
        birth_year = int(input("Введіть рік вашого народження: "))
        if birth_year<1900 or birth_year>= current_year:
            raise ValueError()
        break
    except ValueError: 
        print("Будь ласка, введіть коректний рік народження.")  
age = current_year - birth_year
if age >= 18:
    print("Ви є повнолітнім. Вхід дозволений!")
else:
    print("Ви ще не досягли повноліття. Вхід заборонений!")
years_to_eighteen = 18 - age
if years_to_eighteen >= 5:
    print("Ви досягнете повноліття через "+ str(years_to_eighteen) +" років.")
if years_to_eighteen<5:
    print("Ви досягнете повноліття через "+ str(years_to_eighteen) +" роки.")
if years_to_eighteen == 1:
    print("Ви досягнете повноліття через один рік.")
print("Дякую, що використали нашу програму!")