from Acquisition import aq_inner, aq_parent
from plone import api
from plone.app.iterate.interfaces import IWorkingCopy, ICheckinCheckoutPolicy
from plone.app.iterate import PloneMessageFactory as _
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from zExceptions import Redirect
import transaction


def notifyFolderIsAdded(folder, event):
    folder.REQUEST.RESPONSE.redirect(folder.absolute_url() + "/++add++Document") 

def notifyDocumentIsAdded(document, event):
    folder = aq_parent(aq_inner(document))
    if not IWorkingCopy.providedBy(aq_inner(context)):
       folder.setDefaultPage(getattr(document,"id"))

def checkInIfNeeded(document, event):
    context = aq_inner(document)
    workflowTool = getToolByName(context, "portal_workflow")
    status = workflowTool.getStatusOf("1MX_wiki_workflow", document)
    if IWorkingCopy.providedBy(context) and status["review_state"] == "internally_published":
       policy = ICheckinCheckoutPolicy(context)
       baseline = policy.checkin("")
       IStatusMessage(context.REQUEST).addStatusMessage(
            _("Checked in"), type='info')
       view_url = baseline.unrestrictedTraverse("@@plone_context_state").view_url()
       transaction.commit()
       raise Redirect(view_url)
   
