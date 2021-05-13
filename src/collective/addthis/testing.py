from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from zope.configuration import xmlconfig
import collective.addthis


ADDTHIS_FIXTURE = PloneWithPackageLayer(
    zcml_package=collective.addthis,
    zcml_filename='configure.zcml',
    gs_profile_id='collective.addthis:default',
    name="AddThisFixture",
    additional_z2_products=[
        'plone.app.z3cform:default',
        'plone.app.registry:default',
    ],
)
ADDTHIS_INTEGRATION_TESTING = IntegrationTesting(bases=(ADDTHIS_FIXTURE,),
    name="AddThisTests:Integration")
ADDTHIS_FUNCTIONAL_TESTING = FunctionalTesting(bases=(ADDTHIS_FIXTURE,),
    name="AddThisTests:Functional")
