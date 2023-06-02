#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:06:08 2023

@author: apy12
"""

__app_name__ = 'metodo'
__version__ = '0.1.0'

(SUCCESS,
 DIR_ERROR, FILE_ERROR,
 DB_READ_ERROR, DB_WRITE_ERROR,
 JSON_ERROR, ID_ERROR,) = range(7)

ERRORS = {
    DIR_ERROR: 'config directory error',
    FILE_ERROR: 'config file error',
    DB_READ_ERROR: 'database read error',
    DB_WRITE_ERROR: 'database write error',
    ID_ERROR: 'to-do id error',}
