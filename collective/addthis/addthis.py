from zope.component import getUtility, getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets import common
from plone.registry.interfaces import IRegistry
from plone.memoize import view
from zope.schema.interfaces import IVocabularyFactory
from collective.addthis.interfaces import IAddThisSettings
try:
    import json
except ImportError:
    import simplejson as json

HAS_GA = True
try:
    from collective.googleanalytics import interfaces
except ImportError:
    HAS_GA = False


class AddThisViewlet(common.ViewletBase):
    """ AddThis viewlet """

    index = ViewPageTemplateFile('addthis.pt')

    @property
    def _settings(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IAddThisSettings)
        return settings

    @property
    def chicklets(self):
        chicklet_names = self._settings.addthis_chicklets
        vocab = getUtility(IVocabularyFactory, name="AddThis Social Media")
        chicklets = [term for term in vocab(self.context)
                        if term.value in chicklet_names]
        results = [None] * len(chicklet_names)
        for chick in chicklets:
            results[chicklet_names.index(chick.value)] = chick
        return results

    def getAddThisURL(self):
        """
        Returns URL to AddThis service. If that isn't specified we'll return
        an random URL from AddThis.com when this addon was developed.
        """
        return self._settings.addthis_url or "http://www.addthis.com/bookmark.php?v=250&amp;username=xa-4b7fc6a9319846fd"

    def addthis_config(self):
        addthis_config = {'ui_click': True,
                          'ui_hover_direction': 1,
                          'ui_language': self.language()}
        if self._settings.addthis_data_track_addressbar:
            addthis_config['data_track_addressbar'] = self._settings.addthis_data_track_addressbar

        if self._settings.addthis_data_track_clickback:
            addthis_config['data_track_clickback'] = self._settings.addthis_data_track_clickback

        if HAS_GA:
            analytics_tool = getToolByName(self.context, "portal_analytics", None)
            account_id = None

            if analytics_tool is not None:
                account_id = getattr(analytics_tool, 'tracking_web_property', None)

            if account_id is not None:
                addthis_config['data_ga_property'] = account_id
                addthis_config['data_ga_social'] = True

        return addthis_config

    def addthis_config_javascript(self):
        return "var addthis_config = %s" % json.dumps(self.addthis_config())

    def javascript_url(self):
        return self._settings.addthis_script_url

    def language(self):
        state = getMultiAdapter((self.context, self.request),
                                name=u'plone_portal_state')
        return state.language()
