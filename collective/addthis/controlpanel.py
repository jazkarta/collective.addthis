from plone.app.registry.browser import controlpanel
from collective.addthis.interfaces import IAddThisSettings
from collective.addthis import _


class AddThisSettingsForm(controlpanel.RegistryEditForm):
    schema = IAddThisSettings
    label = _(u"AddThis settings")
    description = _(u"Set your own AddThis URL and social media chicklets "
                     "by using this form")

    def updateFields(self):
        super(AddThisSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(AddThisSettingsForm, self).updateWidgets()


class AddThisControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AddThisSettingsForm
