# -*- coding: utf-8 -*-

#imports for unittest
import unittest
from collective.addthis.tests.base import ADDTHIS_INTEGRATION_TESTING
from collective.addthis.tests.base import ADDTHIS_FUNCTIONAL_TESTING
from collective.addthis.interfaces import IAddThisControlPanelForm
from plone.testing.z2 import Browser
from Products.CMFCore.utils import getToolByName


class IntegrationTest(unittest.TestCase):

    layer = ADDTHIS_INTEGRATION_TESTING

    #### INITIALIZE AND SETUP SECTION ####
    def setUp(self):
        ''' Initialize the portal '''
        self.portal = self.layer['portal']

    def test_is_addthis_installed(self):
        qi = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(qi.isProductInstalled('collective.addthis'))

    def test_is_controlpanel_available(self):
        portal_controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        action_ids = [action.id for action in portal_controlpanel.listActions()]
        self.assertTrue('setAddThisSettings' in action_ids)

    def test_controlpanel_chicklets(self):
        form = IAddThisControlPanelForm(self.portal)
        self.assertTrue(('facebook', 'blogger', 'livejournal', 'wordpress', 'google', 'twitter') == \
                        form.get_addthis_chicklets())

    def test_controlpanel_addthis_url(self):
        form = IAddThisControlPanelForm(self.portal)
        self.assertTrue(form.addthis_url == \
            "http://www.addthis.com/bookmark.php?v=250&username=xa-4b7fc6a9319846fd")

    def test_controlpanel_addthis_script_url(self):
        form = IAddThisControlPanelForm(self.portal)
        self.assertTrue(form.addthis_script_url == \
            "http://s7.addthis.com/js/250/addthis_widget.js#username=xa-4b7fc6a9319846fd")

    def test_controlpanel_set_addthis_chicklets(self):
        form = IAddThisControlPanelForm(self.portal)
        form.set_addthis_chicklets(('twitter', 'facebook'))
        self.assertTrue(form.get_addthis_chicklets() == ('twitter', 'facebook'))

    def test_controlpanel_set_addthis_url(self):
        form = IAddThisControlPanelForm(self.portal)
        form.set_addthis_url("http://www.addthis.com/bookmark.php?v=250&username=user")
        self.assertTrue(form.get_addthis_url() == \
            "http://www.addthis.com/bookmark.php?v=250&username=user")

    def test_controlpanel_set_addthis_script_url(self):
        form = IAddThisControlPanelForm(self.portal)
        form.set_addthis_script_url("http://s7.addthis.com/js/250/addthis_widget.js#username=user")
        self.assertTrue(form.get_addthis_script_url() == \
            "http://s7.addthis.com/js/250/addthis_widget.js#username=user")



class FunctionalTest(unittest.TestCase):

    layer = ADDTHIS_FUNCTIONAL_TESTING

    def setUp(self):
        ''' Initialize the portal '''
        self.portal = self.layer['portal']

    def test_is_addthis_visible(self):
        browser = Browser(self.portal)
        browser.open(self.portal.absolute_url())
        self.assertTrue('http://www.addthis.com/bookmark.php?v=250&amp;username='\
            in browser.contents)

