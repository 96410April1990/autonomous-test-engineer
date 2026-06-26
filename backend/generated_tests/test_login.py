# test_login.py

import pytest
from playwright.sync_api import Page, expect

# --- Test Case: UL_001 - Successful login with valid username and password ---

def test_successful_login(page: Page, valid_username, valid_password, dashboard_url):
    """
    Tests successful login with valid credentials.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login") # Assuming '/login' is the login page path
    expect(page).to_have_url("/login")
    expect(page.locator("input[name='username']")).to_be_visible()
    expect(page.locator("input[name='password']")).to_be_visible()
    expect(page.locator("button[type='submit']")).to_be_visible()

    # Step 2: Enter a valid username in the username field.
    page.fill("input[name='username']", valid_username)
    expect(page.locator("input[name='username']")).to_have_value(valid_username)

    # Step 3: Enter a valid password in the password field.
    page.fill("input[name='password']", valid_password)
    expect(page.locator("input[name='password']")).to_have_value(valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: The user is successfully logged in and redirected to the dashboard/home page.
    expect(page).to_have_url(dashboard_url)
    # Add assertions here to verify elements on the dashboard/home page are visible
    # For example: expect(page.locator("h1:has-text('Dashboard')")).to_be_visible()

# --- Test Case: UL_002 - Login with invalid password ---

def test_login_invalid_password(page: Page, valid_username, invalid_password):
    """
    Tests login with a valid username and an invalid password.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username in the username field.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter an invalid password (incorrect) in the password field.
    page.fill("input[name='password']", invalid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating 'Invalid username or password' (or similar) is displayed. The user remains on the login page.
    expect(page).to_have_url("/login") # User remains on the login page
    expect(page.locator(".error-message")).to_contain_text("Invalid username or password") # Adjust selector for actual error message

# --- Test Case: UL_003 - Login with invalid username ---

def test_login_invalid_username(page: Page, invalid_username, valid_password):
    """
    Tests login with an invalid username and a valid password.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter an invalid username (non-existent) in the username field.
    page.fill("input[name='username']", invalid_username)

    # Step 3: Enter a valid password in the password field.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating 'Invalid username or password' (or similar) is displayed. The user remains on the login page.
    expect(page).to_have_url("/login") # User remains on the login page
    expect(page.locator(".error-message")).to_contain_text("Invalid username or password") # Adjust selector for actual error message

# --- Test Case: UL_004 - Login with empty username ---

def test_login_empty_username(page: Page, valid_password):
    """
    Tests login with an empty username and a valid password.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Leave the username field empty.
    expect(page.locator("input[name='username']")).to_be_empty()

    # Step 3: Enter a valid password in the password field.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating that the username is required is displayed. The user remains on the login page.
    expect(page).to_have_url("/login")
    expect(page.locator(".username-error")).to_contain_text("Username is required") # Adjust selector for actual error message

# --- Test Case: UL_005 - Login with empty password ---

def test_login_empty_password(page: Page, valid_username):
    """
    Tests login with a valid username and an empty password.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username in the username field.
    page.fill("input[name='username']", valid_username)

    # Step 3: Leave the password field empty.
    expect(page.locator("input[name='password']")).to_be_empty()

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating that the password is required is displayed. The user remains on the login page.
    expect(page).to_have_url("/login")
    expect(page.locator(".password-error")).to_contain_text("Password is required") # Adjust selector for actual error message

# --- Test Case: UL_006 - Login with both empty username and password ---

def test_login_empty_credentials(page: Page):
    """
    Tests login with both empty username and password.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Leave both username and password fields empty.
    expect(page.locator("input[name='username']")).to_be_empty()
    expect(page.locator("input[name='password']")).to_be_empty()

    # Step 3: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: Error messages indicating that both username and password are required are displayed. The user remains on the login page.
    expect(page).to_have_url("/login")
    expect(page.locator(".username-error")).to_contain_text("Username is required")
    expect(page.locator(".password-error")).to_contain_text("Password is required")

# --- Test Case: UL_007 - Login with username containing leading/trailing spaces ---

def test_login_username_with_spaces(page: Page, valid_username_for_spaces, dashboard_url):
    """
    Tests login with valid username containing leading/trailing spaces (assuming trimming).
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username with leading spaces.
    username_with_leading_spaces = f"  {valid_username_for_spaces}"
    page.fill("input[name='username']", username_with_leading_spaces)
    expect(page.locator("input[name='username']")).to_have_value(username_with_leading_spaces)

    # Step 3: Enter a valid password.
    page.fill("input[name='password']", "some_valid_password") # Use a placeholder or parameter

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User successfully logged in (assuming spaces are trimmed).
    expect(page).to_have_url(dashboard_url)

    # Step 5: Repeat with trailing spaces.
    page.goto("/login")
    username_with_trailing_spaces = f"{valid_username_for_spaces}  "
    page.fill("input[name='username']", username_with_trailing_spaces)
    page.fill("input[name='password']", "some_valid_password")
    page.click("button[type='submit']")
    expect(page).to_have_url(dashboard_url)

    # Step 6: Repeat with both leading and trailing spaces.
    page.goto("/login")
    username_with_both_spaces = f"  {valid_username_for_spaces}  "
    page.fill("input[name='username']", username_with_both_spaces)
    page.fill("input[name='password']", "some_valid_password")
    page.click("button[type='submit']")
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_008 - Login with password containing leading/trailing spaces ---

def test_login_password_with_spaces(page: Page, valid_username, valid_password_for_spaces, dashboard_url):
    """
    Tests login with valid password containing leading/trailing spaces (assuming trimming).
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter a valid password with leading spaces.
    password_with_leading_spaces = f"  {valid_password_for_spaces}"
    page.fill("input[name='password']", password_with_leading_spaces)
    expect(page.locator("input[name='password']")).to_have_value(password_with_leading_spaces)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User successfully logged in (assuming spaces are trimmed).
    expect(page).to_have_url(dashboard_url)

    # Step 5: Repeat with trailing spaces.
    page.goto("/login")
    page.fill("input[name='username']", valid_username)
    password_with_trailing_spaces = f"{valid_password_for_spaces}  "
    page.fill("input[name='password']", password_with_trailing_spaces)
    page.click("button[type='submit']")
    expect(page).to_have_url(dashboard_url)

    # Step 6: Repeat with both leading and trailing spaces.
    page.goto("/login")
    page.fill("input[name='username']", valid_username)
    password_with_both_spaces = f"  {valid_password_for_spaces}  "
    page.fill("input[name='password']", password_with_both_spaces)
    page.click("button[type='submit']")
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_009 - Case sensitivity of username ---

def test_login_username_case_sensitivity(page: Page, valid_username_mixed_case, valid_password, dashboard_url):
    """
    Tests the case sensitivity of the username field.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username in mixed case.
    page.fill("input[name='username']", valid_username_mixed_case)

    # Step 3: Enter the corresponding valid password.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button (case-insensitive check).
    page.click("button[type='submit']")
    expect(page).to_have_url(dashboard_url)

    # Step 5: Repeat with an incorrect case for the username (case-sensitive check).
    page.goto("/login")
    incorrect_case_username = valid_username_mixed_case.lower() # Example of incorrect case
    page.fill("input[name='username']", incorrect_case_username)
    page.fill("input[name='password']", valid_password)
    page.click("button[type='submit']")
    expect(page).to_have_url("/login") # Should remain on login page if case-sensitive
    expect(page.locator(".error-message")).to_contain_text("Invalid username or password")

# --- Test Case: UL_010 - Case sensitivity of password ---

def test_login_password_case_sensitivity(page: Page, valid_username, valid_password_mixed_case, dashboard_url):
    """
    Tests the case sensitivity of the password field.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter a valid password in mixed case.
    page.fill("input[name='password']", valid_password_mixed_case)

    # Step 4: Click the 'Login' button (case-sensitive check).
    page.click("button[type='submit']")
    expect(page).to_have_url(dashboard_url)

    # Step 5: Repeat with an incorrect case for the password (case-sensitive check).
    page.goto("/login")
    page.fill("input[name='username']", valid_username)
    incorrect_case_password = valid_password_mixed_case.lower() # Example of incorrect case
    page.fill("input[name='password']", incorrect_case_password)
    page.click("button[type='submit']")
    expect(page).to_have_url("/login") # Should remain on login page if case-sensitive
    expect(page.locator(".error-message")).to_contain_text("Invalid username or password")

# --- Test Case: UL_011 - Login with special characters in username ---

def test_login_username_special_chars(page: Page, valid_username_special_chars, valid_password, dashboard_url):
    """
    Tests login with a valid username containing special characters.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username with special characters.
    page.fill("input[name='username']", valid_username_special_chars)

    # Step 3: Enter the corresponding valid password.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_012 - Login with special characters in password ---

def test_login_password_special_chars(page: Page, valid_username, valid_password_special_chars, dashboard_url):
    """
    Tests login with a valid password containing special characters.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter a valid password with special characters.
    page.fill("input[name='password']", valid_password_special_chars)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_013 - Login with maximum allowed username length ---

def test_login_max_username_length(page: Page, max_username_length, valid_password, dashboard_url):
    """
    Tests login with a username at the maximum allowed length.
    Assumes max_username_length is provided via pytest fixture or config.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a username with the maximum allowed length.
    # This requires a fixture or a way to generate a string of specific length.
    # Example: username = "a" * max_username_length
    username = max_username_length
    page.fill("input[name='username']", username)
    expect(page.locator("input[name='username']")).to_have_value(username)

    # Step 3: Enter a valid password.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_014 - Login with username exceeding maximum allowed length ---

def test_login_exceed_username_length(page: Page, username_exceeding_max_length, valid_password):
    """
    Tests login with a username exceeding the maximum allowed length.
    Assumes username_exceeding_max_length is provided via pytest fixture or config.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Attempt to enter a username exceeding the maximum allowed length.
    page.fill("input[name='username']", username_exceeding_max_length)

    # Step 3: Enter a valid password.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating the username exceeds the maximum allowed length should be displayed.
    expect(page).to_have_url("/login")
    expect(page.locator(".username-error")).to_contain_text("Username exceeds maximum length") # Adjust selector

# --- Test Case: UL_015 - Login with maximum allowed password length ---

def test_login_max_password_length(page: Page, valid_username, max_password_length, dashboard_url):
    """
    Tests login with a password at the maximum allowed length.
    Assumes max_password_length is provided via pytest fixture or config.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter a password with the maximum allowed length.
    # Example: password = "p" * max_password_length
    password = max_password_length
    page.fill("input[name='password']", password)
    expect(page.locator("input[name='password']")).to_have_value(password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_016 - Login with password exceeding maximum allowed length ---

def test_login_exceed_password_length(page: Page, valid_username, password_exceeding_max_length):
    """
    Tests login with a password exceeding the maximum allowed length.
    Assumes password_exceeding_max_length is provided via pytest fixture or config.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Attempt to enter a password exceeding the maximum allowed length.
    page.fill("input[name='password']", password_exceeding_max_length)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating the password exceeds the maximum allowed length should be displayed.
    expect(page).to_have_url("/login")
    expect(page.locator(".password-error")).to_contain_text("Password exceeds maximum length") # Adjust selector

# --- Test Case: UL_017 - Login with unicode characters in username (if supported) ---

def test_login_unicode_username(page: Page, valid_unicode_username, valid_password, dashboard_url):
    """
    Tests login with a valid username containing unicode characters.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username with unicode characters.
    page.fill("input[name='username']", valid_unicode_username)

    # Step 3: Enter the corresponding valid password.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_018 - Login with unicode characters in password (if supported) ---

def test_login_unicode_password(page: Page, valid_username, valid_unicode_password, dashboard_url):
    """
    Tests login with a valid password containing unicode characters.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter a valid password with unicode characters.
    page.fill("input[name='password']", valid_unicode_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: User is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_019 - Login attempt after multiple failed attempts (brute force prevention) ---

# This test requires knowledge of the system's lockout threshold and mechanism.
# You'll need to define how many failed attempts lead to lockout and the expected lockout behavior.
# For demonstration, let's assume a lockout after 5 attempts and a lockout message.

def test_brute_force_prevention(page: Page, valid_username, invalid_password, lockout_threshold=5):
    """
    Tests brute force prevention by attempting multiple failed logins.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username and an invalid password for N consecutive times.
    for _ in range(lockout_threshold):
        page.fill("input[name='username']", valid_username)
        page.fill("input[name='password']", invalid_password)
        page.click("button[type='submit']")
        expect(page).to_have_url("/login") # Stays on login page after each failed attempt
        # Optionally, check for a generic error message on each attempt
        expect(page.locator(".error-message")).to_contain_text("Invalid username or password")

    # Step 3: After the lockout, attempt to login with the correct username and password.
    # The expected result here depends on the system's lockout implementation.
    # It could be a CAPTCHA, a specific lockout message, or complete blockage.
    page.fill("input[name='username']", valid_username)
    page.fill("input[name='password']", "correct_password") # Placeholder for correct password
    page.click("button[type='submit']")

    # Example: Check for a lockout message.
    expect(page.locator(".lockout-message")).to_be_visible()
    expect(page.locator(".lockout-message")).to_contain_text("Account locked due to multiple failed attempts.") # Adjust selector and text
    expect(page).to_have_url("/login") # Remains on login page after lockout

# --- Test Case: UL_020 - Successful login with a username that was previously locked out ---

def test_login_after_lockout_period(page: Page, valid_username, valid_password, dashboard_url):
    """
    Tests successful login after a lockout period has expired (or account unlocked).
    This test might require mocking time or specific setup.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Cause a lockout for a specific username.
    # This part would typically involve a separate test or a setup fixture to simulate failed attempts.
    # For demonstration, assuming the lockout is already in place or we call a helper to do it.
    # Example: cause_account_lockout(page, valid_username, 5) # Simulate failed attempts
    print(f"Simulating account lockout for {valid_username}... (This part needs actual implementation)")

    # Step 3: Wait for the lockout period to expire (if applicable).
    # In a real scenario, you might use page.wait_for_timeout(duration) or have an admin unlock it.
    print("Waiting for lockout period to expire or account to be unlocked... (This part needs actual implementation)")
    # For demonstration, let's assume the lockout duration has passed.

    # Step 4: Attempt to login with the correct username and password.
    page.fill("input[name='username']", valid_username)
    page.fill("input[name='password']", valid_password)
    page.click("button[type='submit']")

    # Expected Result: The user is successfully logged in.
    expect(page).to_have_url(dashboard_url)

# --- Test Case: UL_021 - Login with username that contains only spaces ---

def test_login_username_only_spaces(page: Page, valid_password):
    """
    Tests login with a username consisting only of spaces.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a username that consists only of spaces.
    username_with_spaces = "   "
    page.fill("input[name='username']", username_with_spaces)
    expect(page.locator("input[name='username']")).to_have_value(username_with_spaces)

    # Step 3: Enter a valid password.
    page.fill("input[name='password']", valid_password)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating that the username is required or invalid is displayed.
    expect(page).to_have_url("/login")
    expect(page.locator(".username-error")).to_contain_text("Username is required") # Adjust selector

# --- Test Case: UL_022 - Login with password that contains only spaces ---

def test_login_password_only_spaces(page: Page, valid_username):
    """
    Tests login with a password consisting only of spaces.
    """
    # Step 1: Navigate to the login page.
    page.goto("/login")
    expect(page).to_have_url("/login")

    # Step 2: Enter a valid username.
    page.fill("input[name='username']", valid_username)

    # Step 3: Enter a password that consists only of spaces.
    password_with_spaces = "   "
    page.fill("input[name='password']", password_with_spaces)
    expect(page.locator("input[name='password']")).to_have_value(password_with_spaces)

    # Step 4: Click the 'Login' button.
    page.click("button[type='submit']")

    # Expected Result: An error message indicating that the password is required or invalid is displayed.
    expect(page).to_have_url("/login")
    expect(page.locator(".password-error")).to_contain_text("Password is required") # Adjust selector


# --- Pytest Fixtures (Example - you'll need to define these based on your setup) ---

@pytest.fixture
def valid_username():
    # Replace with your actual valid username
    return "testuser"

@pytest.fixture
def valid_password():
    # Replace with your actual valid password
    return "password123"

@pytest.fixture
def invalid_password():
    return "wrongpassword"

@pytest.fixture
def invalid_username():
    return "nonexistentuser"

@pytest.fixture
def dashboard_url():
    # Replace with your actual dashboard URL
    return "/dashboard"

@pytest.fixture
def valid_username_for_spaces():
    # A username that's valid after trimming spaces
    return "trimmeduser"

@pytest.fixture
def valid_password_for_spaces():
    # A password that's valid after trimming spaces
    return "trimmedpass"

@pytest.fixture
def valid_username_mixed_case():
    # A username with mixed case that might be used for case-insensitivity tests
    return "UsErNaMe"

@pytest.fixture
def valid_password_mixed_case():
    # A password with mixed case that might be used for case-sensitivity tests
    return "PaSsWoRd"

@pytest.fixture
def valid_username_special_chars():
    # A username that includes special characters
    return "user.name-123!"

@pytest.fixture
def valid_password_special_chars():
    # A password that includes special characters
    return "!@#$%^&*()"

@pytest.fixture
def max_username_length():
    # Define the maximum allowed username length for your application
    # Example: return "a" * 255
    return "a" * 255 # Placeholder for a string of max length

@pytest.fixture
def username_exceeding_max_length():
    # Define a username that exceeds the maximum allowed length
    # Example: return "a" * 256
    return "a" * 256 # Placeholder for a string exceeding max length

@pytest.fixture
def max_password_length():
    # Define the maximum allowed password length for your application
    # Example: return "p" * 128
    return "p" * 128 # Placeholder for a string of max length

@pytest.fixture
def password_exceeding_max_length():
    # Define a password that exceeds the maximum allowed length
    # Example: return "p" * 129
    return "p" * 129 # Placeholder for a string exceeding max length

@pytest.fixture
def valid_unicode_username():
    # A valid username with unicode characters
    return "你好世界"

@pytest.fixture
def valid_unicode_password():
    # A valid password with unicode characters
    return "密码123"



