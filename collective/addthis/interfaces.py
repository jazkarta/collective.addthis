# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema
from collective.addthis import _
from plone.theme.interfaces import IDefaultPloneLayer


class IAddThis(Interface):
    """ AddThis marker """


class IAddthisBrowserLayer(IDefaultPloneLayer):
    """Addthis marker"""


class IAddThisControlPanel(Interface):
    """ AddThis Controlpanel marker"""


class IAddThisSettings(Interface):
    """
    AddThis control panel settings used to effect the rendering of the
    addthis viewlet.
    """

    addthis_url = schema.URI(
        title=_(u"AddThis URL"),
        required=False,
        default="http://www.addthis.com/bookmark.php?v=250&amp;username=xa-4ec2c45d56847e04")

    addthis_script_url = schema.URI(
        title=_(u"AddThis JavaScript URL"),
        required=False,
        default="http://s7.addthis.com/js/250/addthis_widget.js#pubid=xa-4ec2c45d56847e04&async=1")

    addthis_chicklets = schema.List(
        title=_(u"Social media selection"),
        description=_(u"A list of social media items that will be displayed "
                       "along side the share link as individual chicklets."),
        required=False,
        default=[],
        value_type=schema.Choice(title=_(u"Social media"),
                                 vocabulary="AddThis Social Media"),
        )

    addthis_data_track_addressbar = schema.Bool(
        title=_(u"Address Bar Sharing"),
        description=_(u"(Beta). Measures when users copy your URL from their"
                       " browser. Add an analytics fragment to the URL."),
        default=False,
        )

    addthis_data_track_clickback = schema.Bool(
        title=_(u"Add clickback tracking variable to URL"),
        description=_(u"Use this to track how many people come back to your "
                       "content via links shared with AddThis."),
        default=False,
        )


class ISocialMedia(Interface):
    """A source of listing of social media supported by the addthis service."""

    sources = schema.Iterable(
        title=_(u"Social media sources"),
        description=_(u"A list of valid social media."),
        )
