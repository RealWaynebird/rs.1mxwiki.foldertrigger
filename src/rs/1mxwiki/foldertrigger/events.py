def notifyFolderIsAdded(folder, event):
    folder.REQUEST.RESPONSE.redirect(folder.absolute_url() + "/++add++Document") 

def notifyDocumentIsAdded(document, event):
    folder = aq_parent(document)
    folder.setDefaultPage(document) 
