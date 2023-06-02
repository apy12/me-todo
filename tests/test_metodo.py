#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:38:39 2023

@author: apy12
"""

from typer.testing import CliRunner
from metodo import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ['--version'])
    assert result.exit_code == 0
    assert f'{__app_name__} v{__version__}\n' in result.stdout
