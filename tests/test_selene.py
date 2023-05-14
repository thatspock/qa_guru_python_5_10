import allure
from selene import browser, by, be


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
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    go_to_issue_tab()
    find_issue_by_text('81')


@allure.step('Open main page')
def open_main_page():
    browser.open('/')


@allure.step('Find github repository {repo}')
def search_for_repository(repo):
    browser.element('.header-search-input').type(repo).submit()


@allure.step('Click on repository link {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Click on issue tab')
def go_to_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Find issue #{number} by text')
def find_issue_by_text(number):
    browser.element(by.partial_text(f'#{number}')).should(be.visible)
