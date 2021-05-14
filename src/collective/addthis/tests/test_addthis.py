# -*- coding: utf-8 -*-
from collective.addthis.testing import ADDTHIS_INTEGRATION_TESTING
from collective.addthis.testing import ADDTHIS_FUNCTIONAL_TESTING
from collective.addthis.interfaces import IAddThisSettings
from Products.CMFCore.utils import getToolByName
from plone.registry import Registry
from plone.testing.z2 import Browser
import unittest


class IntegrationTest(unittest.TestCase):

    layer = ADDTHIS_INTEGRATION_TESTING

    def setUp(self):
        ''' Initialize the portal '''
        qi = getattr(self.layer['portal'], 'portal_quickinstaller')
        qi.installProducts(products=["collective.addthis"])
        self.registry = Registry()
        self.registry.registerInterface(IAddThisSettings)


class FunctionalTest(unittest.TestCase):

    layer = ADDTHIS_FUNCTIONAL_TESTING

    def test_is_addthis_visible(self):
        browser = Browser(self.layer['portal'])
        browser.open(self.layer['portal'].absolute_url())
        self.assertTrue('https://www.addthis.com/bookmark.php?v=250'\
            in browser.contents)
