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
        self.registry = Registry()
        self.registry.registerInterface(IAddThisSettings)

    def test_is_addthis_installed(self):
        qi = getToolByName(self.layer['portal'], 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled('collective.addthis'))

    def test_are_resources_registered(self):
        js = getToolByName(self.layer['portal'], 'portal_javascripts')
        css = getToolByName(self.layer['portal'], 'portal_css')
        self.assertTrue('++resource++collective.addthis/addthis.js' in
            js.getResourceIds())
        self.assertTrue('++resource++collective.addthis/addthis.css' in
            css.getResourceIds())


class FunctionalTest(unittest.TestCase):

    layer = ADDTHIS_FUNCTIONAL_TESTING

    def test_is_addthis_visible(self):
        browser = Browser(self.layer['portal'])
        browser.open(self.layer['portal'].absolute_url())
        self.assertTrue('http://www.addthis.com/bookmark.php?v=250'\
            in browser.contents)
