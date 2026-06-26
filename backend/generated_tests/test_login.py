# test_login.py

from playwright.sync_api import Page, expect

# --- Configuration ---
# NOTE: Replace these with your actual application URLs and credentials.
# For real-world scenarios, consider using environment variables or a config file.
BASE_URL = "http://localhost:8000"  # Replace with your application's base URL
VALID_USERNAME = "testuser"
VALID_PASSWORD = "password123"
INVALID_USERNAME = "wronguser"
INVALID_PASSWORD = "wrongpass"
LOCKED_USERNAME = "lockeduser"

# Assuming a threshold of 3 failed attempts for lockout
LOCKOUT_THRESHOLD = 3

# --- Helper Functions ---
def navigate_to_login_page(page: Page):
    """Navigates to the login page."""
    page.goto(f"{BASE_URL}/login") # Adjust the path if your login page is different

def assert_on_login_page(page: Page):
    """Asserts that the current page is the login page."""
    # This is a generic check, you might want to assert on a specific element
    # like the username input field or a login form header.
    expect(page.locator("input[name='username']")).to_be_visible()
    expect(page.locator("input[name='password']")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()

def enter_credentials(page: Page, username: str, password: str):
    """Enters username and password into the respective fields."""
    page.locator("input[name='username']").fill(username)
    page.locator("input[name='password']").fill(password)

def click_login(page: Page):
    """Clicks the login button."""
    page.get_by_role("button", name="Login").click()

def assert_successful_login(page: Page):
    """Asserts that the user is successfully logged in and on the dashboard."""
    # This is a placeholder. Replace with actual assertions for your dashboard.
    # For example, check for a welcome message, a specific dashboard element, or the URL.
    expect(page).not_to_contain_text("Login") # Example: Login text should not be on dashboard
    # Example: expect(page.url).to_contain("/dashboard")
    # Example: expect(page.locator("#dashboard-title")).to_be_visible()

def assert_error_message(page: Page, expected_message: str):
    """Asserts that a specific error message is displayed."""
    # This is a generic locator. Adjust based on how your application displays errors.
    # Common selectors: .error-message, div[role="alert"], etc.
    error_locator = page.locator(".error-message, [role='alert']") # Combine common selectors
    expect(error_locator).to_be_visible()
    expect(error_locator).to_have_text(expected_message, ignore_case=True)

def assert_user_is_on_login_page_after_failed_login(page: Page):
    """Asserts that the user remains on the login page after a failed login attempt."""
    assert_on_login_page(page)


# --- Test Cases ---

def test_login_tc_001_successful_login(page: Page):
    """LOGIN_TC_001: Verify successful login with valid username and password."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username into the username field.
    page.locator("input[name='username']").fill(VALID_USERNAME)
    expect(page.locator("input[name='username']")).to_have_value(VALID_USERNAME)

    # Step 3: Enter the corresponding valid password into the password field.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    # For password fields, we might not check the exact value due to masking,
    # but we can check if it's filled and masked.
    password_input = page.locator("input[name='password']")
    expect(password_input).to_have_value(VALID_PASSWORD) # Playwright often returns the actual value
    # If masking is expected, you might check type attribute or visual representation if needed.

    # Step 4: Click the 'Login' button.
    click_login(page)
    assert_successful_login(page)


def test_login_tc_002_invalid_password(page: Page):
    """LOGIN_TC_002: Verify login rejection with an invalid password."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username into the username field.
    page.locator("input[name='username']").fill(VALID_USERNAME)
    expect(page.locator("input[name='username']")).to_have_value(VALID_USERNAME)

    # Step 3: Enter an invalid password into the password field.
    page.locator("input[name='password']").fill(INVALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(INVALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Assert that an error message is displayed and user stays on login page
    assert_error_message(page, "Invalid username or password") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_003_invalid_username(page: Page):
    """LOGIN_TC_003: Verify login rejection with an invalid username."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter an invalid username into the username field.
    page.locator("input[name='username']").fill(INVALID_USERNAME)
    expect(page.locator("input[name='username']")).to_have_value(INVALID_USERNAME)

    # Step 3: Enter any password into the password field.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Assert that an error message is displayed and user stays on login page
    assert_error_message(page, "Invalid username or password") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_004_empty_username(page: Page):
    """LOGIN_TC_004: Verify login rejection with empty username field."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Leave the username field empty.
    # The field is already empty on page load, but we can ensure it.
    page.locator("input[name='username']").fill("")
    expect(page.locator("input[name='username']")).to_have_value("")

    # Step 3: Enter a valid password into the password field.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Assert that an error message is displayed for the required username
    assert_error_message(page, "Username is required") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_005_empty_password(page: Page):
    """LOGIN_TC_005: Verify login rejection with empty password field."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username into the username field.
    page.locator("input[name='username']").fill(VALID_USERNAME)
    expect(page.locator("input[name='username']")).to_have_value(VALID_USERNAME)

    # Step 3: Leave the password field empty.
    page.locator("input[name='password']").fill("")
    expect(page.locator("input[name='password']")).to_have_value("")

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Assert that an error message is displayed for the required password
    assert_error_message(page, "Password is required") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_006_empty_username_and_password(page: Page):
    """LOGIN_TC_006: Verify login rejection with both username and password fields empty."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Leave both the username and password fields empty.
    page.locator("input[name='username']").fill("")
    page.locator("input[name='password']").fill("")
    expect(page.locator("input[name='username']")).to_have_value("")
    expect(page.locator("input[name='password']")).to_have_value("")

    # Step 3: Click the 'Login' button.
    click_login(page)
    # Assert that error messages are displayed for both required fields
    assert_error_message(page, "Username is required") # Adjust message as per application
    # The specific error message for password might be separate or combined. Adapt this.
    # For example, if there are multiple error messages, you might check for both.
    # expect(page.locator(".error-message").all_text_contents()).to_contain("Username is required")
    # expect(page.locator(".error-message").all_text_contents()).to_contain("Password is required")
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_007_locked_user(page: Page):
    """LOGIN_TC_007: Verify that a locked user cannot log in."""
    # Step 1: Ensure a specific user account is marked as locked in the system.
    # This is typically an administrative task or setup step, not directly automated in this test.
    # We assume LOCKED_USERNAME refers to an account that is indeed locked.

    # Step 2: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 3: Enter the valid username of the locked account into the username field.
    page.locator("input[name='username']").fill(LOCKED_USERNAME)
    expect(page.locator("input[name='username']")).to_have_value(LOCKED_USERNAME)

    # Step 4: Enter any password into the password field.
    page.locator("input[name='password']").fill(VALID_PASSWORD) # Password doesn't matter for locked account
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 5: Click the 'Login' button.
    click_login(page)
    # Assert that an error message indicating the account is locked is displayed.
    assert_error_message(page, "Account is locked") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_008_account_lockout(page: Page):
    """LOGIN_TC_008: Verify account lockout after multiple failed login attempts."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username into the username field.
    page.locator("input[name='username']").fill(VALID_USERNAME)
    expect(page.locator("input[name='username']")).to_have_value(VALID_USERNAME)

    # Step 3 & 4: Enter an incorrect password and click 'Login'. Repeat for (Threshold - 1) times.
    for i in range(LOCKOUT_THRESHOLD - 1):
        page.locator("input[name='password']").fill(INVALID_PASSWORD + str(i))
        click_login(page)
        assert_error_message(page, "Invalid username or password") # Or a more specific message for failed attempt
        assert_user_is_on_login_page_after_failed_login(page)

    # Step 6: After (Threshold - 1) failed attempts, attempt to login again with the same valid username and incorrect password.
    page.locator("input[name='password']").fill(INVALID_PASSWORD + str(LOCKOUT_THRESHOLD - 1))
    click_login(page)
    # Assert that an error message indicating the account has been locked is displayed.
    assert_error_message(page, "Account locked due to too many failed attempts") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)

    # Step 7: Attempt to login with the correct username and correct password for the locked account.
    # We expect this to also fail with a lockout message since the account is now locked.
    page.locator("input[name='username']").fill(VALID_USERNAME)
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    click_login(page)
    assert_error_message(page, "Account is locked") # Adjust message as per application (this might be the same as TC_007)
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_009_username_leading_trailing_spaces(page: Page):
    """LOGIN_TC_009: Verify login with username containing leading/trailing spaces."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username with leading spaces.
    username_with_leading_spaces = "  " + VALID_USERNAME
    page.locator("input[name='username']").fill(username_with_leading_spaces)
    expect(page.locator("input[name='username']")).to_have_value(username_with_leading_spaces)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting that leading spaces are trimmed and login is successful
    assert_successful_login(page)

    # Step 5: Repeat for trailing spaces.
    navigate_to_login_page(page) # Re-navigate to reset state
    username_with_trailing_spaces = VALID_USERNAME + "  "
    page.locator("input[name='username']").fill(username_with_trailing_spaces)
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    click_login(page)
    assert_successful_login(page)

    # Step 6: Repeat for both leading and trailing spaces.
    navigate_to_login_page(page)
    username_with_both_spaces = "  " + VALID_USERNAME + "  "
    page.locator("input[name='username']").fill(username_with_both_spaces)
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    click_login(page)
    assert_successful_login(page)


def test_login_tc_010_password_leading_trailing_spaces(page: Page):
    """LOGIN_TC_010: Verify login with password containing leading/trailing spaces."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter the corresponding valid password with leading spaces.
    password_with_leading_spaces = "  " + VALID_PASSWORD
    page.locator("input[name='password']").fill(password_with_leading_spaces)
    expect(page.locator("input[name='password']")).to_have_value(password_with_leading_spaces)

    # Step 4: Click the 'Login' button.
    # Expecting that leading spaces are NOT trimmed and login is successful.
    click_login(page)
    assert_successful_login(page)

    # Step 5: Repeat for trailing spaces.
    navigate_to_login_page(page)
    page.locator("input[name='username']").fill(VALID_USERNAME)
    password_with_trailing_spaces = VALID_PASSWORD + "  "
    page.locator("input[name='password']").fill(password_with_trailing_spaces)
    expect(page.locator("input[name='password']")).to_have_value(password_with_trailing_spaces)
    click_login(page)
    assert_successful_login(page)

    # Step 6: Repeat for both leading and trailing spaces.
    navigate_to_login_page(page)
    page.locator("input[name='username']").fill(VALID_USERNAME)
    password_with_both_spaces = "  " + VALID_PASSWORD + "  "
    page.locator("input[name='password']").fill(password_with_both_spaces)
    expect(page.locator("input[name='password']")).to_have_value(password_with_both_spaces)
    click_login(page)
    assert_successful_login(page)


def test_login_tc_011_case_sensitive_username(page: Page):
    """LOGIN_TC_011: Verify login with case-sensitive username."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username in a different case.
    # Assuming VALID_USERNAME is 'testuser', we use 'TEST_USER'.
    different_case_username = VALID_USERNAME.upper() if VALID_USERNAME != VALID_USERNAME.upper() else VALID_USERNAME + "_UPPERCASE"
    if different_case_username == VALID_USERNAME:
        print("Skipping case-sensitive username test: Username might not have distinct upper/lower cases.")
        return # Skip if username is already case-insensitive
    
    page.locator("input[name='username']").fill(different_case_username)
    expect(page.locator("input[name='username']")).to_have_value(different_case_username)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting login to fail due to case sensitivity.
    assert_error_message(page, "Invalid username or password") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_012_case_sensitive_password(page: Page):
    """LOGIN_TC_012: Verify login with case-sensitive password."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter the corresponding valid password in a different case.
    # Assuming VALID_PASSWORD is 'password123', we use 'PASSWORD123'.
    different_case_password = VALID_PASSWORD.upper() if VALID_PASSWORD != VALID_PASSWORD.upper() else VALID_PASSWORD + "_UPPERCASE"
    if different_case_password == VALID_PASSWORD:
        print("Skipping case-sensitive password test: Password might not have distinct upper/lower cases.")
        return # Skip if password is already case-insensitive

    page.locator("input[name='password']").fill(different_case_password)
    expect(page.locator("input[name='password']")).to_have_value(different_case_password)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting login to fail due to case sensitivity.
    assert_error_message(page, "Invalid username or password") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_013_special_chars_username(page: Page):
    """LOGIN_TC_013: Verify login with special characters in username."""
    # Define a username with allowed special characters. Adjust characters as per your system's rules.
    allowed_special_chars_username = "test_user.name-123+more"
    valid_password_for_special_user = "securepass"

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username containing allowed special characters.
    page.locator("input[name='username']").fill(allowed_special_chars_username)
    expect(page.locator("input[name='username']")).to_have_value(allowed_special_chars_username)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(valid_password_for_special_user)
    expect(page.locator("input[name='password']")).to_have_value(valid_password_for_special_user)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # This test assumes these special characters are allowed and will result in a successful login.
    # If they are not allowed, the test should expect an error message (see TC_015).
    assert_successful_login(page)


def test_login_tc_014_special_chars_password(page: Page):
    """LOGIN_TC_014: Verify login with special characters in password."""
    # Define a password with special characters. Adjust characters as per your system's rules.
    special_chars_password = "P@sswOrd!#$^*%&()_+=-[]{}"

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter the corresponding valid password containing special characters.
    page.locator("input[name='password']").fill(special_chars_password)
    expect(page.locator("input[name='password']")).to_have_value(special_chars_password)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # This test assumes these special characters are allowed and will result in a successful login.
    # If they are not allowed, the test should expect an error message (see TC_016).
    assert_successful_login(page)


def test_login_tc_015_disallowed_chars_username(page: Page):
    """LOGIN_TC_015: Verify behavior with username containing disallowed characters."""
    # Define a username with characters that are typically disallowed.
    disallowed_chars_username = "user<">;?/|\test"
    corresponding_password = VALID_PASSWORD # Assuming password is valid

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a username containing disallowed characters.
    page.locator("input[name='username']").fill(disallowed_chars_username)
    # Depending on frontend validation, the input might be accepted or prevented.
    # We'll assume it's accepted for the sake of testing the backend validation on login click.
    expect(page.locator("input[name='username']")).to_have_value(disallowed_chars_username)

    # Step 3: Enter the corresponding password.
    page.locator("input[name='password']").fill(corresponding_password)
    expect(page.locator("input[name='password']")).to_have_value(corresponding_password)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting an error message for invalid characters.
    assert_error_message(page, "Invalid characters in username") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_016_disallowed_chars_password(page: Page):
    """LOGIN_TC_016: Verify behavior with password containing disallowed characters."""
    # Define a password with characters that are typically disallowed.
    disallowed_chars_password = "pass<>";?/|\test"

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter a password containing disallowed characters.
    page.locator("input[name='password']").fill(disallowed_chars_password)
    # Assuming it's accepted for the sake of testing backend validation.
    expect(page.locator("input[name='password']")).to_have_value(disallowed_chars_password)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting an error message for invalid characters.
    assert_error_message(page, "Invalid characters in password") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_017_max_username_length(page: Page):
    """LOGIN_TC_017: Verify login with maximum allowed username length."""
    # NOTE: You need to know the maximum allowed username length for your system.
    # Let's assume it's 50 characters for this example.
    MAX_USERNAME_LENGTH = 50
    # Ensure VALID_USERNAME is shorter than MAX_USERNAME_LENGTH
    if len(VALID_USERNAME) >= MAX_USERNAME_LENGTH:
        print("Skipping max username length test: VALID_USERNAME is already at or exceeds max length.")
        return

    max_length_username = "a" * (MAX_USERNAME_LENGTH - len(VALID_USERNAME)) + VALID_USERNAME
    # Ensure the generated username is exactly MAX_USERNAME_LENGTH
    assert len(max_length_username) == MAX_USERNAME_LENGTH

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username exactly at the maximum allowed length.
    page.locator("input[name='username']").fill(max_length_username)
    expect(page.locator("input[name='username']")).to_have_value(max_length_username)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    assert_successful_login(page)


def test_login_tc_018_username_exceeding_max_length(page: Page):
    """LOGIN_TC_018: Verify login with username length exceeding the maximum."""
    MAX_USERNAME_LENGTH = 50 # Assume max length is 50
    # Generate a username that is one character longer than the max allowed length.
    username_exceeding_max = "a" * (MAX_USERNAME_LENGTH + 1)

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Attempt to enter a username that exceeds the maximum allowed length.
    page.locator("input[name='username']").fill(username_exceeding_max)
    # We expect the input to be either prevented or truncated.
    # Let's check the actual value in the field after attempting to fill.
    entered_username_value = page.locator("input[name='username']").input_value()

    # Step 3: If truncated, verify the entered username is at the maximum length.
    # This depends on the implementation. Some systems might allow typing but truncate on submit.
    # Others prevent typing past the limit. For this test, we assume truncation happens.
    if len(entered_username_value) > MAX_USERNAME_LENGTH:
        # If it's not truncated, this part of the test might be invalid for this specific UI.
        # We will assert based on truncation.
        print(f"Warning: Username input was not truncated to {MAX_USERNAME_LENGTH} characters. Actual: {entered_username_value}")
        # Fallback assertion: Check if it's exactly the max length after potential truncation
        assert len(entered_username_value) <= MAX_USERNAME_LENGTH, "Username input exceeded max length and was not truncated."
    
    # If the system enforces the max length by preventing input:
    # expect(page.locator("input[name='username']")).to_have_value(username_exceeding_max[:MAX_USERNAME_LENGTH])

    # Step 4: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)

    # Step 5: Click the 'Login' button.
    click_login(page)

    # Step 5 (Expected Result Interpretation):
    # If the system correctly truncated the username to a valid one (e.g., if the original VALID_USERNAME
    # was part of the truncated string), login might succeed.
    # However, if the system strictly enforces length and rejects truncated/invalid inputs,
    # it should show an error. The most robust expectation is that it should NOT succeed with the oversized input.
    # We'll test for a failure or an error related to length if possible.
    # If the system truncates and the result is valid, it might pass. Let's assume failure for stricter validation.
    
    # Attempt to assert successful login IF the truncated username is valid.
    # If the test fails here, it means either truncation didn't happen as expected, 
    # or the truncated username is invalid, or the system shows an error.
    try:
        assert_successful_login(page)
    except:
        # If not successful, assert that it failed with a reasonable error message.
        # The exact error might be 'Username too long' or 'Invalid username'.
        assert_error_message(page, "Username is too long" or "Invalid username or password") # Adapt message
        assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_019_min_username_length(page: Page):
    """LOGIN_TC_019: Verify login with minimum allowed username length (if applicable)."""
    # NOTE: You need to know the minimum allowed username length. Let's assume it's 3.
    MIN_USERNAME_LENGTH = 3
    min_length_username = "a" * MIN_USERNAME_LENGTH

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username exactly at the minimum allowed length.
    page.locator("input[name='username']").fill(min_length_username)
    expect(page.locator("input[name='username']")).to_have_value(min_length_username)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # This test assumes the minimum length is enforced and a username of that length is valid.
    # If it's not, the test would need to assert for an error. For now, positive assertion.
    assert_successful_login(page)


def test_login_tc_020_username_below_min_length(page: Page):
    """LOGIN_TC_020: Verify login with username length below the minimum."""
    MIN_USERNAME_LENGTH = 3 # Assume minimum is 3
    # Create a username shorter than the minimum.
    username_below_min = "a" * (MIN_USERNAME_LENGTH - 1)

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a username that is shorter than the minimum allowed length.
    page.locator("input[name='username']").fill(username_below_min)
    expect(page.locator("input[name='username']")).to_have_value(username_below_min)

    # Step 3: Enter the corresponding password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting an error message indicating the username is too short.
    assert_error_message(page, "Username is too short") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_021_max_password_length(page: Page):
    """LOGIN_TC_021: Verify login with maximum allowed password length."""
    # NOTE: You need to know the maximum allowed password length for your system.
    # Let's assume it's 128 characters.
    MAX_PASSWORD_LENGTH = 128
    # Ensure VALID_PASSWORD is shorter than MAX_PASSWORD_LENGTH.
    if len(VALID_PASSWORD) >= MAX_PASSWORD_LENGTH:
        print("Skipping max password length test: VALID_PASSWORD is already at or exceeds max length.")
        return

    max_length_password = "p" * (MAX_PASSWORD_LENGTH - len(VALID_PASSWORD)) + VALID_PASSWORD
    # Ensure the generated password is exactly MAX_PASSWORD_LENGTH
    assert len(max_length_password) == MAX_PASSWORD_LENGTH

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter a valid password exactly at the maximum allowed length.
    page.locator("input[name='password']").fill(max_length_password)
    expect(page.locator("input[name='password']")).to_have_value(max_length_password)

    # Step 4: Click the 'Login' button.
    click_login(page)
    assert_successful_login(page)


def test_login_tc_022_password_exceeding_max_length(page: Page):
    """LOGIN_TC_022: Verify login with password length exceeding the maximum."""
    MAX_PASSWORD_LENGTH = 128 # Assume max length is 128
    # Generate a password that is one character longer than the max allowed length.
    password_exceeding_max = "p" * (MAX_PASSWORD_LENGTH + 1)

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Attempt to enter a password that exceeds the maximum allowed length.
    page.locator("input[name='password']").fill(password_exceeding_max)
    entered_password_value = page.locator("input[name='password']").input_value()

    # Step 4: If truncated, verify the entered password is at the maximum length.
    if len(entered_password_value) > MAX_PASSWORD_LENGTH:
        print(f"Warning: Password input was not truncated to {MAX_PASSWORD_LENGTH} characters. Actual: {entered_password_value}")
        assert len(entered_password_value) <= MAX_PASSWORD_LENGTH, "Password input exceeded max length and was not truncated."
    
    # Step 5: Click the 'Login' button.
    click_login(page)

    # Step 5 (Expected Result Interpretation):
    # Similar to username, we expect failure or an error related to length if the input is invalid.
    try:
        assert_successful_login(page)
    except:
        # Adapt message based on your system's error handling for password length.
        assert_error_message(page, "Password is too long" or "Invalid username or password") 
        assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_023_min_password_length(page: Page):
    """LOGIN_TC_023: Verify login with minimum allowed password length (if applicable)."""
    # NOTE: You need to know the minimum allowed password length. Let's assume it's 8.
    MIN_PASSWORD_LENGTH = 8
    min_length_password = "p" * MIN_PASSWORD_LENGTH

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter a valid password exactly at the minimum allowed length.
    page.locator("input[name='password']").fill(min_length_password)
    expect(page.locator("input[name='password']")).to_have_value(min_length_password)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # This test assumes the minimum length is enforced and a password of that length is valid.
    assert_successful_login(page)


def test_login_tc_024_password_below_min_length(page: Page):
    """LOGIN_TC_024: Verify login with password length below the minimum."""
    MIN_PASSWORD_LENGTH = 8 # Assume minimum is 8
    # Create a password shorter than the minimum.
    password_below_min = "p" * (MIN_PASSWORD_LENGTH - 1)

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter a password that is shorter than the minimum allowed length.
    page.locator("input[name='password']").fill(password_below_min)
    expect(page.locator("input[name='password']")).to_have_value(password_below_min)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Expecting an error message indicating the password is too short.
    assert_error_message(page, "Password is too short") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_025_remember_me(page: Page):
    """LOGIN_TC_025: Verify 'Remember Me' functionality (if present)."""
    # This test assumes a 'Remember Me' checkbox exists.
    remember_me_checkbox_selector = "input[type='checkbox'][name='remember_me']" # Adjust selector
    
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter valid username and password.
    enter_credentials(page, VALID_USERNAME, VALID_PASSWORD)

    # Step 3: Check the 'Remember Me' checkbox.
    remember_me_checkbox = page.locator(remember_me_checkbox_selector)
    expect(remember_me_checkbox).not_to_be_checked()
    remember_me_checkbox.check()
    expect(remember_me_checkbox).to_be_checked()

    # Step 4: Click 'Login'.
    click_login(page)
    assert_successful_login(page)

    # Step 5: Close the browser completely.
    page.context.close()
    # In a real pytest run, this would be handled by the fixture. 
    # For a single test simulating this, we'd need a new page.
    # For this example, we'll simulate by re-navigating in the same context.
    # If you are running this in a loop with multiple browser contexts, 
    # closing and opening a new one is essential.

    # Re-open browser/context and navigate (simulated)
    # new_page = page.context.new_page() # This would be done in a separate test or fixture context.
    # For this single test scenario, we reset the page context for demonstration.
    # A better approach would be to have separate tests for remember me and then closing.
    
    # Simulating closing browser and opening a new one:
    page = page.context.browser.new_page()
    navigate_to_login_page(page)

    # Step 6: Re-open the browser and navigate to the login page.
    # Verify the username field is pre-populated.
    expect(page.locator("input[name='username']")).to_have_value(VALID_USERNAME)
    # Password field might be empty or masked, depending on implementation.
    # expect(page.locator("input[name='password']")).to_have_value("") # or specific masking check

    # Step 7: Click 'Login' without re-entering the password.
    click_login(page)
    assert_successful_login(page)


def test_login_tc_026_remember_me_expired_session(page: Page):
    """LOGIN_TC_026: Verify 'Remember Me' functionality with expired session."""
    remember_me_checkbox_selector = "input[type='checkbox'][name='remember_me']" # Adjust selector

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter valid username and password.
    enter_credentials(page, VALID_USERNAME, VALID_PASSWORD)

    # Step 3: Check the 'Remember Me' checkbox.
    remember_me_checkbox = page.locator(remember_me_checkbox_selector)
    remember_me_checkbox.check()
    expect(remember_me_checkbox).to_be_checked()

    # Step 4: Click 'Login'.
    click_login(page)
    assert_successful_login(page)

    # Step 5: Wait for the session to expire.
    # This is highly dependent on your application's session timeout. 
    # For automation, we can't reliably 'wait' for a long time. 
    # This step might need to be simulated or the test might rely on application logic.
    # For demonstration, we'll assume the app handles session expiry.
    print("Simulating session expiration...")
    # In a real scenario, you might force a cookie expiry or use a mock server.
    # For this test, we'll assume the next action triggers re-authentication.

    # Step 6: Refresh the page or navigate to another page.
    # If the session has truly expired, this should redirect to login.
    page.reload()
    assert_on_login_page(page)

    # Step 7: Verify the username field is pre-populated.
    expect(page.locator("input[name='username']")).to_have_value(VALID_USERNAME)

    # Step 8: Enter the correct password and click 'Login'.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    click_login(page)
    assert_successful_login(page)


def test_login_tc_027_forgot_password_link(page: Page):
    """LOGIN_TC_027: Verify 'Forgot Password' link functionality (if present)."""
    # This test assumes a 'Forgot Password?' link exists and leads to a password reset page.
    forgot_password_link_selector = "a:has-text('Forgot Password?'), a:has-text('Forgot Password'), a:has-text('Reset Password')" # Adjust selector
    forgot_password_page_url_part = "/forgot-password" # Adjust based on your URL
    email_input_selector = "input[name='email'], input[name='username']" # Selector for email/username field on reset page
    submit_button_selector = "button[type='submit'], input[type='submit']" # Selector for submit button
    
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)
    expect(page.locator(forgot_password_link_selector)).to_be_visible()

    # Step 2: Click the 'Forgot Password?' link.
    page.locator(forgot_password_link_selector).click()
    # Assert that the user is redirected to the password reset page.
    expect(page).to_have_url(lambda url: forgot_password_page_url_part in url)
    expect(page.locator(email_input_selector)).to_be_visible()
    expect(page.locator(submit_button_selector)).to_be_visible()

    # Step 3: Enter a valid registered email address or username.
    # NOTE: You need a known registered email/username for this test.
    registered_email = "registered_user@example.com" # Replace with a real registered email
    page.locator(email_input_selector).fill(registered_email)
    expect(page.locator(email_input_selector)).to_have_value(registered_email)

    # Step 4: Submit the request.
    page.locator(submit_button_selector).click()
    # Assert confirmation message and that an email is sent (simulated check).
    # The actual email sending is hard to verify directly in UI tests. 
    # We typically check for a confirmation message on the page.
    # Example confirmation message:
    confirm_message_selector = ".confirmation-message, .success-message" 
    expect(page.locator(confirm_message_selector)).to_be_visible()
    expect(page.locator(confirm_message_selector)).to_contain_text("instructions sent") # Adjust text


def test_login_tc_028_forgot_password_unregistered_email(page: Page):
    """LOGIN_TC_028: Verify 'Forgot Password' with unregistered email/username."""
    forgot_password_link_selector = "a:has-text('Forgot Password?'), a:has-text('Forgot Password'), a:has-text('Reset Password')" # Adjust selector
    forgot_password_page_url_part = "/forgot-password" # Adjust based on your URL
    email_input_selector = "input[name='email'], input[name='username']" # Selector for email/username field on reset page
    submit_button_selector = "button[type='submit'], input[type='submit']" # Selector for submit button

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Click the 'Forgot Password?' link.
    page.locator(forgot_password_link_selector).click()
    expect(page).to_have_url(lambda url: forgot_password_page_url_part in url)

    # Step 3: Enter an unregistered email address or username.
    unregistered_email = "nonexistent_user@example.com"
    page.locator(email_input_selector).fill(unregistered_email)
    expect(page.locator(email_input_selector)).to_have_value(unregistered_email)

    # Step 4: Submit the request.
    page.locator(submit_button_selector).click()
    # Expecting a message indicating that instructions will be sent if the email exists.
    # This is to prevent user enumeration.
    expect(page.locator(".info-message, [role='alert']")).to_be_visible()
    expect(page.locator(".info-message, [role='alert']")).to_contain_text("if the email exists") # Adjust text


def test_login_tc_029_non_existent_username(page: Page):
    """LOGIN_TC_029: Verify login with non-existent username."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a username that does not exist in the system.
    page.locator("input[name='username']").fill(INVALID_USERNAME) # Using INVALID_USERNAME as a placeholder for non-existent
    expect(page.locator("input[name='username']")).to_have_value(INVALID_USERNAME)

    # Step 3: Enter any password into the password field.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click the 'Login' button.
    click_login(page)
    # Assert that a generic error message is displayed to prevent username enumeration.
    assert_error_message(page, "Invalid username or password") # Adjust message as per application
    assert_user_is_on_login_page_after_failed_login(page)


def test_login_tc_030_browser_back_after_successful_login(page: Page):
    """LOGIN_TC_030: Verify browser back button after successful login."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter valid credentials and click 'Login'.
    enter_credentials(page, VALID_USERNAME, VALID_PASSWORD)
    click_login(page)
    assert_successful_login(page)

    # Step 3: Click the browser's back button.
    page.go_back()
    # Assert that the user is NOT on the login page and cannot access it.
    # This might mean staying on the dashboard, or showing a session expired message if the backend handles it.
    # A common behavior is to stay on the current page or show a 'session expired' message.
    # If the system correctly handles back button navigation after login:
    # expect(page).not_to_have_url(lambda url: "/login" in url) # Ensure not on login page
    # The most robust check is to try and access a protected resource and see if it redirects to login.
    # For this specific test, we assert that we are NOT on the login page and ideally still logged in.
    # If it redirects to login, that's also a valid security measure.
    try:
        # Check if still on dashboard or similar logged-in state
        assert_successful_login(page)
    except:
        # If it redirected to login, that's also acceptable security behavior.
        assert_on_login_page(page)
        assert_error_message(page, "Session expired" or "Please log in again") # Example error message


def test_login_tc_031_browser_back_after_failed_login(page: Page):
    """LOGIN_TC_031: Verify browser back button after failed login."""
    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter invalid credentials and click 'Login'.
    enter_credentials(page, INVALID_USERNAME, INVALID_PASSWORD)
    click_login(page)
    assert_error_message(page, "Invalid username or password") # Adjust message
    assert_user_is_on_login_page_after_failed_login(page)

    # Step 3: Click the browser's back button.
    page.go_back()
    # Assert that the user can navigate to the previous page (if any) and the login state is clean.
    # The login page should ideally be reloaded without error messages or previous input.
    # This is a general expectation for back navigation.
    assert_on_login_page(page)
    expect(page.locator("input[name='username']")).to_have_value("")
    expect(page.locator("input[name='password']")).to_have_value("")
    # Ensure no error messages are visible after going back.
    expect(page.locator(".error-message, [role='alert']")).not_to_be_visible()


def test_login_tc_032_login_page_responsiveness(page: Page):
    """LOGIN_TC_032: Verify login page responsiveness on different screen sizes."""
    # This test requires the page to be rendered in different viewports.
    # We'll check a few common breakpoints.
    # NOTE: Adjust the assertions based on your application's design and expected responsive behavior.

    # Step 1: Access the login page on various devices/screen resolutions.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Test on Desktop viewport
    page.set_viewport_size({"width": 1280, "height": 720})
    print("Testing on Desktop viewport (1280x720)")
    # Add assertions for desktop layout, e.g., element positioning, visibility.
    # expect(page.locator(".login-container")).to_have_css('width', '...') # Example assertion

    # Test on Tablet viewport
    page.set_viewport_size({"width": 768, "height": 1024})
    print("Testing on Tablet viewport (768x1024)")
    # Add assertions for tablet layout.

    # Test on Mobile viewport
    page.set_viewport_size({"width": 375, "height": 667})
    print("Testing on Mobile viewport (375x667)")
    # Add assertions for mobile layout.
    # Example: check if input fields take full width or if elements stack correctly.
    expect(page.locator("input[name='username']")).to_have_css('width', '90%') # Example assertion for mobile full width
    expect(page.locator("input[name='password']")).to_have_css('width', '90%')
    expect(page.get_by_role("button", name="Login")).to_have_css('width', '90%')

    # Ensure no visual defects (this is more of a manual check or requires visual regression tools).
    # For Playwright, we can check for elements that might overflow or be cut off.
    # Example: Check if any critical element is not fully visible.
    # For a comprehensive test, consider Percy.io or Applitools.
    print("Responsiveness check completed. Manual verification of visual aspects is recommended.")


def test_login_tc_033_unicode_username(page: Page):
    """LOGIN_TC_033: Verify login with unicode characters in username."""
    # Example Unicode usernames
    unicode_username_1 = "JöhnDoë"
    unicode_username_2 = "你好世界" # Chinese for 'Hello World'
    unicode_username_3 = "élégant"

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username containing unicode characters.
    page.locator("input[name='username']").fill(unicode_username_1)
    expect(page.locator("input[name='username']")).to_have_value(unicode_username_1)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click 'Login'.
    click_login(page)
    # Assuming unicode characters are supported and this results in successful login.
    assert_successful_login(page)

    # Repeat for other unicode usernames if necessary and if you have credentials for them.
    # For this example, we'll stick to one for demonstration.


def test_login_tc_034_unicode_password(page: Page):
    """LOGIN_TC_034: Verify login with unicode characters in password."""
    # Example Unicode passwords
    unicode_password_1 = "P@sswÖrd123!"
    unicode_password_2 = "你好世界123"
    unicode_password_3 = "résumé!"

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Enter the corresponding valid password containing unicode characters.
    page.locator("input[name='password']").fill(unicode_password_1)
    expect(page.locator("input[name='password']")).to_have_value(unicode_password_1)

    # Step 4: Click 'Login'.
    click_login(page)
    # Assuming unicode characters are supported and this results in successful login.
    assert_successful_login(page)

    # Repeat for other unicode passwords if necessary and if you have credentials for them.


def test_login_tc_035_very_long_valid_username(page: Page):
    """LOGIN_TC_035: Verify login with very long valid username."""
    MAX_USERNAME_LENGTH = 50 # Assume max length is 50
    # Generate a valid username that is close to, but within, the maximum allowed length.
    if len(VALID_USERNAME) >= MAX_USERNAME_LENGTH:
        print("Skipping very long username test: VALID_USERNAME is already at or exceeds max length.")
        return

    long_valid_username = "a" * (MAX_USERNAME_LENGTH - 10) + VALID_USERNAME[-10:] # Ensure it ends with valid chars if needed
    # Ensure the generated username is at least within max length.
    assert len(long_valid_username) <= MAX_USERNAME_LENGTH

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Generate and enter a valid username that is close to, but within, the maximum allowed length.
    page.locator("input[name='username']").fill(long_valid_username)
    expect(page.locator("input[name='username']")).to_have_value(long_valid_username)

    # Step 3: Enter the corresponding valid password.
    page.locator("input[name='password']").fill(VALID_PASSWORD)
    expect(page.locator("input[name='password']")).to_have_value(VALID_PASSWORD)

    # Step 4: Click 'Login'.
    click_login(page)
    assert_successful_login(page)


def test_login_tc_036_very_long_valid_password(page: Page):
    """LOGIN_TC_036: Verify login with very long valid password."""
    MAX_PASSWORD_LENGTH = 128 # Assume max length is 128
    # Generate a valid password that is close to, but within, the maximum allowed length.
    if len(VALID_PASSWORD) >= MAX_PASSWORD_LENGTH:
        print("Skipping very long password test: VALID_PASSWORD is already at or exceeds max length.")
        return

    long_valid_password = "p" * (MAX_PASSWORD_LENGTH - 10) + VALID_PASSWORD[-10:]
    assert len(long_valid_password) <= MAX_PASSWORD_LENGTH

    # Step 1: Navigate to the login page.
    navigate_to_login_page(page)
    assert_on_login_page(page)

    # Step 2: Enter a valid username.
    page.locator("input[name='username']").fill(VALID_USERNAME)

    # Step 3: Generate and enter a valid password that is close to, but within, the maximum allowed length.
    page.locator("input[name='password']").fill(long_valid_password)
    expect(page.locator("input[name='password']")).to_have_value(long_valid_password)

    # Step 4: Click 'Login'.
    click_login(page)
    assert_successful_login(page)
