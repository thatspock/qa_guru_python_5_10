import allure
from selene import browser, by, be


class AllureSteps:
    @allure.step('Open main page')
    def open_main_page(self):
        browser.open('/')

    @allure.step('Find github repository {repo}')
    def search_for_repository(self, repo):
        browser.element('.header-search-input').type(repo).submit()

    @allure.step('Click on repository link {repo}')
    def go_to_repository(self, repo):
        browser.element(by.link_text(repo)).click()

    @allure.step('Click on issue tab')
    def go_to_issue_tab(self):
        browser.element('#issues-tab').click()

    @allure.step('Find issue #{number} by text')
    def find_issue_by_text(self, number):
        browser.element(by.partial_text(f'#{number}')).should(be.visible)
