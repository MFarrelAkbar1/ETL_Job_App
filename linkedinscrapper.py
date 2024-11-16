import os
from dotenv import load_dotenv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')

# Log in
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(os.getenv('EMAIL_ADDRESS'))
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(os.getenv('PASSWORD'))
password_field.submit()

# Go to the LinkedIn job search page
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=&geoId=102478259&keywords=developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Wait until the list container is visible
job_list = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'scaffold-layout__list-container')))
# Get all job items in the ordered list
job_items = job_list.find_elements(By.CSS_SELECTOR, '[data-occludable-job-id]')

print(len(job_items))

for index, item in enumerate(job_items):
    try:
        # Click each job 3 times, since sometimes clicking once doesn't work
        item.click()
        item.click()
        item.click()

        # Wait for the job title to appear
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.t-24.t-bold.inline'))
        )

        WebDriverWait(driver, 3)
        wrapper_location_element = driver.find_element(By.CLASS_NAME, "job-details-jobs-unified-top-card__primary-description-container")

        location_element = wrapper_location_element.find_element(By.CLASS_NAME, "t-black--light")
        location = location_element.find_elements(By.CSS_SELECTOR, ".tvm__text.tvm__text--low-emphasis")

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mv5.t-16.pt1.pb1.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--2.artdeco-button--secondary.ember-view')))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mv5.t-16.pt1.pb1.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--2.artdeco-button--secondary.ember-view')))
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', class_='t-24 t-bold inline').get_text().strip()
        company_name = soup.find('div', class_='job-details-jobs-unified-top-card__company-name').get_text().strip()
        li_element = soup.find('li', class_='job-details-jobs-unified-top-card__job-insight')


        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'job-details')))
            job_description_span =  driver.find_element(By.ID, "job-details")
            job_description = job_description_span.get_attribute("innerHTML")

        except Exception as e:
            print(f"{e}")

        print(f"{company_name}")
        print(f"Job {index + 1}: {title}")
        if job_description != None:
            print(f"{job_description}")
        if li_element:
            spans = li_element.find_all('span', dir='ltr')
            for span in spans:
                print(span.get_text())  # Print the text content of each <span>


        skill_button = driver.find_element(By.CSS_SELECTOR, '.mv5.t-16.pt1.pb1.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--2.artdeco-button--secondary.ember-view')
        driver.execute_script("arguments[0].click();", skill_button)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-skill-match-status-list')))


        skill_list = driver.find_element(By.CLASS_NAME, 'job-details-skill-match-status-list')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-skill-match-status-list__unmatched-skill')))
        skill_list_item = driver.find_elements(By.CSS_SELECTOR, '.job-details-skill-match-status-list__unmatched-skill.text-body-small')
        skill_list_obj = []

        for index,skill in enumerate(skill_list_item):
            if skill.text != "Add":
                print(skill.text)
                skill_list_obj.append(skill.text)
        time.sleep(4)
        exit_button = driver.find_element(By.CSS_SELECTOR, '[data-test-modal-close-btn]')
        driver.execute_script("arguments[0].click();", exit_button)

        # Optionally, add a short delay to handle dynamic loading
        time.sleep(4)

    except Exception as e:
        print(f"Error on job {index + 1}: {e}")
        continue



# Optional: close the driver after completion
driver.quit()
