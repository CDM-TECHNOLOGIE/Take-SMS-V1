==============================

#🚧 CONFIGURATION TAKE SMS 🚧

==============================

#NUMÉRO 

target_number = "+509xxxxxxxx"
sauvegarder_sms("+509xxxxxxxx", "Ton message ici", target_number)

# ==============================  
# PART 02  
# ==============================  
  
```python  
def sauvegarder_sms(numero_source, message, target_number):  
    if numero_source == target_number:  
        with open("sms_recus.txt", "a") as f:  
            f.write(f"De \n")  
            print("Message enregistré avec succès ! 📝")  
  
  
  
  

