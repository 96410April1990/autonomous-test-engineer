PLAYWRIGHT_TEMPLATE = """

from playwright.sync_api import Page

def {test_function}{page:Page}:

{test_steps}

"""