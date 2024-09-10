# TikTok Scraping

This script automates interactions with a TikTok user profile using Selenium. It navigates to the specified TikTok profile, scrolls down to load more content, and collects URLs of the current page. The collected URLs are saved to a text file named after the TikTok user.

## Features

- Automatically scrolls through a TikTok user profile.
- Captures and logs URLs of the current page.
- Saves collected URLs to a text file named after the TikTok user.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver (automatically installed via ChromeDriverManager)
- WebDriver Manager

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Edgarmejiav/tiktok-scrapings.git
    ```

2. Navigate into the project directory:
    ```bash
    cd tiktok-scrapings
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open `main.py` and set the `urlget` variable to the TikTok profile URL you want to scrape.

2. Run the script:
    ```bash
    python main.py
    ```

3. The script will scroll through the profile and save URLs to a file named after the TikTok user (e.g., `username.txt`).

4. To stop the script manually, use `Ctrl+C`.

## Notes

- Ensure compliance with TikTok’s terms of service and avoid excessive requests to prevent rate limiting.
- Adjust the `sleep` duration in the script as needed to accommodate network speeds or content loading times.

## Contributing

Feel free to open issues or submit pull requests if you have improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
