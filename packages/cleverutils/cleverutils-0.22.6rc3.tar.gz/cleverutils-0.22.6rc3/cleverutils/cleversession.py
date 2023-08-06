from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import webbrowser
import pyperclip
from pathlib import Path
import keyring
from .clevergui import *
from .cleverweb import *
from .cleverutils import *
import threading
import difflib
import urllib

# TODO: Options/Notifications
"""


option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path='path-of-
driver\chromedriver.exe')
driver.get('https://www.facebook.com')
"""

class CleverSession(CleverDict):
    """
    A CleverDict sub-class(*) intended to handle selenium webbrowser sessions
    and common repeatable tasks such as selecting a target website using
    PySimpleGUI, retrieving login credentials using keyring, automated login,
    and scraper/collection tasks.

    Also uses predefined login and scraper functions notably from:

    login_to.py
    collect.py

    (*) CleverDict provides easy data handling and auto-save features.
    """
    index = CleverDict()
    choices = {"https://github.com/login": "Github",
               "https://twitter.com": "Twitter",
               "https://www.satchelone.com/login": "SatchelOne",
               "https://www.hackerrank.com": "HackerRank",
               "192.168.0.1": "TP-Link",
               "https://facebook.com/marketplace": "FB Marketplace"}
    keyring_config_root = keyring.util.platform_.config_root()
    keyring_data_root = keyring.util.platform_.data_root()

    def __init__(self, *args, **kwargs):
        options, kwargs = self.get_options_from_kwargs(**kwargs)
        super().__init__(**kwargs)
        self.start_time = get_time()
        start_gui(redirect=kwargs.get("redirect"))
        self.url = args if "http" in args else kwargs.get("url") or ""
        if self.url.endswith("/"):
            self.url = self.url[:-1]
        if not self.url:
            self.check_and_prompt("url")
        self.account = CleverSession.choices[self.url]
        self.login_url = self.url
        self.get_username()
        if not self.get("dirpath"):
            self.dirpath_str = str(Path().cwd())
        self.max_browsers = 5 if self.account == "Github" else 1
        if kwargs.get("echo") is True:
            setattr(CleverSession, "save", CleverSession.echo_on)
        if kwargs.get("echo") is False:
            setattr(CleverSession, "save", CleverSession.echo_off)
        self.browser = kwargs.get("browser")
        options = Options()
        options.add_argument("--disable-infobars")
        # options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        # Pass the argument 1 to allow and 2 to block
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        options.add_argument("--disable-logging")
        if not self.browser:
            self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(kwargs.get("wait") or 3)
        self.add_current_browser()

    @property
    def dirpath(self):
        """
        This @property returns a pathlib.Path version of .dirpath_str.
        Needed in order to allow JSON serialisation without constant conversions
        since pathlib.Path is not JSON serialisable.
        """
        return Path(self.dirpath_str)

    def get_options_from_kwargs(self, **kwargs):
        """ Separate actionable options from general data in kwargs."""
        options = {}
        for key, default_value in {"echo": True, "_break": False, "redirect": False}.items():
            if isinstance(kwargs.get(key), bool):
                options[key] = kwargs.get(key)
                del kwargs[key]
            else:
                options[key] = default_value
        return options, kwargs

    def get_username(self):
        """
        Loads (last modified) username from keyring. May not work on iOS.
        """
        try:
            self.username = keyring.get_credential(self.account, None).username
        except:
            print("\n  ⚠ .get_username() only supported on Windows OS.")
            print("\n     Trying creating .username manually first.")

    def check_and_prompt(self, *args):
        """
        Checks for existence/non-False value of an argument, and if required
        calls the specified method to prompt for a value.  Different methods
        may be needed for different input types e.g. file, folder, checkboxes, database read, REST API call, or regular input().

        args : attributes (as strings) to look for; try to use logical order.
        """
        buttons = {"url": "Please enter a link (URL) to the target website:",}
        text = {"username": "Please enter a username/login ID{}:",
                "password": "Please enter a password{}:"}
        choices = CleverSession.choices
        for attribute in args:
            prompt = buttons.get(attribute) or text.get(attribute) or f"Please enter a value for .{attribute} :"
            prompt = prompt.replace("{}", f" for your {self.account} account" if self.get("account") else "")
            if attribute == "password":
                self.check_and_prompt("url", "username")
                if not keyring.get_password(choices[self.url], self.username):
                    self.set_password(text_input(prompt))
            elif not self.get(attribute):
                if attribute in buttons:
                    value = button_menu(choices)
                else:  # Includes attributes in neither buttons nor text
                    value = text_input(prompt)
                if value:
                    self[attribute] = value

    @property
    def password(self):
        """ Retrieve password from keyring """
        return keyring.get_password(CleverSession.choices[self.url], self.username)

    def set_password(self, value):
        """ Set password in keyring """
        if value:
            keyring.set_password(CleverSession.choices[self.url], self.username, value)

    def delete_password(self):
        """
        Delete password AND username from keyring.
        .username remains in memory but .password was only ever an @property.
        """
        keyring.delete_password(CleverSession.choices[self.url], self.username)

    def add_current_browser(self):
        """Appends the current (login) browser to self.browsers"""
        if not hasattr(self, "browsers"):
            self.browsers = []
        self.browsers += [self.browser]

    @timer
    def login_with_webbrowsers(self, browsers=None):
        """
        KWARGS:

        wait : Seconds for selenium to implicitly_wait
        browsers : int > number of browsers to run concurrently
        """
        try:
            self.check_and_prompt("url", "username", "password")
            if not hasattr(self, "browsers"):
                self.setattr_direct("browsers", [])
            dispatch = {"github.com": Login_to.github,
                        "twitter.com": Login_to.twitter,
                        "satchelone.com": Login_to.satchelone,
                        "hackerrank.com": Login_to.hackerrank,}
                        # "192.168.0.1": Login_to.tplink}
            browserThreads = []
            if browsers is None:
                browsers = self.get("max_browsers") or 1
            # Adjust if main browser is already be running:
            browsers = browsers - len(self.browsers)
            for n in  range(browsers):
                for website, func in dispatch.items():
                    if website in self.url:
                        browserThread = threading.Thread(target=func, args=[self])
                        browserThreads.append(browserThread)
                        browserThread.start()
                        break
            for browserThread in browserThreads:
                    browserThread.join()
        except WebDriverException:
            raise WebDriverException("Check chromdriver is in your PATH or you're running this code from a directory with chromedriver.exe in it")

    def echo_on(self, name, value):
        """
        Generic confirmation applied CleverDict auto-save with:

        setattr(CleverSession, "save", CleverSession.echo_on)
        """
        if "password" not in str(name).lower() and name not in vars(self):
            # vars(self) includes CleverDict keys created with setattr_direct()
            # i.e. not intended to be readily accessible as data attributes
            print(f" ⓘ  {name} = {value} {type(value)}")

    def echo_off(self, name, value):
        """
        Disable CleverSession autosave confirmations with:

        setattr(CleverSession, "save", CleverSession.echo_off)
        """
        pass

    def start(self):
        """ Shortcut/Alias for starting a webbrowser session and logging in """
        self.login_with_webbrowsers()

    def listen(self, save=False):
        """
        Compares web page source code (.page_source) with a previous
        version/page of the same browser session (.source), calculates any
        differences using difflib, and saves the changed lines (only) to
        .source_diff and to file (if save=True).

        self.browser is a selenium webdriver instance.
        """
        if not hasattr(self, "source"):
            self.source = ""
            self.source_diff = []
            self.source_index = 1
        source = self.browser.page_source.splitlines()
        if source != self.source:
            print("\nⓘ  Page source code has changed.  Saving to .source_diff")
            d = difflib.Differ()
            diff = d.compare(source, self.source)
            diff = '\n'.join([x for x in diff if x[0] in "+-?"])
            if self.source:
                self.source_diff += [diff]
                if save:
                    filename = "source" + str(self.source_index).zfill(3)
                    with open(filename, "w") as file:
                        file.write(diff)
                        print(f"\nⓘ  Saved page source to {filename}")
                        self.source_index += 1
            self.source = source

    @property
    def href_images(self, min_height=100, min_width=100, zoom_out=True):
        """
        Returns a list of all image (href) image elements of minimum size
        """
        if zoom_out:
            # Zoom out
            self.browser.execute_script("document.body.style.zoom='25%'")
            time.sleep(5)
            self.browser.execute_script("document.body.style.zoom='100%'")
        a_tags = self.browser.find_elements_by_tag_name("a")
        a_tags = [x for x in a_tags if x.get_attribute('href').endswith(".jpg") or x.get_attribute('href').endswith(".png")]
        a_tags = [i for i in a_tags if i.size["height"] >= min_height]
        a_tags = [i for i in a_tags if i.size["width"] >= min_width]
        return [x.get_attribute('href') for x in a_tags if x.get_attribute('href').endswith(".jpg") or x.get_attribute('href').endswith(".png")]

    def download_all_images(self, images_list=None, dir_path=None):
        """
        Downloads images from a list of urls to the specified dir_path
        See also cleverutils.scrape_images
        """
        if images_list is None:
            images_list = self.href_images()
        dir_path = Path(dir_path) if dir_path else Path.cwd()
        if not dir_path.is_dir():
            dir_path.mkdir()
        for image in images_list:
            try:
                _, filename = image.split("/item/")
                filename, _ = filename.split("?")
            except ValueError:
                filename = image
                for punctuation in ":/?":
                    filename = filename.replace(punctuation, "_")
            media = requests.get(image).content
            with open(f'{dir_path/filename}', 'wb') as file:
                file.write(media)




# setattr(CleverSession, "login_with_webbrowsers", login_with_webbrowsers)
# self= CleverSession()
# self.start()
