from selenium import webdriver
import time, loginInfo



browser = webdriver.Firefox()
browser.get("https://twitter.com/")
time.sleep(1)


###### AUTO LOGIN


loginPage = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
loginPage.click()
time.sleep(2)       ### sets the time(seconds) you wait on that page

usernameInput = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
passwordInput = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
loginButton = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")

usernameInput.send_keys(loginInfo.username)
passwordInput.send_keys(loginInfo.password)

loginButton.click()
time.sleep(2)       ### sets the time(seconds) you wait on that page


##################


###### SEARCH FOR A HASHTAG


searchFıeld = browser.find_element_by_xpath("//*[@id='search-query']") 
searchButton = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[3]/div/form/span/button")

searchFıeld.send_keys("#worldsugliestdog")   ### change input to search something else
searchButton.click()
time.sleep(2)       ### sets the time(seconds) you wait on that page


##################


###### SCROLLS TO BOTTOM OF THE PAGE


lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):    ## CONTINUES TO SCROLL UNTIL THE BOTTOM
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:  ## IF SCROLLED TO BOTTOM OF THE PAGE STOPS LOOP
        match=True
time.sleep(5)


##################


##### AUTO LIKE/UNDO LIKE TWEETS


likeTweet = browser.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")
undoLike = browser.find_elements_by_css_selector(".ProfileTweet-actionButtonUndo.ProfileTweet-action--unfavorite.u-linkClean.js-actionButton.js-actionFavorite")


for item in undoLike:  ##### CHANGE TO likeTweet or undoLike
    try:
        item.click()
        time.sleep(1)
    except Exception:
        print("Error accoured.")    ### RAISES ERROR IF LIKE/DISLIKE DOESN'T WORK


time.sleep(3)

browser.close()








