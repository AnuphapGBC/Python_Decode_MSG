
# Secret Message Decoder

This project retrieves a secret message from a Google Docs URL, decodes it by extracting coordinates and characters from a table, and prints the message as a grid.

## How It Works

The Python script uses the `requests` library to fetch an HTML document from the provided URL, and the `BeautifulSoup` library to parse the HTML content. It specifically extracts a table containing `x`, `y` coordinates and corresponding characters. The script then populates a grid using these coordinates, flipping the y-axis to ensure correct orientation, and finally prints the decoded message in the correct order.

### Example Output

Given the following table:
```
x  | character | y
0  | █         | 0
1  | ▀         | 1
...
```

The output will be:
```
█▀▀▀
█▀▀ 
█   
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script by providing the Google Docs URL:
```bash
python decode_secret_message.py
```

## Dependencies

- `requests`
- `beautifulsoup4`
- `lxml`

Install them using:
```bash
pip install requests beautifulsoup4 lxml
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
