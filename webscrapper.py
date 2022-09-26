import undetected_chromedriver as uc
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import time
import pandas as pandas

#Define working directory
wd = '/Users/kyoshi/Desktop/python/keywords.xlsx'
#READ EXCEL
excel_data_df = pandas.read_excel('keywords.xlsx')
# df.keywords = pd.read_excel('\keywords.xlsx’)
# No. of top N result extracting
n_result = 50
# initializing
se_results = []
n_keyword = 0
#Start webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
# options.add_argument('--headless') #hidden browser 
driver = uc.Chrome(options=options)