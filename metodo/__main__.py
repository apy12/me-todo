#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:49:35 2023

Me To-Do entry point script.

@author: linft
"""

from metodo import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == '__main__':
    main()
