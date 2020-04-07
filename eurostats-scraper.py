#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expcond
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time

# Realiza web scraping para buscar informações sobre os indicadores:
# 1428584 Harmonized Consumer Price Índex (HCPI) - European Union / MENSAL
# 1428490 Harmonized Consumer Price Índex (HCPI) - Austria / MENSAL 


# Set browser options
opts = Options()
driver_path = r"C:/Users/winicius.faquieri/Programas/chromedriver.exe"

timeout = 5  # In seconds
opts.headless = False
#assert opts.headless

# Carrega o navegador
browser = Chrome(driver_path, options=opts)

# 1st step
# Open the url for main site
url = "https://ec.europa.eu/eurostat/data/database" 
browser.get(url)
time.sleep(10)

# Click on "Browse statistics by theme"
buttom1 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_Ky13bqSfZSwl"]/div/div/div/ul/li[2]/a')
buttom1.click()

# Click on "Harmonised Indices of Consumer Prices (HICP)""
buttom2 = browser.find_element(By.XPATH,'//*[@id="portlet_56_INSTANCE_kN4mK3EFTK4A"]/div/div/div/div[1]/table/tbody/tr[1]/td[2]/ul/li[7]/a')
buttom2.click()

# Click on "Complete database"
buttom3 = browser.find_element(By.XPATH,'//*[@id="portlet_56_INSTANCE_LxedYvMUiUHG"]/div/div/div/div[1]/div/div[1]/div[1]/a/p')
buttom3.click()

window_current = browser.window_handles[0]
print (window_current)

# Click on "HICP (2015 = 100) - monthly data (index) (prc_hicp_midx)"
time.sleep(10)
buttom4 = browser.find_element_by_class_name('icon-app-nui-bookmark')
buttom4.click()

# Open new URL
window1 = browser.window_handles[1]
browser.switch_to.window(window1)
print (window1)
time.sleep(10)

# Click on "Change selection"
buttom5 = browser.find_element(By.XPATH,'//*[@id="COICOP"]/button')
buttom5.click()

# Open new URL
window2 = browser.window_handles[2]
browser.switch_to.window(window2)
print (window2)
time.sleep(7)

# Click on "TIME"
buttom6 = browser.find_element(By.XPATH,'//*[@id="tabs"]/div[3]/a/span')
buttom6.click()

# Click on "Code range"
buttom7 = browser.find_element(By.XPATH,'//*[@id="filteringRANGE"]')
buttom7.click()

# Agatha 
date_min = (browser.find_element (By.XPATH, '//*[@id="minCode"]'))
date_min.send_keys('2000')
date_max = (browser.find_element (By.XPATH, '//*[@id="maxCode"]'))
date_max.send_keys('2019')

# Click on "Search"
buttom8 = browser.find_element(By.XPATH,'//*[@id="searchButtons"]/input[1]')
buttom8.click()

# Click on "Select list"
buttom9 = browser.find_element(By.XPATH,'//*[@id="selectList"]')
buttom9.click()

# Click on "Select All"
buttom10 = browser.find_element(By.XPATH,'//*[@id="checkUncheckAllCheckboxTable"]')
buttom10.click()

# Click on "Update"
buttom11 = browser.find_element(By.XPATH,'//*[@id="updateExtractionButton"]')
buttom11.click()

# Back to window1
browser.switch_to.window(window1)
time.sleep(7)

# Click on "Download"
buttom12 = browser.find_element(By.XPATH,'//*[@id="nav"]/ul/li[3]/a')
buttom12.click()

# Click on "Cell formatting"
buttom13 = browser.find_element(By.XPATH,'//*[@id="csvDOT_COMMA_FORMAT"]')
buttom13.click()

# Download in CSV format 
#buttom14 = browser.find_element(By.XPATH,'//*[@id="CSV"]/ol/li[9]/input')
#buttom14.click()

# Download in xls format
buttom14 = browser.find_element(By.XPATH,'//*[@id="EXCEL"]/ol/li[10]/input')
buttom14.click()



# Crawling para coleta dos seguintes indicadores:
# Freight transport by road and removal services - European Union (28 countries)
# Service Producer Prices - Total Output Price Index  - Air Transport  - European Union (28 countries)
# Service Producer Prices - Total Output Price Index - Sea and Coastal Water Transport  - European Union (28 countries)

# Set browser options
opts = Options()
driver_path = r"C:/Users/winicius.faquieri/Programas/chromedriver.exe"

timeout = 5  # In seconds
opts.headless = False
#assert opts.headless

# Carrega o navegador
browser = Chrome(driver_path, options=opts)

# 1st step
# Open the url for main site
url = "https://ec.europa.eu/eurostat/data/database" 
browser.get(url)
time.sleep(10)

# Click on "Browse statistics by theme"
buttom1 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_Ky13bqSfZSwl"]/div/div/div/ul/li[2]/a')
buttom1.click()

# Click on "Short-term business statistics"
buttom2 = browser.find_element(By.XPATH,'//*[@id="portlet_56_INSTANCE_kN4mK3EFTK4A"]/div/div/div/div[1]/table/tbody/tr[2]/td[1]/ul/li[2]/a')
buttom2.click()

# Click on "Database"
buttom3 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_uQTy950apfY9"]/div/div/div/ul/li[2]/ul/li[2]/a')
buttom3.click()

window_current = browser.window_handles[0]
print (window_current)

