from selenium import webdriver
import time as t
#from Credentials import username,psw
import pyautogui as p
from colorama import Fore,Style


good=0

bad=0

follow=0
like=0
views=0
action=""
ad=0

target= input("Inserisci username Target:")
operation= input("Inserisci operazione(1.Follow,2.Like,3.views):")
link=""




def Work(operation,driver):
    if int(operation)==1:
        t.sleep(2)
        try:
            x,y=p.locateCenterOnScreen("igfollow.png",confidence=0.75)
            p.click(x,y)
            global follow
            follow+=1
            t.sleep(0.5)
            
            print("pulsante follow  trovato")
            return(follow)
            
        except:
            print("pulsante follow non trovato")
    elif int(operation)==2:
        driver.get(link)
        t.sleep(1.5)
        try:
            t.sleep(2)
            x,y=p.locateCenterOnScreen("iglike.png",confidence=0.75)
            p.click(x,y)
            global like
            like+=1
            t.sleep(0.3)
            
            
            print("pulsante like trovato")
            return(like)
        except:
            print("pulsante like non trovato")
    else:
        driver.get(link)
        t.sleep(1.5)
        try:
            x,y=p.locateCenterOnScreen("iglike.png",confidence=0.75)
            p.click(x-250,y-100)
            global views
            views+=1
            t.sleep(0.3)
            return(views)
            
            
        except:
            print("pulsante views non trovato")
        t.sleep(30)
        
        
        
        




if int(operation) !=1:
    link=input("Inserisci link post:")
    
                 

try:
    file = open("IGAccountlist.txt")
    accounts = list(file)
#    print (accounts)
    c3=""
    for item in accounts:
        c3+=item
    accounts=c3.split("\n")
    c2=""
#   print(accounts)

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
        
        t.sleep(4)
        if p.locateCenterOnScreen("iglog.png",confidence=0.7)!=None:
            
            print(Fore.LIGHTGREEN_EX+"[GOOD]Log in")
            good+=1
        else:
            t.sleep(1)
            if p.locateCenterOnScreen("ignonora.png",confidence=0.7)!=None:
                 print(Fore.LIGHTGREEN_EX+"[GOOD]Log in")
                 good+=1
                 t.sleep(2)
                 x,y=p.locateCenterOnScreen("ignonora.png",confidence=0.7)
                 p.click(x,y)
            else:
                 print(Fore.LIGHTRED_EX+"[BAD]Failed")
                 bad+=1
                 
            
        t.sleep(2)
        try:
            x,y=p.locateCenterOnScreen("igsearch.png",confidence=0.75)
            p.click(x,y)
            t.sleep(0.5)
            p.write(target)
            
        except:
            print("pulsante di ricerca non trovato")
        t.sleep(1)
        p.hotkey("enter")
        p.hotkey("enter")
        try:
            cv=Work(operation,driver)
            if cv>0 and cv!=None:
                ad=cv
        except Exception as e:
            print("error:"+str(e))
        t.sleep(1)
        p.hotkey("alt","f4")
        t.sleep(1)
except Exception as e:
    print(str(e))
#print("ALIVE Account:"+str(good)+"\nDEAD Account:"+ str(bad))

if  follow>0:
    print("Follow:"+str(follow))
elif like>0:
    print("Likes:"+str(like))
else:
    print("Views:"+str(views))



#print("fine")
t.sleep(3)





                                                                          




