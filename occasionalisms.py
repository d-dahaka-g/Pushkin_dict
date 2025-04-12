from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)
#

url = 'https://www.google.com/search?q=%D0%B1%D1%8B%D0%B2%D0%B0%D0%BB%D0%BE-%D0%BE%D1%81%D1%82%D1%80%D1%8B%D0%B9&sca_esv=1cf97cdeb544ba54&udm=36&tbs=cdr:1,cd_min:1/1/1700,cd_max:12/31/1906&sxsrf=AHTn8zrxZ4QfEYInR2J6FUGB2ySedTp9Vw:1744463944953&ei=SGj6Z575ObS4i-gPw5GceQ&start=0&sa=N&sstk=Af40H4Uw3phOtj-U8or2Kr4eHSllRJBcE1VsLpFWIJe1EPizX_je-yLLVtYV3bJ1t4s3X4MJyevTqN0PHSX1-1Ty6_VMJPR_66rJEzIgn7MfdShHrVmgICo3MC58NZU9GW7_beg1Uu5vhZop9Rrzbw2Z57JNcf6mOinwfqiNXZpN3Ck53z-p-_llury_zfcNqYNvf0Ybof-cmplhbNiT1hAKl10UdX4T78nefdROXwVrfJzZbxsNxIiZFQHOCB5et8IzGkuSDUIzB6ipGD3610-Z0nThytWe76VGvcrDK3n7urxkQTHUUF1ZMjzCZb5XnznAR15Gcbpwwv_Y4_Fnhfq6zptLZNFOKuq78jc-sz9LDTj27DlKVCquetnkglUMNJIQJq6cQn7ezjek2kTOux9CFe-tIWKnc8bnGgFIm0Y0CePfHMoOEg0&ved=2ahUKEwievYzOytKMAxU03AIHHcMIJw84MhDy0wN6BAgBEAQ&biw=1440&bih=900&dpr=2&ih=824&iw=1440'
driver = webdriver.Chrome(options=options)
driver.get(url)

text = driver.find_elements(by=By.CLASS_NAME, value='cmlJmd ETWPw')
#rso > div:nth-child(1) > div > div > div.bHexk.Tz5Hvf > div.cmlJmd.ETWPw

# for i in range(10):
#     text = driver.find_element(by=By.XPATH, value=f'//*[@id="rso"]/div[{i}]/div/div/div[2]/div[3]/span/span').text
#     print(text)


print(text)