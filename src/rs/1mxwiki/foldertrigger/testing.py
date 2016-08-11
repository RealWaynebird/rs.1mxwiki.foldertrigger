# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import rs.1mxwiki.foldertrigger


class Rs1MxwikiFoldertriggerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=rs.1mxwiki.foldertrigger)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rs.1mxwiki.foldertrigger:default')


RS_1MXWIKI_FOLDERTRIGGER_FIXTURE = Rs1MxwikiFoldertriggerLayer()


RS_1MXWIKI_FOLDERTRIGGER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(RS_1MXWIKI_FOLDERTRIGGER_FIXTURE,),
    name='Rs1MxwikiFoldertriggerLayer:IntegrationTesting'
)


RS_1MXWIKI_FOLDERTRIGGER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(RS_1MXWIKI_FOLDERTRIGGER_FIXTURE,),
    name='Rs1MxwikiFoldertriggerLayer:FunctionalTesting'
)


RS_1MXWIKI_FOLDERTRIGGER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        RS_1MXWIKI_FOLDERTRIGGER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Rs1MxwikiFoldertriggerLayer:AcceptanceTesting'
)
