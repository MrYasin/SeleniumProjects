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


searchField = browser.find_element_by_xpath("//*[@id='search-query']") 
searchButton = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/div[3]/div/form/span/button")

searchField.send_keys("#worldsugliestdog")   ### change input to search something else
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


###### COLLECT TWEETS

allTweets = browser.find_elements_by_css_selector(".TweetTextSize.js-tweet-text.tweet-text")
tweets = list()

for tweet in allTweets:

    tweets.append(tweet.text)

tweetCount = 1

with open("tweets.txt", "w", encoding="UTF-8") as file:
    for tweet in tweets:

        file.write(str(tweetCount) + ": \n" + tweet + "\n")
        file.write("--------------------------------------------\n")
        tweetCount += 1

time.sleep(2)       ### sets the time(seconds) you wait on that page

##################



browser.close()        ### CLOSES THE BROWSER

