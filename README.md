# Transcribble

This is web application that take .mp4 video file and transcribes video into text using Python, Django, SpeechRecognition library 

## Installation:
#### 1. Clone the repository
`git clone https://github.com/sonaljain067/Transcribble.git
`

#### 2. Create a virtual environment
`cd SocialScape` <br/>
`python3 -m venv env` or `virtualenv env` 
to create virtual environment named `env`

#### 3. Activate the virtual environment
In Ubuntu: `source env/bin/activate` <br/>
In Windows: `.\env\Scripts\activate`

#### 4. Install dependencies
`pip install -r requirements.txt`

#### 5. Setup database 
`python manage.py migrate`

#### 6. Run the server
`python manage.py runserver`


## Usage
1. Upload a video URL(with .mp4 link) to the application
2. The application will download the video and convert it into audio file
3. The audio file will then be transcribed using SpeechRecogition library
4. The transcript will be saved to the saved and displayed to the user 


## Requirements
- Python (3.8 or higher)
- Django (3.2 or higher)
- SpeechRecognition (3.8.1 or higher)
- PyDub (0.25.1 or higher)
- Requests (2.25.1 or higher)
- FFMpeg (4.2 or higher)
