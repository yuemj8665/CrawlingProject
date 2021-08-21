from selenium import webdriver
import csv
import time

# chrome 창 열기
driver = webdriver.Chrome("../chromedriver.exe")
# 카카오 맵 실행
driver.get("https://map.kakao.com/")

# 맵 실행하면 화면 전체를 뭔가가 덮고있는데, 그걸 클릭해서 없애준다.
firstClick = driver.find_element_by_css_selector("div.DimmedLayer")
firstClick.click()

# 검색 박스 설정 후 검색어 입력
sendbox = driver.find_element_by_id("search.keyword.query")
sendbox.send_keys("카페")

# 검색어 입력 후 검색 버튼 클릭
driver.find_element_by_id("search.keyword.submit").click()
time.sleep(1)

# 장소 더보기 클릭
driver.find_element_by_css_selector("a#info\.search\.place\.more.more").click()
time.sleep(1)

# 1페이지부터 시작하기 위한 변수
number = 1
csvNumber = 1

# CSV 파일을 만든다!
csvfile = open("./test.csv",'w',newline='')
wr = csv.writer(csvfile)

while True:
    # 페이징을 한번씩 클릭해준다.
    paging = driver.find_element_by_id("info.search.page.no"+str(number)).click()
    # 페이지 읽어오는 3초의 대기시간
    time.sleep(3)

    # 찾은 검색 결과의 박스들을 잡는다.
    searchBoxes = driver.find_elements_by_css_selector("li.PlaceItem.clickArea")

    # paging 다음버튼 클릭하기 위해 사용한다.
    nextButton = driver.find_element_by_id("info.search.page.next")

    # 본격적으로 긁어온다.
    for searchBox in searchBoxes:
        # 카페이름
        title = searchBox.find_element_by_css_selector("a.link_name").get_attribute("title")
        # 카페 주소
        address_front = searchBox.find_element_by_css_selector("div.addr p").get_attribute("title")
        wr.writerow([csvNumber,title,address_front])
        csvNumber += 1

    # 페이징이 5페이지씩 되어있으므로, 다섯 페이지마다 크롤링이 끝나면 다음화살표 버튼을 입력한다.
    if number%5 == 0:
        nextButton.click()
        number = 0

    # 다음 페이지로 갑시다.
    number += 1
    time.sleep(2)










