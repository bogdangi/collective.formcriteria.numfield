from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.formcriteria.numfield


COLLECTIVE_FORMCRITERIA_NUMFIELD = PloneWithPackageLayer(
    zcml_package=collective.formcriteria.numfield,
    zcml_filename='testing.zcml',
    gs_profile_id='collective.formcriteria.numfield:testing',
    name="COLLECTIVE_FORMCRITERIA_NUMFIELD")

COLLECTIVE_FORMCRITERIA_NUMFIELD_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_FORMCRITERIA_NUMFIELD, ),
    name="COLLECTIVE_FORMCRITERIA_NUMFIELD_INTEGRATION")

COLLECTIVE_FORMCRITERIA_NUMFIELD_FUNCTIONAL = FunctionalTesting(
    bases=(COLLECTIVE_FORMCRITERIA_NUMFIELD, ),
    name="COLLECTIVE_FORMCRITERIA_NUMFIELD_FUNCTIONAL")
