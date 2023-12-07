#!/bin/python
from pybot import Robot
from pybot.module_webapp import create_app
import os
import threading

def run():
    debug = False
    webapp = create_app(root_dir=os.path.dirname(os.path.abspath(__file__)))
    robot = Robot(webapp, debug)
    threading.Thread(target=robot.demarrer()).start()
    webapp.run(debug)

if __name__ == "__main__":
    run()