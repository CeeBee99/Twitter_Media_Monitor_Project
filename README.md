Twitter Image Downloader
Overview
Twitter Image Downloader is a Python application that allows users to monitor specific Twitter accounts for new media images, automatically downloading them to a local directory. The app uses Selenium for web scraping and Tkinter for a simple graphical user interface (GUI).

Features
Monitor multiple Twitter accounts or Twitter profile URLs.
Automatically download the latest media images from monitored accounts.
Label and favorite specific Twitter accounts within the application.
Receive notifications when a new image is downloaded from a favorite account.
User-friendly GUI built with Tkinter for ease of interaction.
Prerequisites
Before running this project, make sure you have the following installed:

Python 3.x
Selenium
BeautifulSoup
Webdriver Manager
Requests
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/Twitter_Image_Downloader.git
Navigate to the project directory:
bash
Copy code
cd Twitter_Image_Downloader
Set up a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Run the application:
bash
Copy code
python main.py
In the GUI, enter the Twitter handle or URL of the user you want to monitor.
Add the user to the list, and the application will start monitoring for new media images.
You can label or favorite users, and the app will notify you when new images are downloaded for favorited users.
GUI Features
Add User: Enter a Twitter handle or URL and click this button to start monitoring the user.
Add Label: Assign a label to a user to easily identify them.
Favorite User: Mark a user as a favorite. Favorited users will trigger notifications when new images are downloaded.
Project Structure
bash
Copy code
📂 Twitter_Image_Downloader/
├── 📂 gui.py               # Handles the graphical user interface.
├── 📂 twitter_monitor.py    # Contains functions for monitoring Twitter accounts.
├── 📂 image_downloader.py   # Contains image downloading and saving functionality.
├── 📂 requirements.txt      # Lists required packages.
└── main.py                  # Main entry point for the application.
Known Issues
Twitter might block requests after frequent media downloads due to rate limiting.
The application depends on web scraping and is thus subject to changes in Twitter's website structure.
Only the latest media image from a user is downloaded.
Future Improvements
Add support for downloading media beyond just the latest image.
Enhance error handling and rate-limiting mechanisms.
Support for other media types such as videos.
Contributing
Fork the repository.
Create a new branch for your feature or bug fix:
bash
Copy code
git checkout -b feature-name
Make your changes and commit them:
bash
Copy code
git commit -m "Add feature"
Push to the branch:
bash
Copy code
git push origin feature-name
Create a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any issues or inquiries, please contact cbphilips00@gmail.com
