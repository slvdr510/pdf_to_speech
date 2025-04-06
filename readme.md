# PDF to Audio Reader with Bookmarking

This Python script reads a PDF file, converts its text to speech, and plays it as an audio file. It also includes bookmarking functionality to remember the last read page.

## Features

-   **PDF to Audio Conversion:** Converts the text content of a PDF page into an MP3 audio file using Google Text-to-Speech (gTTS).
-   **Audio Playback:** Plays the generated MP3 file using VLC media player.
-   **Page Navigation:** Reads pages sequentially from a specified range.
-   **Bookmarking:** Saves the current page number in a JSON file to resume reading from the same point later.
-   **Keyboard Control:** Allows pausing and resuming audio playback using `Ctrl + Alt`.
-   **Configurable Language:** Supports multiple languages for text-to-speech (e.g., Spanish, English).
-   **Page Enumeration:** Optionally adds page numbers to the audio output.

## Requirements

-   Python 3.x
-   Libraries:
    -   `json`
    -   `vlc`
    -   `fitz` (PyMuPDF)
    -   `pynput`
    -   `gTTS`

## Installation

1.  **Install Python:** If you don't have Python installed, download and install it from [python.org](https://www.python.org/).
2.  **Install Libraries:** Open a terminal or command prompt and run the following command:

    ```bash
    pip install PyMuPDF pynput gTTS python-vlc
    ```

3.  **VLC Media Player:** Make sure VLC media player is installed on your system.
4.  **Create a Bookmark File:** Create a JSON file (e.g., `eloquent_js_spanish__BOOKMARK.json`) with the following structure:

    ```json
    {
      "pdf_name": "your_pdf_file_name",
      "language": "es",
      "begin_page": 1,
      "end_page": 10,
      "current_page": 1
    }
    ```

    -   `pdf_name`: The name of your PDF file (without the `.pdf` extension).
    -   `language`: The language code for text-to-speech (e.g., "es" for Spanish, "en" for English).
    -   `begin_page`: The starting page number.
    -   `end_page`: The ending page number.
    -   `current_page`: The page number to start reading from.

## Usage

1.  **Prepare your PDF and Bookmark File:** Place your PDF file and the bookmark JSON file in the same directory as the Python script.
2.  **Run the Script:** Execute the Python script.

    ```bash
    python your_script_name.py
    ```

3.  **Control Playback:**
    -   Press `Ctrl + Alt` to pause or resume playback.

## Customization

-   **`addingPageEnumeration`:** Set this variable to `True` to include page numbers in the audio output, or `False` to exclude them.
-   **Bookmark File:** Modify the `bookmark_file_name` variable in the script to point to your bookmark JSON file.
-   **Playback Speed:** Change the `media_player.set_rate(1.4)` line to adjust the playback speed.

## File Structure