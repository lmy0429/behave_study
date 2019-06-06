from behave import *
from API.api import *
from data import search
from features.environment import before_all


# def setup(context):
#     global run
#     run = Testbase(context)
#


@given('open baidu')
def open(context):
    context.driver.openurl('https://www.baidu.com')


@when('input data and click search')
def searchthing(context):
    context.driver.send_key(search.searchinput, search.search)
    context.driver.click(search.submit)


@then('i will look the search result')
def ass(context):
    context.driver.assertelementdisplayed(search.assert1)
    print('132132132')
