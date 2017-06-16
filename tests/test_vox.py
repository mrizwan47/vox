#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_vox
----------------------------------

Tests for `vox` module.
"""


import unittest
import os
from click.testing import CliRunner

from vox import api
from vox import cli


class Test_vox(unittest.TestCase):

	# TODO: More tests

	def test_command_line_interface(self):
		target_string = '--help  Show this message and exit.'
		runner = CliRunner()
		help_result = runner.invoke(cli.main, ['--help'])
		self.assertEqual(help_result.exit_code, 0)
		self.assertTrue(target_string in help_result.output)
