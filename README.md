# tana-careers


# Tana Careers Page — Selenium Automation

A simple Selenium script that automates navigating the [Tana Careers page](https://www.careers-page.com/tanacareers) through the Tana Fellowship Program (Technical Roles) application flow, up to the point of starting an application.

## What it does

1. Launches Chrome in fullscreen mode
2. Opens the Tana careers page
3. Clicks the **Ready to go** banner button
4. Clicks the **Apply** button for the relevant job listing
5. Clicks the **Apply Position** button on the job detail page
6. Waits for you to press **Enter** in the terminal before closing the browser

## Requirements

- Python 3.7+
- Google Chrome installed
- [Selenium](https://pypi.org/project/selenium/) (Selenium Manager, bundled since Selenium 4.6, handles the ChromeDriver binary automatically — no separate driver download needed)

Install dependencies:

```bash
pip install selenium
```

## Usage

Run the script directly:

```bash
python main.py
```

A Chrome window will open and step through the flow automatically. Once the script reaches the final step, it will pause and print:

```
Press Enter to close the browser...
```

Press **Enter** in your terminal to close the browser and end the script.

## How it works

The script follows a standard Selenium pattern:

```
launch browser → open URL → locate element → perform action → verify/pause → close browser
```
