# -*- coding: utf-8 -*-

import unittest

from plone.browserlayer.utils import registered_layers

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.addthis.testing import ADDTHIS_INTEGRATION_TESTING

PROJECTNAME = 'collective.addthis'


class InstallTestCase(unittest.TestCase):

    layer = ADDTHIS_INTEGRATION_TESTING

    def test_installed(self):
        qi = getattr(self.layer['portal'], 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('IAddThisBrowserLayer' in layers,
                        'add-on layer was not installed')


class UninstallTestCase(unittest.TestCase):

    layer = ADDTHIS_INTEGRATION_TESTING

    def test_uninstalled(self):
        qi = getattr(self.layer['portal'], 'portal_quickinstaller')
        qi.installProducts(products=[PROJECTNAME])
        qi.uninstallProducts(products=[PROJECTNAME])
        self.assertFalse(qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_removed(self):
        qi = getattr(self.layer['portal'], 'portal_quickinstaller')
        qi.installProducts(products=[PROJECTNAME])
        qi.uninstallProducts(products=[PROJECTNAME])
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('IAddThisBrowserLayer' not in layers,
                        'add-on layer was not removed')
