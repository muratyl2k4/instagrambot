from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

##firstly sorry for my language I am 17 y.o. and new in codes

username = ""   #your account informations for signIn function  
password = ""

class Instagram():
    def __init__(self , username , password):
        self.driver = webdriver.Edge()
        self.username = username
        self.password = password
        self.followinglist = []    
        self.followerslist = []
    def signIn(self):   
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        userInput = self.driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[1]/div/label/input") #find the css , xpath , class name , ...
        passInput = self.driver.find_element(By.XPATH , "//*[@id='loginForm']/div/div[2]/div/label/input")

        userInput.send_keys(self.username) 
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.ENTER)
        time.sleep(10) #the sleep time may changable i did 10sec bcz slowly network connection 
        
    def unfollowBot(self):    
        self.signIn()
        i = 15
    
        self.driver.get("https://www.instagram.com/cagestrength/following/")
        time.sleep(6)
        while i > 1: 
        
            followingdiv = self.driver.find_element(By.CLASS_NAME , "_aano")
            
            buton = followingdiv.find_element(By.TAG_NAME, "button") ##find the css's again 
            time.sleep(2)
            buton.click()
            time.sleep(1)
            followingdivt = self.driver.find_element(By.CLASS_NAME , "_a9-v")
            unfollow = followingdivt.find_element(By.CLASS_NAME , "_a9-z")  #this for [You sure about unfollow <user>] messagebox on instagram
            butont = unfollow.find_element(By.TAG_NAME , "button")
            butont.click()
            time.sleep(1)
            self.driver.get("https://www.instagram.com/cagestrength/following/")
            time.sleep(4)
            i = i-1

            if i == 3:
                time.sleep(500)
                i = 15

            
    def getFollowers(self):
        self.signIn()

        self.driver.get(f"https://instagram.com/{self.username}/followers") #this self.username for your account you can change it to which account do you wanna get him/her followers

        time.sleep(6)
        
        divto = self.driver.find_element(By.CSS_SELECTOR , "div[role=dialog]")
        
        divtre = divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")

        followerCount = len(divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm"))
        print(f"first count : {followerCount}")

        action = webdriver.ActionChains(self.driver)
        divto.click() #this is the background of list what you see your followers 
        time.sleep(1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform() #and press the tab 2 times for when program press on space move the scroll down
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform() #it may changable 

        time.sleep(2)

        while True : 

            n = 20 

            for _ in range(n) :
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform() #i did 20 times because of bugs        

            time.sleep(5)

            newCount = len(divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm"))
            print(followerCount)
            print(newCount)
            if followerCount < newCount :  #after the first count if we have new followers this command continue to counting
                followerCount = newCount
                print(f"Count Update : {newCount}")  
                time.sleep(1)  

            else : 
                break
            
            
            divto = self.driver.find_element(By.CSS_SELECTOR , "div[role=dialog]")
            
            divtre = divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")
            
        for abc in divtre :
            instext = (abc.find_element(By.CSS_SELECTOR , "._aacl._aaco._aacw._adda._aacx._aad7._aade").text)
            self.followerslist.append(instext)            

        with open("followers.txt" , "w" , encoding="UTF-8") as file :  #this is for save in a txt file on your followers
            for item in self.followerslist:
                file.write(f"https://www.instagram.com/{item}\n")            

        print(len(self.followerslist))

    def getFollowing(self):  #this is the same of getFollowers
        
        self.signIn()

        self.driver.get(f"https://instagram.com/{self.username}/following")

        time.sleep(6)
        
        divto = self.driver.find_element(By.CSS_SELECTOR , "div[role=dialog]")
        
        divtre = divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")

        followerCount = len(divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm"))
        print(f"first count : {followerCount}")

        action = webdriver.ActionChains(self.driver)
        divto.click()
        time.sleep(1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform() 
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()

        time.sleep(2)

        while True :

            n = 20 
            for _ in range(n):
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform() 

            time.sleep(5)


            newCount = len(divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm"))
            if followerCount < newCount: 
                followerCount = newCount
                print(f"Count Update : {newCount}")
                time.sleep(1)

            else:
                break
                        

            
            divto = self.driver.find_element(By.CSS_SELECTOR , "div[role=dialog]")
                
            divtre = divto.find_elements(By.CSS_SELECTOR , "._ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm")

            

        for abc in divtre :
            instext = (abc.find_element(By.CSS_SELECTOR , "._aacl._aaco._aacw._adda._aacx._aad7._aade").text)
            self.followinglist.append(instext)            

        with open("following.txt" , "w" , encoding="UTF-8") as file :
            for item in self.followinglist:
                file.write(f"https://www.instagram.com/{item}\n")

        print(len(self.followinglist))

    def unfollowtounFollowers(self):  #and this is the last step on my code
        self.signIn()
        followfile = open("unfollows.txt" , "r") #you can use http://www.listdiff.com/ for see who doesnt follow you while you following
        data = followfile.read()

        txtintofile = data.split("\n")  #first we change txt to list for reach index's of unfollowers

        i = 15       

        for liste in txtintofile:
            
            self.driver.get(liste)  #while end of list this is the open all index's of list
            time.sleep(4)
             
            buton1 = self.driver.find_element(By.CSS_SELECTOR , "div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm")
            buton = buton1.find_element(By.TAG_NAME, "button")    
            buton.click()
            time.sleep(2)
            buton2 = self.driver.find_element(By.CSS_SELECTOR , "div._a9-z")
            buton3 = buton2.find_element(By.TAG_NAME , "button")
            buton3.click()
            i = i -1 

            if i <= 3:          #instagram algorithms block us when we unfollow 12 person in close time thats why i did this counter
                time.sleep(600) #to escape algorithm ban :)
                i = 15
                
                
                
            




inst = Instagram(username , password)
inst.unfollowtounFollowers()




