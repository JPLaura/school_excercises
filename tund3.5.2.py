a = True
#Kõik numbrind ja tähed (mitte täpitähed jms) on True kuid 0 on alati False
if a == True:
    print("a on tõene")
    print("True")
#if a != 10 kontrollib kas a on 10
elif a == "y":
    print("a on y")
else:
    #print("a on väär")
    #print("False")
    print("a ei ole x ega y")
#print("False") siin ei käi enam blokki ning satub tingimusteta teksti