from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from pyairports.airports import Airports

options = Options()
options.add_experimental_option("detach", True)





def webscraper_kayak(from_location, to_location, from_date, travelers, max_flight_time, hand_luggage, baggage,  to_date = ''):
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    #max_flight_time muss noch in minuten konvertiert werden
    i = max_flight_time.index(':')  # Finde den Index des Doppelpunkts
    hours = int(max_flight_time[:i])  # Extrahiere die Stunden und konvertiere in Integer
    minutes = int(max_flight_time[i+1:])  # Extrahiere die Minuten und konvertiere in Integer

    # Berechne die gesamte Flugzeit in Minuten
    total_minutes = hours * 60 + minutes

    # Konvertiere das Gesamtergebnis in einen String, um es zu drucken oder weiterzuverarbeiten
    max_flight_time = str(total_minutes)
    print(max_flight_time)  # Ausgabe: '254'

    #Der Link zu Kayak, die website die ich benutze. Den link habe ich so angepasst das ich beliebeige Infos einbauen kann, um bestimmte Infos zu bekommen

    #falls es kein rückflug gibt, muss der Slash zwischen hin- und rückflug entfernt werden -> to_date_connector
    


    if to_date != '': 
        to_date = ''.join('/', to_date)
        driver.get(f"https://www.kayak.de/flights/{from_location}-{to_location}/{from_date}{to_date}/{travelers}adults?sort=price_a&fs=cfc={hand_luggage};legdur=-{max_flight_time};bfc={baggage}")
    else:
        driver.get(f"https://www.kayak.de/flights/{from_location}-{to_location}/{from_date}/{travelers}adults?sort=price_a&fs=cfc={hand_luggage};legdur=-{max_flight_time};bfc={baggage}")


    #browser tab maximieren
    driver.maximize_window()

    #wir wollen zuerst das Cookie Fenster entfernen, da es uns daran hindert auf die Informationen zuzugreifen 
    sleep(2)
    cookie_window = "//button[contains(@class,'Py0r-mod-size-xxxsmall')]"
    driver.find_element(By.XPATH, cookie_window).click()

    #nun versuchen wir Infromationen über die Flüge zu erhalten. flights_html beschreibt alle unterschiedliche Flugboxen auf der website
    flights_html = driver.find_elements(By.XPATH, "//div[@class = 'nrc6-inner']")


    #wir initialisieren zuerst die liste in der wir alle Infos speichern
    flight_data = []

    #hier ist die for-loop die durch alle Flügeinträge durchiteriert und alle wichtigen Infos herauszieht
    for webelement in flights_html:
        #Preis
        price = webelement.find_element(By.XPATH, ".//div[@class = 'f8F1-price-text']").text
        print('price: '+ price)
        #Airline
        airline = webelement.find_element(By.XPATH, ".//div[@class = 'J0g6-operator-text']").text
        print('airline: ' +airline)
        #Stopps
        stops = webelement.find_element(By.XPATH, ".//div[@class = 'vmXl vmXl-mod-variant-default']").text
        print('stops: ' +stops)
        #Fluglänge
        duration = webelement.find_element(By.XPATH, ".//div[@class='xdW8 xdW8-mod-full-airport']/div[@class = 'vmXl vmXl-mod-variant-default']").text
        print('duration: '+ duration)
        #Infos zu Ankunft und Landung
        time = webelement.find_element(By.XPATH, ".//div[@class= 'vmXl vmXl-mod-variant-large']").text
        print('time: '+time)
        #Anzahl an Handgepäck inkls.
        luggage = webelement.find_element(By.XPATH, ".//div[contains(@class, 'ac27-fee-box ac27-mod-')]/div[@class = 'ac27-inner'][2]").text
        print('luggage: '+luggage+'\n')
        #flight_data erhält alle infos zu jeweios einem Flug als dict
        flight_data.append({
            'price' : price,
            'airline': airline,
            'stops': stops,
            'duration': duration,
            'time': time,
            'luggage': luggage
        })
    #flight_data[0]['price'] 
    driver.quit()
    return flight_data

def client_com():
    from_location = '' 

def airport_code(iata_input):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.iatacodes.de/")

    #wir müssen zuerst die stadt suchen von der wirr die airports haben wollen, bzw den airport von den wir den code haben wollen
    search_input = driver.find_element(By.XPATH, "//input[@id='searchInput']")
    search_input.send_keys(iata_input)
    
    airport_codes = driver.find_elements(By.XPATH, ".//tr/td[@class='code']")
    airport_names = driver.find_elements(By.XPATH, ".//tr/td[@class='desc']")

    airport_info = []
    for i in range(len(airport_codes)):
        airport_code = airport_codes[i].text
        airport_name = airport_names[i].text
        print(airport_code, airport_name)
        airport_info.append({
            airport_name : airport_code
        })
    driver.quit()
    return airport_info

from_location = 'LEJ'
to_location = 'KTP'
from_date = '2024-05-15'
to_date = ''
travelers = '1'
max_flight_time = '4:10'
hand_luggage = ''
baggage = ''

flight_info = webscraper_kayak(from_location, to_location, from_date, travelers, max_flight_time, hand_luggage, baggage, to_date)

#airport_code('leipzig')






