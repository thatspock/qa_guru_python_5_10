from selene import browser, by, be


def test_github_selene():
    browser.open('/')
    browser.element('.header-search-input').type('eroshenkoam/allure-example').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#81')).should(be.visible)
