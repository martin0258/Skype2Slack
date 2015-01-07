# Skype2Slack
Send Skype messages to Slack

## Usage
1. Install [dependency](#dependency)
2. Download this repo
3. Edit [app.cfg] with your settings
4. Run Skype and log in with your account
5. Run script: `python Skype2Slack.py`

## Dependency
1. [python](https://www.python.org)
2. [python module - Skype4Py](https://github.com/awahlig/skype4py)
3. [python module - requests](http://docs.python-requests.org/en/latest/)

## How to find my settings for [app.cfg]
### Bot URL
`Slack` > `Configure Integrations` > `Slackbot` > `Post messages as Slackbot` > `Your slackbot URL`

### Channel
Channel: #general  
Direct message: @user_id (e.g., @martin)

[app.cfg]: ./app.cfg
