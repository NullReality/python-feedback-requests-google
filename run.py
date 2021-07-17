#! /usr/bin/env python3

import os
import requests

feedbackDir = '/data/feedback'
feedbackDic = {}
url = "http://HOSTNAME/feedback/"

def run():
    dirs = os.listdir(feedbackDir)

    for file in dirs:
        with open(os.path.join(feedbackDir, file)) as feedback:
            lines = feedback.read().splitlines()
            feedbackDic['title'] = lines[0]
            feedbackDic['name'] = lines[1]
            feedbackDic['date'] = lines[2]
            feedbackDic['feedback'] = lines[3]

            req = requests.post(url, data=feedbackDir)
            req.raise_for_status()
            print(str(req.ok))

if __name__ == "__main__":
    run()