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


class SkypeEventHandler:
    @staticmethod
    def monitor_message(msg, stat):
        if not stat == "SENDING":
            return

        msgBody = msg.Body.strip()
        print stat, msg.FromHandle, msgBody

        # Send message to Slack channel
        msg2Slack = "[Skype] %s: %s" % (msg.FromHandle, msgBody)
        response = requests.post(bot_url, data=msg2Slack, params=post_params)
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

    raw_input("Waiting for Skype messages (Press ENTER to finish)\n")
    print 'Thank you for using skyfire! Bye=)'
    sys.stdout.close()
    sys.stderr.close()
    sys.exit(0)
