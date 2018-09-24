"""
Driving
"""
from lib.settings import *
from lib.browser import browser
from lib.captcha import captcha
from lib.mail import mail
from lib.helpers import helpers

class test:
    """
    Captcha
    """
    def captcha(self):
        # TODO reload to handle unsupported captcha: https://www.gstatic.com/recaptcha/images/v1_unsupported.png

        captcha_images = self.b.driver.find_by_id("recaptcha_challenge_image")

        if len(captcha_images):
            helpers.message("Loading captcha.")

            c = captcha()
            c.download_image(captcha_images.first["src"])
            c.show_image()
            c.delete_image()

            # Check if user can answer captcha
            bad_captcha = input("Can you read the Captcha? Answer y or n: ")

            if " " in bad_captcha:
                # User might have entered captcha already
                captcha_answer = bad_captcha

            elif bad_captcha != "y":
                # Reload the page and return
                self.b.driver.visit(self.b.driver.url)
                return self.captcha()

            if captcha_answer is None:
                # Get captcha text
                captcha_answer = input("Captcha: ")

            self.b.driver.fill("recaptcha_response_field", captcha_answer)

    """
    Login
    """
    def login(self):
        try:
            self.b = browser("https://driverpracticaltest.direct.gov.uk/login")

            # Captcha
            self.captcha()

            self.b.driver.fill("username", LICENCE)
            self.b.driver.fill("password", APPLICATION_REFERENCE)

            helpers.message("Logging in...")

            self.b.driver.find_by_name("booking-login").first.click()

        except Exception as e:
            self.b.driver.quit()
            helpers.error(e)

    """
    Check
    Starting from change link on account dashboard
    """
    def check(self):
        try:
            helpers.message("Checking for next available tests...")

            url = self.b.driver.find_by_id("date-time-change").first["href"]
            self.b.get(url)

            # Show earliest date available
            self.b.driver.choose("testChoice", "ASAP")

            helpers.message("Checking...")

            self.b.driver.find_by_name("drivingLicenceSubmit").first.click()

            # Captcha
            try:
                self.captcha()
                self.b.driver.find_by_name("recaptchaSubmit").first.click()
            except Exception:
                pass

            # TODO Loop this, randomly every 1-2 mins
            # TODO Test list isn't empty
            dates = []
            days = self.b.driver.find_by_xpath("//ul[@class='SlotPicker-days']/li[@class='SlotPicker-day']/label/input")

            if len(days):
                for day in days:
                    dates.append(day["data-datetime-label"])

                # Send email
                m = mail()
                m.send("Available Driving Tests", "Available days:\n%s" % "\n- ".join(dates))

        except Exception as e:
            helpers.error(e)

        finally:
            self.b.driver.quit()
