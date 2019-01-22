from selenium import webdriver
import time

def input():
    search_type = raw_input('Search for artist or song? [a/s]: ')
    if (search_type == 'a'):
        search_term = raw_input('Enter artist: ')
        startPlayList(search_term)
    elif (search_type == 's'):
        search_term = raw_input('Enter song: ')
        startVideo(search_term)
    else:
        input()

def skipAd(driver, player_status):
    if (player_status == -1 or player_status == 3):                             # -1 and 3 are ad states on youtube
        print "ad started"
        time.sleep(4)
        print "waited for skip button"
    if (len(driver.find_elements_by_class_name('ytp-ad-skip-button')) > 0):
        skip_button = driver.find_element_by_class_name('ytp-ad-skip-button')
        print skip_button
        skip_button.click()
    if (len(driver.find_elements_by_class_name('videoAdUiSkipButton')) > 0):
        skip_button = driver.find_element_by_class_name('videoAdUiSkipButton')
        print skip_button
        skip_button.click()

def startPlayList(search_term):
    driver = webdriver.Chrome()
    uri = "https://www.youtube.com/results?search_query="
    driver.get(uri + search_term)

    if (len(driver.find_elements_by_id('hero')) > 0):                           #Side Mix
        print "side mix"
        side_mix = driver.find_element_by_id('hero')
        side_mix.click()
        quit = raw_input()
        if quit == 'q':
            driver.quit()
            input()
    elif (len(driver.find_elements_by_tag_name('ytd-radio-renderer')) > 0):     #Mix in search results
        print 'mix'
        results_mix = driver.find_element_by_tag_name('ytd-radio-renderer')
        results_mix.click()
        quit = raw_input()
        if quit == 'q':
            driver.quit()
            input()

    elif (len(driver.find_elements_by_tag_name('ytd-playlist-thumbnail')) > 0): #Playlist in search results
        playlist = driver.find_element_by_tag_name('ytd-playlist-thumbnail')
        playlist.click()
        print "playlist"
        quit = raw_input()
        if quit == 'q':
            driver.quit()
            input()
    else:                                                                       #Playlist not found
        print "Sorry, artist playlist not found"
        driver.quit()
        input()

def startVideo(search_term):
    driver = webdriver.Chrome()
    uri = "https://www.youtube.com/results?search_query="
    driver.get(uri + search_term)
    first_vid = driver.find_element_by_tag_name('ytd-video-renderer')
    first_vid.click()
    print "video"
    time.sleep(3)
    player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
    print player_status
    skipAd(driver, player_status)

    # player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
    # while (player_status == -1):
    #     time.sleep(1)
    #     player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")

    # minutes = driver.find_element_by_class_name('ytp-time-duration').text[0]
    # seconds = driver.find_element_by_class_name('ytp-time-duration').text[2] + driver.find_element_by_class_name('ytp-time-duration').text[3]
    # video_length = int(minutes)*60 + int(seconds)
    quit = raw_input()
    if quit == 'q':
        driver.quit()
        input()

input()
# startPlayList()
