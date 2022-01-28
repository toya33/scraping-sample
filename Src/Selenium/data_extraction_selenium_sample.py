from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd


class scraper:

    def __init__(self):
        self.browser = webdriver.Chrome('chromedriver.exe')

    def set_option(self):
        self.options = Options()

        # ウィンドウ非表示で実行
        self.options.add_argument('--headless')

    def exec_get(self, url):
        self.browser.get(url)
        sleep(3)

    def login(self, url):

        self.exec_get(url)

        elem_username = self.browser.find_element(By.ID, 'username')
        elem_username.send_keys('imanishi')

        elem_password = self.browser.find_element(By.ID, 'password')
        elem_password.send_keys('kohei')

        elem_login_btn = self.browser.find_element(By.ID, 'login-btn')
        elem_login_btn.click()

        # ログイン画面から遷移する時間を考慮し、一定時間(ここでは3秒)処理を停止する
        sleep(3)

    def print_element_text(self, id):
        elem = self.browser.find_element(By.ID, id).text
        print(elem)

    def extract_stupid(self):
        self.print_element_text('name')
        self.print_element_text('company')
        self.print_element_text('birthday')
        self.print_element_text('come_from')
        self.print_element_text('hobby')

    def extract(self):
        elems_th = self.browser.find_elements(By.TAG_NAME, 'th')
        elems_td = self.browser.find_elements(By.TAG_NAME, 'td')

        self.keys = []
        self.values = []

        for iter in range(len(elems_th)):
            key = elems_th[iter].text
            self.keys.append(key)

            # Windows版：windowsでは「\n」で改行する。
            # このままだとcsvの形式が保てないため、「\n」を「-」に置換することとした
            # 置換しない場合の例
            # ------------
            # 4,趣味,バスケットボール
            # 読書
            # ガジェット集め
            # ------------
            value = str(elems_td[iter].text).replace('\n', '-')
            self.values.append(value)

        print(self.keys)
        print(self.values)

        df = pd.DataFrame()
        df['項目'] = self.keys
        df['値'] = self.values

        print(df)

        # インデックスは不要
        df.to_csv('講師情報.csv', index=False)

    def quit(self):
        self.browser.quit()

    def main(self):

        url = 'https://scraping-for-beginner.herokuapp.com/login_page'
        self.login(url)

        # self.extract_stupid()
        self.extract()

        self.quit()


if __name__ == "__main__":
    scraper = scraper()
    scraper.main()
