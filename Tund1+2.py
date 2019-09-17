#Stringi ja inti ei saa üksteisega liita ega lahutada, sellepärast tuleb neid
#defineerida int ja str comandidega
first_name = input("Mis on sinu nimi: ")
#NB! input annab valiku midagi sisse kirjutada 
print("Tere, " + first_name + "!")
#NB! spaceid on vajalikud, sest muudame meie keelest arvuti keelda keset lauset
birth_year = int(input("Mis on sinu sünniaasta: "))
#NB! muudan sisestatava NUMBRI intiks et seda saaks hiljem 2019st lahutada
age = 2019 - birth_year
print("Oled " + str(age) + "-aastane")
#NB! kuna saadud lahutis on int peab selle tagasi stringinks muutma
