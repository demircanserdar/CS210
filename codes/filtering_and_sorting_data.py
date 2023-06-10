import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("data.csv")
data2 = pd.read_csv("yonelimfinal.csv")
data3 = pd.read_csv("datav2.csv")

data = pd.concat([data, data2, data3], axis = 0)
data = data.drop(columns="Timestamp")

x = data.shape
data.head() 
print(x)

data = data.rename(columns = {"Cinsiyet":"Gender", "Yas":"Age", "Bolge":"Region", "Egitim":"Education", "soru1":"GOOD_ECONOMY", "soru2":"SUPPORT_EDUCATIONAL_REFORM", "soru3":"STOP_PRIVATIZATION",
                            "soru4":"DEATH_PENALTY", "soru5": "FREE_MEDIA", "soru6": "SUPPORT_ALCOHOL_BAN",
                            "soru7":"SUPPORT_SECULARISM", "soru8":"SUPPORT_ABORTION_BAN", "soru9":"OHAL_LIMITS_FREEDOM",
                            "soru10":"SUPPORT_NEW_PARTIES", "parti": "Party"})

data = data.replace("Hayır", "No")
data = data.replace("Evet", "Yes")
data = data.replace("Lisans", "Bachelor Degree")
data = data.replace("Ön Lisans", "Associate Degree")
data = data.replace("Lisans Üstü", "Masters Degree")
data = data.replace("Ortaokul", "Middle School")
data = data.replace("İlkokul", "Primary School")
data = data.replace("Lise", "Highschool")
data = data.replace("DIĞER", "OTHER")
data = data.replace("Erkek", "Male")
data = data.replace("Güneydoğu", "Guneydogu")
data = data.replace("İç Anadolu", "Ic Anadolu")
data = data.replace("Doğu Anadolu", "Dogu Anadolu")
data = data.replace("Kadın", "Female")
