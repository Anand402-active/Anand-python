from selenium import webdriver
import time
import csv
# import csv_test
driver = webdriver.Chrome(r"C:\Users\AnandKumar\PycharmProjects\Anandtesting\chromedriver_win32\chromedriver.exe")
driver.get("https://web.whatsapp.com/")#"name = input ("enter name of user or group")
# msg = input ("enter your messsage")
# count=int(input("enter count"))
input('enter anything after QR code scan')
time.sleep(5)
count = 1;
with open('./Files/contacts.csv') as file :
    data=csv.reader(file)
    for row in data:
        name=row[0].split("\t")[0]  #for selecting the name
        msg = row[0].split("\t")[1] #for selecting the msg
        time.sleep(5)
        # with open('./Files/contacts.csv') as file :
        #     name=csv_test.reader(file)
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
        user.click()
        for i in range(count):
            msg_box=driver.find_element_by_class_name('_3u328')
            msg_box.send_keys(msg)
            button=driver.find_element_by_class_name('_3M-N-')
            button.click()
