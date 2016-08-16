from Acquisition import aq_inner, aq_parent
from plone import api

def notifyFolderIsAdded(folder, event):
    folder.REQUEST.RESPONSE.redirect(folder.absolute_url() + "/++add++Document") 

def notifyDocumentIsAdded(document, event):
    folder = aq_parent(aq_inner(document))
    folder.setDefaultPage(getattr(document,"id"))
