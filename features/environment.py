# encoding: utf-8
from selenium import webdriver
from API import api


def before_all(context):
    context.driver = api.Testbase(webdriver.Chrome())


def after_all(context):
    context.driver.quit()
