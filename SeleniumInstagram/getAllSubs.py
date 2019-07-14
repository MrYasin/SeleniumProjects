from selenium import webdriver
import time, loginInfo

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")

time.sleep(2)

### IF YOU HAVE A SAVED ACCOUNT AND WANT TO CHANGE ACCOUNTS

"""

switch_acc = browser.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[1]/div/div[3]/span/button")
switch_acc.click()

"""

### IF YOU DON'T HAVE A SAVED ACCOUNT



logIn = browser.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[2]/p/a")
logIn.click()



# LOGIN PAGE

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
logInButton = browser.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(1) ### LOGIN BUTTON ACTIVATION AFTER SEND_KEYS

logInButton.click()

time.sleep(4)


###### AFTER LOGIN NOTIFICATIONS POP-UP

notNow = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")        #NOT NOW
notNow.click()

"""

turnOn = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[1]")        #TURN ON
turnOn.click()

"""


# NAVIGATION TO USER PAGE

userPage = browser.find_element_by_xpath("/html/body/span/section/nav/div[2]/div/div/div[3]/div/div[3]/a")
userPage.click()

time.sleep(4)



######################## COLLECT FOLLOWERS



# FOLLOWERS PAGE

followersButton = browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[2]/a")
followersButton.click()

time.sleep(3)


    ##### SCROLL FOR FOLLOWERS PAGE


jsCommand = """

followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;

"""


lenOfPage = browser.execute_script(jsCommand)
match=False
while(match==False):    ## CONTINUES TO SCROLL UNTIL THE BOTTOM
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jsCommand)
    if lastCount == lenOfPage:  ## IF SCROLLED TO BOTTOM OF THE PAGE STOPS LOOP
        match=True

time.sleep(5)

    
    #####


# FOLLOWERS LIST

followersList = []

followers =  browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for person in followers:

    followersList.append(person.text)

with open("followers.txt", "w", encoding="UTF-8") as file:
    for i in followersList:

        file.write(i + "\n")
        file.write("--------------------------------------------\n")

time.sleep(1)


# CLOSE FOLLOWERS PAGE

exitButton = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button/span")
exitButton.click() 



######################## COLLECT FOLLOWING



# FOLLOWING PAGE

followingButton = browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a")
followingButton.click()


time.sleep(3)


    ##### SCROLL FOR FOLLOWING PAGE


jsCommand_2 = """

following = document.querySelector(".isgrP");
following.scrollTo(0, following.scrollHeight);
var lenOfPage = following.scrollHeight;
return lenOfPage;

"""


lenOfPage = browser.execute_script(jsCommand_2)
match=False
while(match==False):    ## CONTINUES TO SCROLL UNTIL THE BOTTOM
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jsCommand_2)
    if lastCount == lenOfPage:  ## IF SCROLLED TO BOTTOM OF THE PAGE STOPS LOOP
        match=True

time.sleep(5)


# FOLLOWING LIST

followingList = []

following =  browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for person in following:

    followingList.append(person.text)

with open("following.txt", "w", encoding="UTF-8") as file:
    for i in followingList:

        file.write(i + "\n")
        file.write("--------------------------------------------\n")

time.sleep(1)


####################### COLLECT HASHTAGS YOU FOLLOW


## HASHTAG PAGE


hashButton = browser.find_element_by_xpath("/html/body/div[3]/div/nav/a[2]/button")
hashButton.click()


time.sleep(2)




# HASHTAG LIST

hashList = []

hashtags =  browser.find_elements_by_css_selector(".hI7cq")

for hashtag in hashtags:

    hashList.append(hashtag.text)

with open("hashtags.txt", "w", encoding="UTF-8") as file:
    for i in hashList:

        file.write(i + "\n")
        file.write("--------------------------------------------\n")

time.sleep(1)


browser.close()


