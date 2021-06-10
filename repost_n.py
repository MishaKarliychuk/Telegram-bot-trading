from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

login = 'bkrt_bot'
password = 'drugs666'

def repost(from_):
    global login, password

    dr = webdriver.Chrome()

    if 'VK' in from_:
        dr.get('https://vk.com/bkrt_inc')
        sleep(3)
        #
        try:
            dr.find_element_by_class_name('JoinForm__notNow').click()
            sleep(3)
        except:
            pass
        try:
            dr.find_elements_by_class_name('wall_post_text')[1].click()
            sleep(3)
        except:
            pass
        dr.find_element_by_class_name('JoinForm__notNow').click()
        sleep(3)
        try:
            dr.find_elements_by_class_name('wall_post_text')[1].click()
            sleep(3)
        except:
            pass
        try:
            dr.find_element_by_class_name('JoinForm__notNow').click()
        except:
            pass
        try:
            dr.find_elements_by_class_name('wall_post_text')[1].click()
        except:
            pass
        sleep(5)
        url_post = dr.current_url
        sleep(1)
        dr.close()
        return str(url_post)

    else:
        #dr.get('https://instagram.com')
        sleep(2)

        # Парсинг поста
        dr.get('https://www.instagram.com/bkrt_inc/')
        sleep(3)
        dr.find_element_by_class_name('v1Nh3.kIKUG._bz0w').click()
        sleep(2)

        # Вход в инсту
        dr.find_element_by_name('username').send_keys(login)
        sleep(2)
        dr.find_element_by_name('password').send_keys(password)
        sleep(3)
        dr.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB').click()
        sleep(3)

        # Отключить увед и тд.
        try:
            dr.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()
            sleep(3)
        except:
            pass

        dr.find_element_by_class_name('v1Nh3.kIKUG._bz0w').click()
        sleep(1)
        url_post = dr.current_url
        dr.close()
        return str(url_post)

#print(repost('sadsad'))