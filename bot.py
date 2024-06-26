from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Video:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.urls = []
        self.count = 0
    
    def app(self):
        self.driver.get("https://www.oba.gov.tr/")
        self.driver.maximize_window()
        sleep(4)
        mebbis = self.driver.find_element(By.XPATH,"//*[@id='bs-example-navbar-collapse-2']/ul/li[1]/a")
        mebbis.click()
        sleep(4)
        self.login()
        sleep(2)
        self.urlInput()

    def urlInput(self):
        iUrl = self.urlPrint()
        self.urls.append(iUrl)
        while True:
            ch = input("[1] - Başlat\n[2] - Daha fazla link ekle ")
            
            if ch == '1':
                self.urlCheck()
                break
            elif ch == '2':
                iUrl = self.urlPrint()
                self.urls.append(iUrl)
            else:
                print("Yanlış bir değer girdiniz.")
                continue
                
    def urlPrint(self):
        iUrl = input("Kursun başlangıç bölüm linkini ve izlemesi gereken bölüm sayısını giriniz: ")
        iUrl = iUrl.split(" ")
        print(f"Eğitim başlığı: {iUrl[0].split('/')[5]}\nBölüm sayısı: {iUrl[1]}")
        return iUrl
        
    def urlCheck(self):
        self.url = self.urls[self.count][0]
        self.ep = int(self.urls[self.count][1])
        self.driver.get(self.url)
        self.play()
    
    def login(self):

        while True:
            id_input = self.driver.find_element(By.XPATH,"//*[@id='txtKullaniciAd']")
            ps_input = self.driver.find_element(By.XPATH,"//*[@id='txtSifre']")
            cap_input = self.driver.find_element(By.XPATH,"//*[@id='txtGuvenlikKod']")            
            
            cap_input.send_keys(input("Güvenlik kodunu giriniz\n:"))
            id_input.send_keys(input("Mebbis kullanıcı adınızı giriniz:\n:"))
            ps_input.send_keys(input("Mebbis şifrenizi giriniz\n:"))
        
            if NoSuchElementException:
                print("Yanlış giriş.")
                self.driver.refresh()
                sleep(3)
            else:
                break

        btn = self.driver.find_element(By.XPATH,"//*[@id='btnGiris']")
        btn.click()
    
        
    def video(self):
        video = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]")
        video.click()
        
    def time(self):
        rTime = self.driver.find_element(By.XPATH,"//*[@id='video']/div[4]/div[5]/span[2]").text
        if rTime == "-0:00":
            return True
        
    def play(self):
        print("Play metodu çağrıldı")
        sleep(2)
        
        self.video()
        print("Videoya tıklandı")
        while True:
            sleep(5)
            if self.time():
                break
            
        self.ep -=1
            
        url_parts = self.url.split("/")
        url_parts[-1] = str(int(url_parts[-1]) + 1)
        new_url = "/".join(url_parts)
        self.url = new_url
        self.driver.get(self.url)
        print("Yeni videoya geçildi")
        print("Kalan bölüm: "+str(self.ep))
        
        if self.ep == 0:
            print("Daha fazla bölüm bulunamadı.")
            self.count +=1
            self.urlCheck()
       
        self.play()

a = Video()
a.app()
