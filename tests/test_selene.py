import allure
from selene import browser, by, be

from page_objects.allure_steps import AllureSteps
from tests.config import REPOSITORY, ISSUE_NUMBER


def test_github_selene():
    browser.open('/')
    browser.element('.header-search-input').type('eroshenkoam/allure-example').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#81')).should(be.visible)


def test_github_steps():
    with allure.step('Open main page'):
        browser.open('/')

    with allure.step('Find github repository'):
        browser.element('.header-search-input').type('eroshenkoam/allure-example').submit()

    with allure.step('Click on repository link'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Click on issue tab'):
        browser.element('#issues-tab').click()

    with allure.step('Find issue #81 by text'):
        browser.element(by.partial_text('#81')).should(be.visible)


def test_github_decorator_steps():
    allure_steps = AllureSteps()
    allure_steps.open_main_page()
    allure_steps.search_for_repository(REPOSITORY)
    allure_steps.go_to_repository(REPOSITORY)
    allure_steps.go_to_issue_tab()
    allure_steps.find_issue_by_text(ISSUE_NUMBER)
