# Automate-Cookie-Clickers

Welcome to the Automate-Cookie-Clickers repository!

## Installation

## Intall Selenium

If first time install, run this command:
```bash
pip install selenium
```

### Download chrome driver

https://sites.google.com/chromium.org/driver/

- Under `Latest ChromeDriver Binaries`, go to `the Chrome for Testing availability dashboard`.
- Install the `Stable` version.
- Go to `chromedriver` using `win64` version
- Copy the URL to download the zip and move the zip into the project folder.
- Extract the zip into the project folder.
- Move the `chromedriver.exe` into the root of the project folder. Make sure it's in the same level as the script (in my case, it's `main.py`).
- Delete the remaining installed folders/files.
- Paste the name, `chromedriver.exe`, into the `executable_path`.

## Usage

After installing the chrome driver, use this in the `main.py` to test if the driver works:
```bash

driver.get("https://google.com") # go to google.com

time.sleep(10)  # wait/sleep for 10 sec

driver.quit()  # close the window
```

And run this command:
```bash
python main.py
```
