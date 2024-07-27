def oddClick(i):
	try:
		oddElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'tr.odd:nth-child({i}) > td:nth-child(11) > a:nth-child(1)')))
		oddElement.click()
	except Exception:
		pass

def evenClick(i):
	try:
		evenElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'tr.even:nth-child({i}) > td:nth-child(11) > a:nth-child(1)')))
		evenElement.click()
	except Exception:
		pass

def goBack():
	try:
		goBack = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-lg')))
		goBack.click()
	except Exception:
		pass

def searchForItem(rollNumber):
	try:
		element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#sub_wise_filter > label:nth-child(1) > input:nth-child(1)')))
		element.send_keys(rollNumber)
		time.sleep(0.2)
		elementText = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#sub_wise_info')))
		return elementText.text
	except Exception:
		pass

def login(username, password):
	driver.find_element(By.NAME, 'username').send_keys(username)
	driver.find_element(By.NAME, 'password').send_keys(password)
	driver.find_element(By.CSS_SELECTOR, '#submit').click() # click the submit button
	driver.find_element(By.CSS_SELECTOR, '#load_menu_btn').click() # click the student button
