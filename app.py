from flask import Flask
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True
driver = webdriver.Chrome(executable_path='F:/Python/flask1/env/chromedriver' , chrome_options=options)


app = Flask(__name__)
@app.route('/<name>')
def index(name):
	driver.get("https://www.youtube.com/watch?v=QjtW-wnXlUY&t=469s")
	page = driver.page_source

	return page
