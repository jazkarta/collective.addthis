from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.testing import z2


class AddThisTests(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        z2.installProduct(app, 'collective.addthis')

        # Load ZCML
        import collective.addthis
        self.loadZCML(name='configure.zcml', package=collective.addthis)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        applyProfile(portal, 'collective.addthis:default')

    def tearDownZope(self, app):
        pass


ADDTHIS_FIXTURE = AddThisTests()
ADDTHIS_INTEGRATION_TESTING = IntegrationTesting(bases=(ADDTHIS_FIXTURE,), name="AddThisTests:integration")
ADDTHIS_FUNCTIONAL_TESTING = FunctionalTesting(bases=(ADDTHIS_FIXTURE,), name="AddThisTests:functional")
