import unittest2 as ut
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import ait
        
class testcase1(ut.TestCase):
    def testA(self):
        
        service = Service(executable_path=r"C:\Users\FutureCode\Downloads\chromedriver-win64\chromedriver.exe")

        browser = webdriver.Chrome(service = service)

       
        browser.get('https://www.crazygames.com/game/smash-karts')    

        
         
       
        

           
        ait.click(527, 549)
        time.sleep(30)
        print(ait.color(486,236))
        ait.click(486,236)
        time.sleep(1)
        print(ait.color(244,243))
        r1 ,g1 ,b1 = ait.color(433,465)
        print(r1 ,g1 ,b1)
      

        
        
        self.assertEqual (r1 ,44,'Кнопка меню работает')
        self.assertEqual(g1 ,124,'Кнопка меню работает')
        self.assertEqual(b1 ,229, 'Кнопка меню работает')


class testcase2(ut.TestCase):
    def testB(self):
        
        service = Service(executable_path=r"C:\Users\FutureCode\Downloads\chromedriver-win64\chromedriver.exe")

        browser = webdriver.Chrome(service = service)

        try:
            browser.get('https://www.crazygames.com/game/smash-karts')    

        except:
            b = False
        b = True
       
        self.assertEqual (b ,True,'Сайт открывается')


class testcase3(ut.TestCase):
    def testC(self):
        
        service = Service(executable_path=r"C:\Users\FutureCode\Downloads\chromedriver-win64\chromedriver.exe")

        browser = webdriver.Chrome(service = service)
        browser.get('https://www.crazygames.com/game/smash-karts')    
        ait.click(527, 549)
        time.sleep(30)
        print(ait.color(486,236))
        ait.click(486,236)
        time.sleep(1)
        print(ait.color(244,243))
        r1 ,g1 ,b1 = ait.color(433,465)
        print(r1 ,g1 ,b1)
      
        self.assertEqual (r1 ,44,'С кнопкой меню можно взаимодействовать')
        self.assertEqual(g1 ,124,'С кнопкой меню можно взаимодействовать')
        self.assertEqual(b1 ,229, 'С кнопкой меню можно взаимодействовать')
        
ut.main()
        

