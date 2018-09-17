#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function
from derrick.core.derrick import Derrick
from derrick.core.logger import Logger
import signal


def main():
    # handle control-c and other exit signal
    signal.signal(signal.SIGINT, _exit)
    signal.signal(signal.SIGTERM, _exit)

    dk = Derrick()
    dk.run()


def _exit():
    Logger.warn("Derrick exit because of KeyboardInterrupt.")


if __name__ == "__main__":
    main()
