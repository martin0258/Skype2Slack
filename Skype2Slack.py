#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the MIT license.

"""
This script posts Skype messages to Slack.
"""

import os
import argparse
import ConfigParser
import sys
import requests
import Skype4Py


def send_message_to_slack(msg):
    return requests.post(bot_url, data=msg, params=post_params)


class SkypeEventHandler:
    @staticmethod
    def monitor_message(msg, stat):
        if not stat == "RECEIVED":
            return

        msgBody = msg.Body.strip()
        print stat, msg.FromHandle, msgBody

        # Send message to Slack channel
        msg2Slack = "(Skype) *%s*: %s" % (msg.FromDisplayName, msgBody)
        response = send_message_to_slack(msg2Slack)
        print response


# main program
if __name__ == "__main__":
    # Command-line arguments
    description = "===== Skype2Slack: Send Skype messages to Slack ====="
    print description
    parser = argparse.ArgumentParser(description=description)
    config_help = 'config file. Default [app.cfg].'
    parser.add_argument('-c', '--config', default='app.cfg', help=config_help)
    args = parser.parse_args()

    # Read configurations from config file
    folder = os.path.dirname(os.path.abspath(__file__))
    config_path = "%s/%s" % (folder, args.config)
    config = ConfigParser.ConfigParser()
    config.optionxform = str
    config.read(config_path)
    bot_url = config.get('Slack', 'bot_url')
    channel = config.get('Slack', 'channel')
    post_params = {'channel': channel}

    # Create an instance of the Skype class.
    skype = Skype4Py.Skype()

    # Connect the Skype object to the Skype client.
    skype.Attach()

    skype.OnMessageStatus = SkypeEventHandler.monitor_message

    # Welcome
    welcome_msg = "Hi, I've been told to post your Skype messages here. " + \
                  "Happy *Skype2Slacking*! :smile:"
    # send_message_to_slack(welcome_msg)

    raw_input("(Press ENTER to exit)\nWaiting for Skype messages...")
    exit_msg = 'Hi, *Skype2Slack* just left me! Hope to help you next time~'
    # send_message_to_slack(exit_msg)
    sys.stdout.close()
    sys.stderr.close()
    sys.exit(0)
