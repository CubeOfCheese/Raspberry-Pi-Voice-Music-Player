from page_objects import PageObject, PageElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import
class SpotifyPlaylist(PageObject):

    """Spotify Playlist Page for Selenium Page Object Pattern"""
    album_uri = "https://open.spotify.com/album/"
    playlist_uri = "https://open.spotify.com/playlist/"
    login_uri = "https://spotify.com/login/"

    username = PageElement(css='input[id="login-username"]')
    password = PageElement(css='input[id="login-password"]')
    login_btn = PageElement(css='button[id="login-button"]')

    def open_playlist(self, playlist_id):
        self.get(self.playlist_uri + playlist_id)

    def open_album(self, album_id):
        self.get(self.album_uri + album_id)

    def login(self, username, password):
        self.get(self.login_uri)
        self.username = username
        self.password = password
        self.login_btn.click()

driver = webdriver.Firefox()
spotify_page = SpotifyPlaylist(driver)
username = "cubeofcheese@gmail.com"
password = "1kikidog"

login_btn = driver.find_element_by_css_selector('button#login-button.btn.btn-block.btn-green.ng-binding')

print login_btn
spotify_page.login(username, password)
spotify_page.open_album('71QyofYesSsRMwFOTafnhB')
