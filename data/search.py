from selenium.webdriver.common.by import By

# search
searchinput = (By.ID, 'kw')
search = '风景'
submit = (By.ID, 'su')
assert1 = (By.CLASS_NAME, 'c-gap-bottom-small')
assert2 = (By.CLASS_NAME, 'result-op')
