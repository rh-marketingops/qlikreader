import sys

#import os

from retrying import retry
from pyvirtualdisplay import Display

#from xvfbwrapper import Xvfb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class QlikReader(object):
    """
    """

    def __init__(self):
        """
        """
        self.driver = None
        #self.display = Xvfb()
        #self.display.start()
        self.display = Display(visible=0, size=(800,600))
        self.display.start()

    def init_driver(self, driver_path=None, driver_wait=None, qv_url_str=None):
        """
        """
        '''
        if not driver_path:
            driver_dir = os.path.dirname(os.path.abspath('__file__'))
            driver_path = os.path.join(driver_dir, 'webdriver/chromedriver')
        '''
        self.driver = webdriver.Chrome(driver_path)
        self.driver.wait = WebDriverWait(self.driver, driver_wait)
        self.driver.url_str = qv_url_str

    @retry(wait_exponential_multiplier=2000, wait_exponential_max=10000)
    def lookup(self, locate_element=None, locate_element_xpath=None):
        """
        """
        print("Info: get element value!!")

        try:

            self.driver.get(self.driver.url_str)
        
            self.driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, locate_element)))

            element_text = self.driver.find_element_by_xpath(locate_element_xpath).text

        except TimeoutException as te_error:
            print te_error
            raise te_error

        return element_text

    def quit_driver(self):
        """
        """
        self.display.stop()
        self.driver.quit()


if __name__ == "__main__":
    """
    """
    qv_url = sys.argv[1]

    web_driver_path = sys.argv[2]

    wait_time = sys.argv[3]

    locate_element = sys.argv[4] #"TextObject"

    locate_element_xpath = sys.argv[5] #"/html/body/div[3]/div/div[1]/div[2]/table/tbody/tr/td"

    qr_driver = QlikReader()

    qr_driver.init_driver(web_driver_path, wait_time, qv_url)

    print qr_driver.lookup(locate_element, locate_element_xpath)

    qr_driver.quit_driver()

