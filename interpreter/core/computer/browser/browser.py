import threading
import time

import html2text
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, computer):
        self.computer = computer
        self._driver = None

    @property
    def driver(self, headless=False):
        if self._driver is None:
            self.setup(headless)
        return self._driver

    @driver.setter
    def driver(self, value):
        self._driver = value

    def search(self, query):
        """
        Searches the web for the specified query and returns the results.
        """
        pass

    def fast_search(self, query):
        """
        Searches the web for the specified query and returns the results.
        """
        pass

    def setup(self, headless):
        try:
            self.service = Service(ChromeDriverManager().install())
            self.options = webdriver.ChromeOptions()
            # Run Chrome in headless mode
            if headless:
                self.options.add_argument("--headless")
                self.options.add_argument("--disable-gpu")
                self.options.add_argument("--no-sandbox")
            self._driver = webdriver.Chrome(service=self.service, options=self.options)
        except Exception as e:
            print(f"An error occurred while setting up the WebDriver: {e}")
            self._driver = None

    def go_to_url(self, url):
        """Navigate to a URL"""
        pass

    def search_google(self, query, delays=True):
        """Perform a Google search"""
        pass

    def analyze_page(self, intent):
        """Extract HTML, list interactive elements, and analyze with AI"""
        pass

    def quit(self):
        """Close the browser"""
        pass
