#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
try:
    driver.get('https://fitpeo.com')
    wait = WebDriverWait(driver, 10)
    revenue_calc = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Revenue Calculator')))
    revenue_calc.click()
    wait = WebDriverWait(driver, 10)
    slider1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slider')))
    driver.execute_script("arguments[0].scrollIntoView();", slider1)
    wait = WebDriverWait(driver, 10)
    slider2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slider-handle'))) 
    action = ActionChains(driver)
    action.click_and_hold(slider2).move_by_offset(820, 0).release().perform()
    wait = WebDriverWait(driver, 10)
    text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#text-field')))
    text_field.click()
    text_field.clear()
    text_field.send_keys('560')
    wait = WebDriverWait(driver, 10)
    slider_value = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#slider-value')))
    assert slider_value.text == '560', f"Expected slider value to be '560', but got '{slider_value.text}'"
    cpt_codes = [
        'CPT-99091',
        'CPT-99453',
        'CPT-99454',
        'CPT-99474'
    ]
    for code in cpt_codes:
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, f"'//html/body/div[2]/div[1]/div[2]/div[2]/label/span[1]/input', '{code}')]/preceding-sibling::input[@type='checkbox'")))
        if not checkbox.is_selected():
            checkbox.click()
    total_reimbursement = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#total-reimbursement')))
    assert total_reimbursement.text == '$110700', f"Expected total reimbursement to be '$110700', but got '{total_reimbursement.text}'"
finally:
    time.sleep(5) 
    driver.quit()

