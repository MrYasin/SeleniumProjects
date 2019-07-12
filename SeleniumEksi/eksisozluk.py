"""

"""





from selenium import webdriver
import time, random


browser = webdriver.Firefox()
url = ""                    ##### PUT THE URL YOU WANT TO PULL ENTRIES FROM

pageCount = 1
entryCount = 100
entries = list()


while pageCount <= 10 and entryCount <= 100:        ### CHANGE THE VALUES TO YOUR WILL

    randomPage = random.randint(1,1400)             ### GET RANDOM 10 PAGES
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    time.sleep(1)

    elements = browser.find_elements_by_css_selector(".content")             ### GET 100 ENTRIES
    for i in elements:
        entries.append(i.text)

    pageCount += 1

with open("entries.txt", "w", encoding="UTF-8") as file:

    for element in entries:
        file.write(str(entryCount) + ".\n" + element + ".\n")
        entryCount += 1



browser.close()





