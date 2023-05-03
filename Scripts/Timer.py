#! /usr/bin/env python3
# Author: Geir Arne Hjelle
# Source: https://realpython.com/python-timer/
# Imports fra system
import time
# Variables
# Main Code
class TimeError(Exception):
    """A custom exception used to report errors from the Timer Class"""

class Timer:
    def __init__(self):
        self._start_time = None
        #self.ID = ID
    def start(self):
        """Start a new timer """
        if self._start_time is not None:
            raise TimeError(f"Timer is running. use .stop() to stop it")
        self._start_time = time.perf_counter()
        
    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimeError(f"Timer is not Running. Use .start() to start it")
        elapsed_time = time.perf_counter() - self._start_time
        Cooldown = elapsed_time
        print(str(Cooldown) + " Cooldown")
        self._start_time = None
        #print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return Cooldown