#buttom4 = browser.find_element_(By.XPATH,'//*[@id="tree_c439f36c-48f7-429a-82d2-dee58e4656db_.EU_MAIN_TREE.data.icts.sts.sts_ts.sts_os"]/a/table/tbody/tr/td[3]/a/img')
#buttom4.click()

# Click on ""
time.sleep(10)
buttom4 = browser.find_element_by_class_name('title3')
buttom4.click()


# Crawling para coleta dos seguintes indicadores:
# 1428509 Industry Producer Prices Index - Manufacture of Machinery and Equipment n.e.c. - European Union (28 countries)
# 1428638 Producer Prices in Industry - Total Output Price Index  - Manufacture of Basic Metals - European Union (28 countries)
# 1428504 Producer Prices inIndustry- Total Output Price Index -Manufacture of Machinery and Equipmente - European Union (28 countries)
# 1428642 Repair and maintenance of aircraft and spacecraft - European Union (EU 19)

# Set browser options
opts = Options()
driver_path = r"C:/Users/winicius.faquieri/Programas/chromedriver.exe"

timeout = 5  # In seconds
opts.headless = False
#assert opts.headless

# Carrega o navegador
browser = Chrome(driver_path, options=opts)

# 1st step
# Open the url for main site
url = "https://ec.europa.eu/eurostat/data/database" 
browser.get(url)
time.sleep(10)

# Click on "Browse statistics by theme"
buttom1 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_Ky13bqSfZSwl"]/div/div/div/ul/li[2]/a')
buttom1.click()

# Click on "Short-term business statistics"
buttom2 = browser.find_element(By.XPATH,'//*[@id="portlet_56_INSTANCE_kN4mK3EFTK4A"]/div/div/div/div[1]/table/tbody/tr[2]/td[1]/ul/li[2]/a')
buttom2.click()

# Click on "Database"
buttom3 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_uQTy950apfY9"]/div/div/div/ul/li[2]/ul/li[2]/a')
buttom3.click()
time.sleep(10)

# Click on "Production in industry (sts_ind_prod)"
buttom4 = browser.find_element(By.CLASS_NAME,'icon-folder-close')
buttom4.click()

window_current = browser.window_handles[0]
print(window_current)

# Problem 
# Click on "Production in industry (sts_ind_prod)"
#buttom5 = browser.find_element(By.CLASS_NAME,'con-app-nui')
#buttom5.click()
#buttom5 = browser.find_element(By.XPATH,'//*[@id="tree_98f393d8-5606-4a52-8152-a089831c766a_.EU_MAIN_TREE.data.icts.sts.sts_ind.sts_ind_prod.sts_inpr_m"]/a/table/tbody/tr/td[5]/a[1]')
#buttom5.click()

# <a title="Data explorer" class="icon-app-nui" href="#" onclick="window.open('/eurostat/estat-navtree-portlet-prod/AppLinkServices?lang=en&amp;appId=nui&amp;appUrl=http%3A%2F%2Fappsso.eurostat.ec.europa.eu%2Fnui%2Fshow.do%3Fdataset%3Dsts_inpr_m%26lang%3Den', '', 'menubar=no,toolbar=yes,resizable,scrollbars,width=1024,height=768,top=128,left=128');return false;"></a>
# //*[@id="tree_98f393d8-5606-4a52-8152-a089831c766a_.EU_MAIN_TREE.data.icts.sts.sts_ind.sts_ind_prod.sts_inpr_m"]/a/table/tbody/tr/td[5]/a[1]

# Open new URL
window1 = browser.window_handles[1]
browser.switch_to.window(window1)
print (window1)
time.sleep(10)


# Crawling para coleta do seguinte indicador:
# 1428643 Europa Industry Producer Prices Index - Manufacture of Machinery and Equipment n.e.c. - Switzerland

# Set browser options
opts = Options()
driver_path = r"C:/Users/winicius.faquieri/Programas/chromedriver.exe"

timeout = 5  # In seconds
opts.headless = False
#assert opts.headless

# Carrega o navegador
browser = Chrome(driver_path, options=opts)

# Open the url for main site
url = "https://ec.europa.eu/eurostat/data/database" 
browser.get(url)
time.sleep(10)

# Click on "Browse statistics by theme"
buttom1 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_Ky13bqSfZSwl"]/div/div/div/ul/li[2]/a')
buttom1.click()

# Click on "Short-term business statistics"
buttom2 = browser.find_element(By.XPATH,'//*[@id="portlet_56_INSTANCE_kN4mK3EFTK4A"]/div/div/div/div[1]/table/tbody/tr[2]/td[1]/ul/li[2]/a')
buttom2.click()

# Click on "Database"
buttom3 = browser.find_element(By.XPATH,'//*[@id="portlet_85_INSTANCE_uQTy950apfY9"]/div/div/div/ul/li[2]/ul/li[2]/a')
buttom3.click()
time.sleep(10)

# Problem !!
# Click on "Producer prices in industry (sts_inpp_t)"
buttom4 = browser.find_element(XPATH,'//*[@id="tree_a515e124-6dd8-4e6e-87ea-f273528e0300_.EU_MAIN_TREE.data.icts.sts.sts_ind.sts_ind_pric"]/a/table/tbody/tr/td[4]/a/i')
buttom4.click()


# In[10]:



# Click on "Producer prices in industry, total (sts_inpp_t)"
buttom5 = browser.find_element(By.CLASS_NAME,'icon-folder-close')
buttom5.click()

window_current = browser.window_handles[0]
print(window_current)




