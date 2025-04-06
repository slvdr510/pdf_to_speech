##########################################################

# IMPORTS

import json, vlc, fitz
from pynput.keyboard import Key, Listener
from gtts import gTTS

##########################################################

# FUNCTIONS

def loadBookmarkJsonData(bookmark_file_name):
    with open(bookmark_file_name) as json_file:
        bookmarkData = json.load(json_file)

        global pdf_name
        global language
        global begin_page
        global end_page
        global current_page

        pdf_name = bookmarkData['pdf_name']
        language = bookmarkData['language']
        begin_page = bookmarkData['begin_page']
        end_page = bookmarkData['end_page']
        current_page = bookmarkData['current_page']-1

def text_to_mp3_file(text, language): # Opciones de lenguaje: es, en
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")

paused = True

pressed_keys = set()
def on_press(key):
    global pressed_keys
    global paused
    global media_player

    try:
        if key == Key.ctrl_l or key == Key.alt_l:
            pressed_keys.add(key)
        if Key.ctrl_l in pressed_keys and Key.alt_l in pressed_keys:
                        
            if media_player.get_state() != vlc.State.Playing:
                paused = True
            elif media_player.get_state() != vlc.State.Paused:
                paused = False
        
        if paused and media_player.get_state() != vlc.State.Playing:
            media_player.set_pause(0)
        elif not paused and media_player.get_state() != vlc.State.Paused:
            media_player.set_pause(1)

    except AttributeError as ex:
        print(ex)

def on_release(key):
    global pressed_keys
    try:
        if key == Key.ctrl_l or key == Key.alt_l:
            pressed_keys.remove(key)
    except KeyError:
        pass

def play_mp3_file():
    global vlc_instance
    global media_player

    # Load the audio file
    media = vlc_instance.media_new("output.mp3")

    # Set the media for the media player
    media_player.set_media(media)

    # Play the media
    media_player.play()

    listener = Listener(on_press=on_press, on_release=on_release).start()

    # Wait for playback to finish
    while media_player.get_state() != vlc.State.Ended:
        continue
    
    # Release the media player and instance
    media_player.release()
    vlc_instance.release()


def increment_current_page():
    
    with open(bookmark_file_name, 'r') as json_file:
        dataToModify = json.load(json_file)

        dataToModify['current_page'] = dataToModify['current_page']+1

    with open(bookmark_file_name, 'w') as json_file:
        json.dump(dataToModify, json_file, indent=4)


##########################################################

# CUSTOMIZATION

addingPageEnumeration = True


##########################################################

# MAIN

# Task: create Menu for BOOKMARK'S management

# hacer esto seleccionando el archivo de una lista
bookmark_file_name = 'eloquent_js_spanish__BOOKMARK.json'

pdf_name = ""
language = ""
begin_page = 0
end_page = 0
current_page = 0

loadBookmarkJsonData(bookmark_file_name)

with fitz.open(f"{pdf_name}.pdf") as doc:
    
    # If it's 1st time using a bookmark, re-asign current_page
    if current_page not in range(begin_page-1, end_page-1):

        with open(bookmark_file_name, 'r') as json_file:
            dataToModify = json.load(json_file)

            dataToModify['current_page'] = begin_page

        with open(bookmark_file_name, 'w') as json_file:
            json.dump(dataToModify, json_file, indent=4)

        loadBookmarkJsonData(bookmark_file_name)

    # Start playing audio
    for page_num in range(current_page, end_page):
        
        loadBookmarkJsonData(bookmark_file_name)

        text = ""

        # Manual Add Page enumeration
        if addingPageEnumeration:
            if language == 'en':
                text += f"Page {page_num+1}.. "
            elif language == 'es':
                text += f"Página {page_num+1}.. "
    
        # Get text from the current_page of the pdf
        text += doc.load_page(page_num).get_text()

        # PARA PODER TRADUCIR, DESCOMENTAR
        text_to_mp3_file(text, language)

        # Create a VLC media player instance
        vlc_instance = vlc.Instance()

        # Create a media player object
        media_player = vlc_instance.media_player_new()

        # Set the playback speed
        media_player.set_rate(1.4)  # Set speed to 1.4x. Max speed rate is 4.0x.

        play_mp3_file()

        increment_current_page()