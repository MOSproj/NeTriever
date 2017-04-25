#!/usr/bin/env python
# -*- coding: utf-8 -*-


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def header(text):
        return bcolors.HEADER + text + bcolors.ENDC

    @staticmethod
    def okeblue(text):
        return bcolors.OKBLUE + text + bcolors.ENDC

    @staticmethod
    def okegreen(text):
        return bcolors.OKGREEN + text + bcolors.ENDC

    @staticmethod
    def warning(text):
        return bcolors.WARNING + text + bcolors.ENDC

    @staticmethod
    def fail(text):
        return bcolors.FAIL + text + bcolors.ENDC

    @staticmethod
    def endc(text):
        return bcolors.ENDC + text + bcolors.ENDC

    @staticmethod
    def bold(text):
        return bcolors.BOLD + text + bcolors.ENDC

    @staticmethod
    def underline(text):
        return bcolors.UNDERLINE + text + bcolors.ENDC

if __name__ == '__main__':
    print bcolors.header("HEADER")
    print bcolors.okeblue("OKBLUE")
    print bcolors.okegreen("OKGREEN")
    print bcolors.warning("WARNING")
    print bcolors.fail("FAIL")
    print bcolors.endc("ENDC")
    print bcolors.bold("BOLD")
    print bcolors.underline("UNDERLINE")
