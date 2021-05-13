# -*- coding: utf-8 -*-

import unittest

from plone.browserlayer.utils import registered_layers

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from collective.addthis.testing import ADDTHIS_INTEGRATION_TESTING

PROJECTNAME = 'collective.addthis'

JAVASCRIPTS = [
    '++resource++collective.addthis/addthis.js',
    ]

CSS = [
    '++resource++collective.addthis/addthis.css',
    ]


class InstallTestCase(unittest.TestCase):

    layer = ADDTHIS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installed(self):
        qi = getattr(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('IAddThisBrowserLayer' in layers,
                        'add-on layer was not installed')

    def test_jsregistry(self):
        resource_ids = self.portal.portal_javascripts.getResourceIds()
        for id in JAVASCRIPTS:
            self.assertTrue(id in resource_ids, '%s not installed' % id)

    def test_cssregistry(self):
        resource_ids = self.portal.portal_css.getResourceIds()
        for id in CSS:
            self.assertTrue(id in resource_ids, '%s not installed' % id)


class UninstallTestCase(unittest.TestCase):

    layer = ADDTHIS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_removed(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertTrue('IAddThisBrowserLayer' not in layers,
                        'add-on layer was not removed')

    def test_jsregistry_removed(self):
        resource_ids = self.portal.portal_javascripts.getResourceIds()
        for id in JAVASCRIPTS:
            self.assertTrue(id not in resource_ids, '%s not removed' % id)

    def test_cssregistry_removed(self):
        resource_ids = self.portal.portal_css.getResourceIds()
        for id in CSS:
            self.assertTrue(id not in resource_ids, '%s not removed' % id)
