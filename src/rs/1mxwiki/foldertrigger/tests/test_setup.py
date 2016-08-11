# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from rs.1mxwiki.foldertrigger.testing import RS_1MXWIKI_FOLDERTRIGGER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that rs.1mxwiki.foldertrigger is properly installed."""

    layer = RS_1MXWIKI_FOLDERTRIGGER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if rs.1mxwiki.foldertrigger is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'rs.1mxwiki.foldertrigger'))

    def test_browserlayer(self):
        """Test that IRs1MxwikiFoldertriggerLayer is registered."""
        from rs.1mxwiki.foldertrigger.interfaces import (
            IRs1MxwikiFoldertriggerLayer)
        from plone.browserlayer import utils
        self.assertIn(IRs1MxwikiFoldertriggerLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RS_1MXWIKI_FOLDERTRIGGER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['rs.1mxwiki.foldertrigger'])

    def test_product_uninstalled(self):
        """Test if rs.1mxwiki.foldertrigger is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'rs.1mxwiki.foldertrigger'))

    def test_browserlayer_removed(self):
        """Test that IRs1MxwikiFoldertriggerLayer is removed."""
        from rs.1mxwiki.foldertrigger.interfaces import IRs1MxwikiFoldertriggerLayer
        from plone.browserlayer import utils
        self.assertNotIn(IRs1MxwikiFoldertriggerLayer, utils.registered_layers())
