
# WrestleAI

WrestleAI is a comprehensive application designed to enhance the training, analysis, and overall experience for wrestlers, coaches, and supporters. This app leverages advanced AI technology to provide personalized assistance, video analysis, and a seamless user experience for all its users.

## Features

- **AI Assistant**: Provides personalized assistance to wrestlers, coaches, and supporters.
- **Video Upload and Analysis**: Upload wrestling videos for detailed analysis and feedback.
- **User Management**: Supports user registration, login, and account management.
- **Payment Integration**: Secure payment processing for premium features.
- **Customizable Home Page**: Tailored home page experience for different user types (athletes, coaches, supporters).

## Repository Structure
```bash
├── .streamlit
│   ├── config.toml
│   ├── secrets.toml
├── assets
│   ├── terms
│   ├── images
│   │   ├── general
│   │   ├── logo
│   │   ├── umich
│   │   ├── qrcodes
│   ├── docs
│   │   ├── pdf
│   │   ├── text
│   │   ├── markdown
├── classes
│   ├── clsSessionState.py
│   ├── clsPageSetup.py
│   ├── cls
├── app
│   ├── userstate
│   │   ├── appUserState.py
│   │   ├── components
│   │   │   ├── appRender.py
│   │   │   ├── appInfo.py
│   │   │   ├── appPayment.py
│   │   │   ├── appLogin.py
│   │   │   ├── appWelcome.py
│   ├── homepage
│   │   ├── appHomePage.py
│   │   ├── components
│   │   │   ├── appAthlete.py
│   │   │   ├── appCoach.py
│   │   │   ├── appSupporter.py
│   ├── assistant
│   │   ├── appAssistant.py
│   │   ├── components
│   │   │   ├── appUserAssistant.py
│   │   │   ├── appGuestAssistant.py
│   │   │   ├── appAssistantPreWork.py
│   ├── account
│   │   ├── appAccount.py
│   │   ├── components
│   │   │   ├── appCreateAccount.py
│   │   │   ├── appLoginAccount.py
├── styles
│   ├── style.css
├── pages
│   ├── 1_Home.py
│   ├── 1_AI_Assistant.py
│   ├── 3_Video_Upload.py
│   ├── 4_Settings.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation
To run WrestleAI locally, follow these steps:

Clone the repository:
```bash
git clone https://github.com/yourusername/WrestleAI.git
cd WrestleAI
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run main.py
```

## Usage

### UserState

**Overview**:
The UserState goes through five different states, which represents the new user path and is the most complex. Steps in the UserState may be skipped or bypassed for existing users. The user is considered new until they have completed Payment step in which they are considered existing users to simplify the experience of returning from payment.

The following outlines the UserState flow:

1. **Render**: The initial view when the user comes to WrestleAI. They will be considered a guest usertype at this point. They will have options to interact with the Guest Assistant, sign in as an existing user, or register as a new user.
2. **Info**: Info refers to the new user information needed to create an account. Once this information is captured, the user will proceed to payment.
3. **Payment**: The user will be required to submit payment, which navigates them out of the current app session via a stripe payment link button to another tab. Upon successful completion, the user will be redirected back to the app with information stored in query params.
4. **Login**: At this step, all users are considered existing and will be asked to provide username and password to authenticate. This is the default step for existing users and users returning from payment.
5. **Welcome**: Welcome is simply ensuring all attributes are captured in the session state and navigation to Home Page (pages/1_Home.py). The user will never be brought back to the original UserState screen again during their session.

### AI Assistant
The AI Assistant is designed to provide personalized assistance to different user types. It can help with training tips, match analysis, and general support.

### Video Upload and Analysis
Users can upload their wrestling videos for detailed analysis. The AI analyzes the videos and provides feedback to help improve performance.

## Packages
Below is the list of required packages:

```bash
    plaintext
    altair                      # Declarative statistical visualization library for Python
    asyncio                     # Asynchronous I/O, event loop, and coroutine support
    beautifulsoup4              # Library for parsing HTML and XML documents
    bs4                         # Another name for BeautifulSoup, used for web scraping
    extra-streamlit-components  # Custom and extra components for Streamlit applications
    fastapi                     # Fast and modern web framework for building APIs
    ffmpeg                      # Tool for handling multimedia data
    folium                      # Python library for interactive maps using Leaflet.js
    google-api-python-client    # Google APIs Python client library
    google-search-results       # API for retrieving search results from Google
    googlemaps                  # Python client for Google Maps services
    IPython                     # Interactive computing environment for Python
    moviepy                     # Video editing library for Python
    nest-asyncio                # Allows nested use of asyncio.run and event loops
    numpy                       # Fundamental package for numerical computing
    opencv-python-headless      # OpenCV library for computer vision tasks without GUI
    pandas                      # Data manipulation and analysis library
    pathlib                     # Object-oriented filesystem paths
    pillow                      # Python Imaging Library (PIL) fork for image processing
    playwright                  # Browser automation library for Python
    plotly                      # Interactive graphing library
    plotly.express              # Simple syntax for complex Plotly visualizations
    pydantic                    # Data validation and settings management using Python type annotations
    pydub                       # Manipulate audio with an intuitive interface
    pygwalker                   # Visualization tool for exploring pandas DataFrames
    PyScrappy                   # Web scraping library for Python
    pytube                      # Python library for downloading YouTube videos
    pyzillow                    # Python wrapper for Zillow API
    requests                    # Simple HTTP library for Python
    scrapegraphai               # Scrape data from graphs and charts
    Scrapy                      # Web crawling and scraping framework
    simple-salesforce           # Simple Salesforce API wrapper for Python
    SpeechRecognition           # Library for performing speech recognition with Python
    streamlit                   # Framework for creating interactive web apps from Python scripts
    streamlit-antd-components   # Ant Design components for Streamlit apps
    streamlit-echarts           # ECharts components for Streamlit apps
    streamlit-elements          # Streamlit component library for building complex UIs
    streamlit-extras            # Additional components and utilities for Streamlit
    streamlit-folium            # Folium integration for Streamlit apps
    stripe                      # Python library for Stripe API integration
    supabase                    # Python client for Supabase, a Firebase alternative
    tavily-python               # Tavily Python client for machine learning tasks
    temp                        # Temporary file and directory management
    tiktoken                    # Tokenizer for OpenAI models
    typing                      # Type hints for Python
    urllib3                     # HTTP library with thread-safe connection pooling
    webscraping                 # General web scraping library
    WebScraperAPI               # API for web scraping tasks
    yelpapi                     # Python client for Yelp Fusion API
    youtube-transcript-api      # Retrieve YouTube video transcripts with Python
    youtube_dl                  # Download videos from YouTube and other sites
```

## Contact
For any questions or support, please contact us at support@wrestleai.com.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
