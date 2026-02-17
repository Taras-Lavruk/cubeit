from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"
number_to_cube = "5"
number_to_cube_1 = ""

def test_cube(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    input_field.fill(number_to_cube)

    cube_btn = page.get_by_role("button", name="Cube")
    cube_btn.click()
    result = str(int(number_to_cube)*int(number_to_cube)*int(number_to_cube))
    result_field = page.locator("css=p#result")
    expect(result_field).to_contain_text(result)


def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input_field = page.get_by_placeholder("enter number...")
    input_field.fill(number_to_cube_1)

    cube_btn = page.get_by_role("button", name="Cube")
    cube_btn.click()
    result_field = page.locator("css=p#result")
    expect(result_field).to_have_text("Enter something!")

