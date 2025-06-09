import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keycode_map = {
    'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33,
    'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38,
    'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43,
    'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48,
    'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53,
    'z': 54, ' ': 62, '-': 69
}

@pytest.fixture(scope="module")
def driver():
    caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.microsoft.office.onenote",
        "appActivity": "com.microsoft.office.onenote.MainActivity",
        "automationName": "UiAutomator2",
        "noReset": True,
    }

    options = UiAutomator2Options()
    options.load_capabilities(caps)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

def test_input_using_press_keycode(driver):
    wait = WebDriverWait(driver, 20)

    # Tạo trang mới
    new_page_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Create a new page")
    ))
    new_page_btn.click()
    time.sleep(2)

    # Tap vào vùng canvas
    size = driver.get_window_size()
    x = size['width'] // 2
    y = size['height'] // 2
    driver.tap([(x, y)], 500)
    time.sleep(1)

    # Nhập "hello appium"
    text = "hello appium "
    for ch in text:
        code = keycode_map.get(ch.lower())
        if code:
            driver.press_keycode(code)
    time.sleep(0.5)

    # Quay lại
    back_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Back")
    ))
    back_btn.click()
    time.sleep(1)

def test_edit_note_and_add_todo_items(driver):
    wait = WebDriverWait(driver, 20)

    # Mở ghi chú cũ chứa text đã tạo trước
    note = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("hello appium")')
    ))
    note.click()
    time.sleep(2)

    # Tap để focus canvas
    size = driver.get_window_size()
    x = size['width'] // 2
    y = size['height'] // 2
    driver.tap([(x, y)], 500)
    time.sleep(1)

    # Nhấn To Do Button
    todo_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("To Do Button")')
    ))
    todo_btn.click()
    time.sleep(1)

    # Nhập "check" và Enter
    for ch in "check":
        driver.press_keycode(keycode_map.get(ch))
    driver.press_keycode(66)  # Enter
    time.sleep(0.5)

    # Nhập "done"
    for ch in "done":
        driver.press_keycode(keycode_map.get(ch))
    time.sleep(0.5)

    # Nhấn lại To Do Button
    todo_btn.click()
    time.sleep(1)

    # Quay lại
    back_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Back")
    ))
    back_btn.click()
    time.sleep(1)

def test_delete_note(driver):
    wait = WebDriverWait(driver, 20)

    # Mở ghi chú
    note = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("hello appium")')
    ))
    note.click()
    time.sleep(2)

    # Nhấn vào "More options"
    more_options_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "More options")
    ))
    more_options_btn.click()
    time.sleep(2)  # ← Tăng delay cho bottom sheet mở ra hoàn toàn

    # Scroll nếu cần thiết
    try:
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().resourceId("com.microsoft.office.onenote:id/delete"))'
        )
    except:
        pass  # Có thể không cần scroll nếu nút hiển thị sẵn

    # Nhấn Delete
    delete_btn = wait.until(EC.element_to_be_clickable(
        (AppiumBy.ID, "com.microsoft.office.onenote:id/delete")
    ))
    delete_btn.click()

    # Xác nhận nếu có
    try:
        confirm_btn = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("DELETE")')
        ))
        confirm_btn.click()
    except:
        pass
    
    try:
        confirm_btn = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "android:id/button1")
        ))
        confirm_btn.click()
    except:
        pass 
    time.sleep(2)