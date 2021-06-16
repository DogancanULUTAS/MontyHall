"""
Created on Mon Nov 30 14:07:27 2020

@author: dcu
"""

import random
import numpy as np
import matplotlib.pyplot as plt

switching=[]
stay=[]

def play_monty_hall(choice):
 
    prizes = ['Keçi', 'Araba', 'Keçi']  #Kapının arkasındaki ödüller Ve
                                        #Bunlar randomlanacak.    
    random.shuffle(prizes) #Ödülleri Randomla
    
    #Arabasız kapıyı belirle
    while True:
        opening_door = random.randrange(len(prizes))
        if prizes[opening_door] != 'Araba' and choice-1 != opening_door:
            break
    
    opening_door = opening_door + 1
    print('Senin İçin -%d- Numaralı Kapıyı Eliyoruz. ' % (opening_door))
    
    #Anahtar kapısının belirlenmesi
    options = [1,2,3]
    options.remove(choice)
    options.remove(opening_door)
    switching_door = options[0]
    
    #Seçeneğin değiştirilmesi için
    print('Kapı Numaranı -%d- İle Değiştirmek İster Misin ? (e/h)' %(switching_door))
    answer = input()
    if answer == 'e':
        result = switching_door - 1
        switching.append(1)
        stay.append(0)
    else:
        result = choice - 1
        switching.append(0)
        stay.append(1)
    
    #Ödül Ekranı
    print('VE ÖDÜLÜN ....', prizes[result].upper())
    
    print ("\n")

for M in range(1, 11): #10 defa yapıyor. 

     print ("- ",M,". Tur -") #Tasarım için
        
    #İlk Seçim
     choice = int(input('Hadi Bakalım! Bir Kapı Seç ? (1,2,3): '))
    
    #Oyun
     play_monty_hall(choice)
     
     #Olasılık Sonuçları
prob_win_switch = np.mean(switching)
prob_win_stay = np.mean(stay)

print ("- Olasılık Sonuçları -\n")

print(f"Yarışmacı İlk Seçimini Değiştirirse Kazanma Olasılığı: {prob_win_switch : 0.2%}")
print(f"Yarışmacı İlk Seçimini Değiştirmezse Kazanma Olasılığı: {prob_win_stay : 0.2%}")
   
# Grafiği çizdir 
fig = plt.figure(figsize = (10,8));
ax = fig.add_subplot(111); #Çizgi=Subplot

# Ortalamaları hesaplat
environments = range(1,11)
switch_probs = [np.mean(switching[:environment]) for environment in environments]
stay_probs = [np.mean(stay[:environment]) for environment in environments]

# Olasılıklar için grafiği çizdir  
ax.plot(environments, switch_probs, label=f"Değişirse Ort.: {prob_win_switch : 0.2%}");
ax.plot(environments, stay_probs, label=f"Kalırsa Ort.: {prob_win_stay : 0.2%}");

# Labellar
ax.set_title("Değişme - Kalma", {'fontsize' :  16});
ax.set_ylabel("Kazanma Olasılığı", {'fontsize' :  14});
ax.set_xlabel("Oyun Sayısı", {'fontsize' :  14});

# Açıklama Ekle
ax.legend(fontsize = 'large');
 

