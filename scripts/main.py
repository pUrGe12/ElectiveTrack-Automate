from .imports import *
from .functions import oddClick, evenClick, goBack, searchForItem, login

username = input("enter username: ")
password = getpass.getpass("enter password: ")
rollNumber = input("enter the girl's roll number: ")

options = Options()
options.add_argument('--headless=new')

home_directory = os.path.expanduser("~")
file_path = os.path.join(home_directory, "Desktop" , "chromedriver")

service = webdriver.ChromeService(executable_path= file_path, options=options) # path to chromedriver executable
driver = webdriver.Chrome(service = service)
driver.get('https://academic.iitm.ac.in')

# CS: 8, DSAI: 10, HS: 14, MA: 15, PH: 23

departments = [8,10,14,15,23]
login(username, password)

driver.find_element(By.CSS_SELECTOR, 'li.dropdown:nth-child(3) > a:nth-child(1)').click() # click the courses button 
driver.find_element(By.CSS_SELECTOR, 'li.dropdown:nth-child(3) > ul:nth-child(2) > li:nth-child(3) > a:nth-child(1)').click() # click the 3rd option for slotwise list
driver.find_element(By.CSS_SELECTOR, '#period > option:nth-child(2)').click() # check the period

for departmentCode in departments:
	driver.find_element(By.CSS_SELECTOR, f"#department_code > option:nth-child({departmentCode})").click() # check the course
	driver.find_element(By.CSS_SELECTOR, '#slot_view').click() # click the view button
	
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to the bottom
	
	numC = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#slot_tables_info")))
	numColumns = math.ceil(int(numC.text.split(' ')[-2])/10)

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to the bottom
	
	time.sleep(2)
	columns = 0
	while columns <= numColumns: # this range is dependent on the department
		if int(driver.find_element(By.CSS_SELECTOR, "#slot_tables_info").text.split(' ')[-4]) != int(driver.find_element(By.CSS_SELECTOR, "#slot_tables_info").text.split(' ')[-2]):
			for row in range(1, 10, 2): # there are 10 rows
				try:
					time.sleep(1)
					oddClick(row)
					numEntries = searchForItem(rollNumber)
					if numEntries.split(' ')[1] == '1':
						print(driver.find_element(By.CSS_SELECTOR ,'table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9)').text)
					goBack()
					time.sleep(1)
					evenClick(row+1)
					numEntries = searchForItem(rollNumber)
					if numEntries.split(' ')[1] == '1':
						print(driver.find_element(By.CSS_SELECTOR ,'table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9)').text)
					goBack()
				except Exception:
					continue
			try:
				time.sleep(1)
				driver.find_element(By.CSS_SELECTOR, '#slot_tables_next').click()
			except ElementClickInterceptedException:
				pass
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll to the bottom
			time.sleep(2)
		else:
			for row in range(1, int(driver.find_element(By.CSS_SELECTOR, "#slot_tables_info").text.split(' ')[-2]) % 10, 2):
				try:
					time.sleep(1)
					oddClick(row)
					numEntries = searchForItem(rollNumber)
					if numEntries.split(' ')[1] == '1':
						print(driver.find_element(By.CSS_SELECTOR ,'table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9)').text)
					goBack()
					time.sleep(1)
					evenClick(row+1)
					numEntries = searchForItem(rollNumber)
					if numEntries.split(' ')[1] == '1':
						print(driver.find_element(By.CSS_SELECTOR ,'table.table:nth-child(3) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9)').text)
					goBack()
				except Exception:
					break
		columns += 1
