# Twitter UI Automation Demo

## Prerequistes
- Python 3.7
- Chrome v89
- [Twitter Developer Account](https://developer.twitter.com/en) 

## Setup
- Create virtualenv :  `python -m venv venv`
- Use virtualenv : `source venv/Scripts/activate`
- Install pip requirements : `pip install -r requirements.txt`

## Configuration
The following variables are needed to run the demo.

- TEST_USER : Twitter login user
- PASSWORD : Twitter login password
- TWITTER_BEARER_TOKEN : Twitter bearer token (developer account)
- TWITTER_API_SECRET : Twitter Secret (developer account)
- TWITTER_API_KEY : Twitter API Key (developer account)

Recommended to create a .env file with the above fields populated.

Or

User can modify config.py file
## Run Tests
- Run pytest command: `pytest`