#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
from ezodf import newdoc
import os
import zipfile
import tempfile
import xlrd
from dates import dates

def updateZip(zipname, filename, data):
    # generate a temp file
    tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
    os.close(tmpfd)

    # create a temp copy of the archive without filename
    with zipfile.ZipFile(zipname, 'r') as zin:
        with zipfile.ZipFile(tmpname, 'w') as zout:
            zout.comment = zin.comment # preserve the comment
            for item in zin.infolist():
                if item.filename != filename:
                    zout.writestr(item, zin.read(item.filename))

    # replace with the temp archive
    os.remove(zipname)
    os.rename(tmpname, zipname)

    # now add filename with its new data
    with zipfile.ZipFile(zipname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(filename, data)

def speaker(name, org):
    filen = './invitation/invitacion_ponencia.odt'
    name = name
    org = org
    ds = dates()
    docx = newdoc(doctype='odt', filename=filen, template='./format/invitation.odt')
    docx.save()
    a = zipfile.ZipFile('./format/invitation.odt')
    content = a.read('content.xml')
    content = str(content.decode(encoding='utf8'))
    content = str.replace(content,"Nombre", name)
    content = str.replace(content,"Organización", org)
    content = str.replace(content,"Fecha1", ds[0])
    content = str.replace(content,"Fecha2", ds[1])
    content = str.replace(content,"Fecha3", ds[2])
    content = str.replace(content,"Fecha4", ds[3])
    updateZip(filen, 'content.xml', content)
    cm = "unoconv -f pdf " + filen
    os.system(cm)
