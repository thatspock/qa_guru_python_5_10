import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Tasks in repository')
    allure.dynamic.story("Unauthorized user can't create a task in repository")
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'mr spock')
@allure.feature('Tasks in repository')
@allure.story("Authorized user can create a task in repository")
@allure.link('https://github.com', name='Testing')
def test_steps_labels():
    pass
