import requests
from bs4 import BeautifulSoup

def decode_secret_message(url):
    # Step 1: Retrieve the document content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the document: {response.status_code}")
        return

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'lxml')

    # Step 3: Find the table containing the coordinates and characters
    table = soup.find('table')  # Find the first table in the document

    if not table:
        print("No table found in the document.")
        return

    # Step 4: Process the table rows and extract coordinates and characters
    rows = table.find_all('tr')

    coordinates = []
    max_x = 0
    max_y = 0

    print("Debugging x, y coordinates and characters:")

    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        if len(cols) != 3:
            print(f"Skipping malformed row: {row}")
            continue

        try:
            x_str = cols[0].text.strip()
            char = cols[1].text.strip()
            y_str = cols[2].text.strip()

            x, y = int(x_str), int(y_str)
            coordinates.append((x, y, char))

            # Track the maximum coordinates to size the grid
            max_x = max(max_x, x)
            max_y = max(max_y, y)

            # Debug: Print the x, y coordinates and the character being processed
            print(f"x: {x}, y: {y}, character: '{char}'")

        except ValueError:
            print(f"Skipping row with invalid data: {row}")
            continue

    # Step 5: Create an empty grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 6: Place characters into the grid, adjusting the y-coordinate (invert the grid vertically)
    for x, y, char in coordinates:
        grid[max_y - y][x] = char  # Flip y-axis when placing characters

    # Step 7: Print the grid
    print("\nResulting grid:")
    for row in grid:
        print(''.join(row))


# URL of the document containing the coordinates and characters
# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"
# Call the function to decode and print the coordinates and characters
decode_secret_message(url)
