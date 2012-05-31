# -*- coding: utf-8 -*-
import json
import urllib
import socket
from zope.interface import implements, alsoProvides
from zope import component
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from collective.addthis.interfaces import ISocialMedia
from Products.Five.browser import BrowserView
from plone.registry.interfaces import IRegistry

SHARING = "http://cache.addthiscdn.com/services/v1/sharing.en.json"


class SocialMediaSources(object):
    """Provides a list of Social Media supported by the addthis.com service."""
    implements(ISocialMedia)

    def _services(self):
        """Returns the services using that addthis API"""
        registry = component.queryUtility(IRegistry)
        return registry.get('collective.addthis.socialmediasources', [])

    @property
    def sources(self):
        for service in self._services():
            code, name = service.split('|')
            yield (name, code,)
        raise StopIteration


def socialMediaVocabulary(context):
    """Vocabulary factory for social media sources."""
    utility = component.getUtility(ISocialMedia)
    terms = [SimpleTerm(value, token, token)
             for token, value in utility.sources]
    return SimpleVocabulary(terms)

alsoProvides(socialMediaVocabulary, IVocabularyFactory)


class SocialMediaUpdater(BrowserView):
    """Update the data used by the vocabulary"""

    def __call__(self):
        raw_services = self._services()
        if not raw_services:
            return u"no services retrieved, don't update the configuration"
        services = []
        for service in raw_services:
            try:
                unicode(service[u'name'], 'utf-8')
            except TypeError:
                value = service[u'name'].encode('ascii', 'ignore')
                service[u'name'] = unicode(value)
            services.append("%s|%s" % (service[u'code'], service[u'name']))
        # TODO: save in registry
        registry = component.queryUtility(IRegistry)
        registry['collective.addthis.socialmediasources'] = tuple(services)
        return u"%s services retrieved" % len(services)

    def _services(self):
        """Returns the services using that addthis API"""
        try:
            old_default = socket.getdefaulttimeout()
            socket.setdefaulttimeout(5)
            response = urllib.urlopen(SHARING)
            socket.setdefaulttimeout(old_default)
        except IOError:
            return []
        except socket.timeout:
            return []

        if response.code == 200:
            data = json.load(response)
            if data:
                return data[u'data']
        return []
