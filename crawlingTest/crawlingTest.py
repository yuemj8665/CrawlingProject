from selenium import webdriver
import time

# chrome 창 열기
driver = webdriver.Chrome("../chromedriver.exe")

# 네이버 뉴스 헤드라인 가져오기
driver.get("https://news.naver.com/")

headline = driver.find_elements_by_css_selector("div.hdline_article_tit a")

for i in headline:
    print(i.text)

# ## 여기서부터 데이터 수집한다.
# for i in range(999): # 1페이지보터 999페이지까지,
#     time.sleep(3) # 3초의 슬립
#     cafeList = driver.find_elements_by_class_name("head_item clickArea")
#     for c in cafeList:
#         title = c.find_element_by_class_name("link_name").text
#
#     try :
#         print(title)
#     except :
#         break;