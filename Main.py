# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:17:23 2016

@author: jpelda
"""


from Data2 import Data2
from Eex import Eex
from Waermeerzeuger import Waermeerzeuger
import numpy as np
import time
from Plotter import Plotter
from Data import Data
from TRY import TRY
from Waermeerzeuger_Solar import Waermeerzeuger_Solar
from Dictionaries import Dictionaries





start_time = time.clock()
a = Waermeerzeuger_Solar(Dictionaries().vitosol_200F_SVE())
weather = TRY(r'C:\Users\jpelda\Documents\Python Scripts\wetterdaten', 'Bremerhaven','2010','Jahr', True)
#print(a.apertureArea_m2(), a.ausrichtung_grad(90), a.neigung_grad(20))
print(a.absorberArea_m2(), a.apertureArea_m2(), a.ausrichtung_grad())
waerme = []
print(len(weather.date()))
for index, item in enumerate(weather.date()):
    waerme.append(a.waerme_kw(weather.airTemperature_2m_degreeCelsius(index), 40, 1000))
    
print(len(waerme))
index = 0
for index, item in enumerate(weather.date()):
    print(item, index, waerme[index])



#i = 0
#while i < len(weather.datum()):
#    print(str(weather.datum()[i]) + '::::: ' + str(weather.lufttemperatur_2m_GradCelsius()[i]))
#    i += 1
#print(str(weather.datum()))
#
#'''start import data which are needed for simulation'''
#
##eex = Data()
#
#
#data = Data()
##print(data.name())
#'''end of import data which are needed for simulation'''
#
#'''start of simulation'''
##print(type(eex.LeistungkW()))
##data = eex.LeistungkW()[2] * eex.LeistungkW()[2]
##data = eex.LeistungkW() * (eex.Bedarf() * eex.Bedarf())
#
#
#
##werzeuger = Waermeerzeuger("data\waermeerzeuger.csv", ";")
##werzeuger.importData(werzeuger.getdtype(), werzeuger.getstartrow(), werzeuger.str2date(werzeuger.get_col_date()))
##
##data_gesamtwaermeproduktion = werzeuger.leistungBHKW1_array() + werzeuger.leistungBHKW2_array() + werzeuger.leistungBHKW3_array() + werzeuger.leistungORC_array() + werzeuger.leistungHHS_array()
##data_waermediff = werzeuger.waermeverbrauch_array() - data_gesamtwaermeproduktion
##
##pltwerzeuger = Plotter(werzeuger.date_array(),[ 
##                       werzeuger.leistungBHKW1_array(), 
##                       werzeuger.leistungORC_array(), 
##                       werzeuger.waermeverbrauch_array(),
##                       data_gesamtwaermeproduktion,
##                       data_waermediff],
##                       "Datum", 
##                       "kW", 
##                       "Leistung über Zeit", 
##                       ["Leistung BHKW1 [kW]", "Leistung ORC [kW]", "Wärmeverbrauch [kW]", "gesamte Wärmeproduktion [kW]", "Wärmedifferenz [kW]"]
##                        )
##pltwdiff = Plotter(werzeuger.date_array(),
##                   [data_waermediff],
##                   "Datum",
##                   "kW",
##                   "Differenz Wärmeverbrauch, Wärmeproduktion",
##                   ["Wärmedifferenz [kW]"])
##                   
#
#pltwetter = Plotter('test')#
#pltwetter.plot_xyyLine(weather.datum(),
#                    [weather.lufttemperatur_2m_GradCelsius()],
#                    [weather.windgeschwindigkeit_10m_mpros()],
##                    weather.windrichtung_10m_Grad(),
#                    "Datum",
#                    "°C",
#                    "[m/s]",
#                    "noch undefiniert",
#                    ["Lufttemperatur 2 m über Grund [°C]"], 
#                    ["Windgeschwindigkeit 10 m über Grund [m/s]"], 
#                    #"Windrichtung 10 m über Grund [°]"
#                    
#                    )                     
##pltwerzeuger.plot_xyLine()
##pltwdiff.plot_xyLine()
#pltwetter.plot_xyLine(weather.datum(),
#                    [weather.lufttemperatur_2m_GradCelsius(),
#                    weather.windgeschwindigkeit_10m_mpros(),
##                    weather.windrichtung_10m_Grad(),
#                    ],
#                    "Datum",
#                    "°C",
#                    "noch undefiniert",
#                    ["Lufttemperatur 2 m über Grund [°C]", "Windgeschwindigkeit 10 m über Grund [m/s]", 
#                    #"Windrichtung 10 m über Grund [°]"
#                    ]
#                    )

'''end of simulation'''
'''start of plotting'''

#print(eex.name())
#print(eex.LeistungkW())
#print(data)
#print(eex.name()[10])

#plt = Plotter(eex.name(),
#              [data,data],
#              'Datum',
#              'kW',
#              'Unsinnsplot',
#              ["BHKW Zeuchs"]
#              )
#plt.plot_xyLine()






#time.sleep(3)
print(time.clock() - start_time)
