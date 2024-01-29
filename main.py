from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")  # Enable headless browsing
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options =  chrome_options)

import json
with open("links.json", "r") as file:
    data = json.load(file)
print(len(data))

addressList = []
priceList = []
featuresList = []
decriptionList = []
tenureList = []
stationsList = []
councilTax = []
schoolsList = []
speedList = []
salePriceList = []
priceHistoryList = []
urlList = []

counter = 0
csv_counter = 0
urls_per_csv = 50

def save_to_csv():
    try:
        global csv_counter
        data = {
            'Address': addressList,
            'Price': priceList,
            'Features': featuresList,
            'Description': decriptionList,
            'Tenure': tenureList,
            'Stations': stationsList,
            'CouncilTax': councilTax,
            'SchoolsText': schoolsList,
            'Speed': speedList,
            'SalePrice': salePriceList,
            'PriceHistory': priceHistoryList,
            'URL': urlList
        }
        df = pd.DataFrame(data)
        csv_counter += 1
        df.to_csv(f"To_{csv_counter}.csv", index=False)
        clear_lists()
    except Exception as e:
        print(e)

def clear_lists():
    addressList.clear()
    priceList.clear()
    featuresList.clear()
    decriptionList.clear()
    tenureList.clear()
    stationsList.clear()
    councilTax.clear()
    schoolsList.clear()
    speedList.clear()
    salePriceList.clear()
    priceHistoryList.clear()
    urlList.clear()

try:
    for url in data:
        driver.get(url)
        time.sleep(3)
        counter += 1
        print("Working on URL", counter)

        # Your existing code for processing each URL here
        address = driver.find_element(By.CLASS_NAME, "h3U6cGyEUf76tvCpYisik").text
        price = driver.find_element(By.CLASS_NAME, "_1gfnqJ3Vtd1z40MlC0MzXu").text
        container = driver.find_element(By.CLASS_NAME, "_4hBezflLdgDMdFtURKTWh")
        boxes = container.find_elements(By.CLASS_NAME, "_3gIoc-NFXILAOZEaEjJi1n")
        addressList.append(address)
        priceList.append(price)
        featuresTemp = []
        for box in boxes:
            featuresTemp.append(box.text)
        featuresList.append(featuresTemp)
        try:
            read_more = driver.find_element(By.CLASS_NAME, "_33m7y0JkS3Q_2tRLrMPB9U")
            read_more.click()
            time.sleep(1)
        except:
            print("read more not working")
        desc = driver.find_element(By.CLASS_NAME, "OD0O7FWw1TjbTD4sdRi1_").text
        decriptionList.append(desc)
        try:
            box = driver.find_elements(By.CLASS_NAME, "_3OGW_s5TH6aUqi4uHum5Gy")
            Tenure = box[-1].text
        except:
            Tenure = "N/A"
        tenureList.append(Tenure)
        driver.execute_script("scrollBy(0, 400);")
        time.sleep(1)
        try:
            council_tax = driver.find_element(By.CLASS_NAME, "_1VOsciKYew6xj3RWxMv_6J").text
        except:
            council_tax = "N/A"
        councilTax.append(council_tax)
        driver.execute_script("scrollBy(0, 800);")
        time.sleep(1)
        try:
            stations_list = driver.find_element(By.CLASS_NAME, "_2f-e_tRT-PqO8w8MBRckcn")
            stations = stations_list.find_elements(By.TAG_NAME, "li")
            stationsTemp = []
            for station in stations:
                stationsTemp.append(station.text)
            stationsList.append(stationsTemp)
        except:
            stationsList.append("N/A")
            print("station not working")
        time.sleep(1)
        schoolsList.append("N/A")
        try:
            time.sleep(1)
            sale_history = driver.find_element(By.CLASS_NAME, "_1-GJOH09_oTTmLw-B-feOC").click()
            time.sleep(1)
            sale_price = driver.find_element(By.CLASS_NAME, "v6bq3YD8Qj9MPRmQBmY-U").text
            priceHistoryContainer = driver.find_element(By.CLASS_NAME, "_1SNP1o4T-Q9HHmHymdO1Gn")
            prices = priceHistoryContainer.find_elements(By.TAG_NAME, 'tr')
            prcieHistoryTemp = []
            flag = False
            for price in prices:
                row = [item.text for item in price.find_elements(By.XPATH, 'td')]  # find the data
                if len(row) != 0:
                    prcieHistoryTemp.append(row[0] + " " + row[1])
                    flag = True
            if flag == True:
                priceHistoryList.append(prcieHistoryTemp)
            else:
                priceHistoryList.append("N/A")
            salePriceList.append(sale_price)
        except:
            priceHistoryList.append("N/A")
            salePriceList.append("N/A")
            print("sale and price history not working")
        speedList.append("N/A")
        urlList.append(driver.current_url)

        # Call save_to_csv after processing every URL
        save_to_csv()

except Exception as e:
    print(e)
    print("stopped on following url", counter)

finally:
    driver.quit()
