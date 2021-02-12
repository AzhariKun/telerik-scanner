# -*- coding: utf-8 -*-
#!usr/bin/python
import os, sys, requests
from multiprocessing import Pool 
from multiprocessing.dummy import Pool as ThreadPool

Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
####################### 
#  Coded By KimiHmei7 #
#######################
def telerik(url):
  if '://' in url:
    pass
  else:
    url = 'http://' + url
  try:
    pathz = ['/DesktopModules/RadEditorProvider/DialogHandler.aspx', '/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx', '/serverside/telerik.web.ui.dialoghandler.aspx', '/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx', '/DesktopModules/Admin/RadEditorProvider/telerik.web.ui.dialoghandler.aspx', '/DesktopModules/TNComments/Telerik.Web.UI.DialogHandler.aspx', '/Resources/Telerik.Web.UI.DialogHandler.aspx', '/DesktopModule/UIQuestionControls/UIAskQuestion/Telerik.Web.UI.DialogHandler.aspx', '/Telerik.Web.UI.DialogHandler.aspx', '/feedback/Telerik.Web.UI.DialogHandler.aspx', '/SiteTemplates/Telerik.Web.UI.DialogHandler.aspx', '/app_master/telerik.web.ui.dialoghandler.aspx', '/modules/shop/manage/telerik.web.ui.dialoghandler.aspx', '/Sitefinity/ControlTemplates/Blogs/Telerik.Web.UI.DialogHandler.aspx', '/dashboard/UserControl/CMS/Page/Telerik.Web.UI.DialogHandler.aspx', '/AsiCommon/Controls/ContentManagement/ContentDesigner/Telerik.Web.UI.DialogHandler.aspx', '/WebUIDialogs/Telerik.Web.UI.DialogHandler.aspx', '/dotnetnuke/DesktopModules/Admin/RadEditorProvider/DialogHandler.aspx', '/static/usercontrols/Telerik.Web.UI.DialogHandler.aspx', '/overview/Telerik.Web.UI.DialogHandler.aspx', '/system/providers/htmleditor/Telerik.Web.UI.DialogHandler.aspx', '/cms/portlets/telerik.web.ui.dialoghandler.aspx', '/desktopmodules/base/editcontrols/telerik.web.ui.dialoghandler.aspx', '/desktopmodules/tcmodules/tccategory/telerik.web.ui.dialoghandler.aspx', '/portal/channels/fa/Cms_HtmlText_Manage/Telerik.Web.UI.DialogHandler.aspx', '/sitecore/shell/Controls/RichTextEditor/Telerik.Web.UI.DialogHandler.aspx', '/sitecore/shell/applications/contentmanager/telerik.web.ui.dialoghandler.aspx']
    for path in pathz:
      cekvuln = requests.get(url + path, headers=Headers, timeout=15)
      if 'Loading the dialog...' in str(cekvuln.content):
        print "\x1b[32m[*]\x1b[0m \x1b[41m" + url + path + "\x1b[0m"
        open('Results/telerik_vuln.txt', 'a').write(url + path +'\n')
        break
      else:
        print "\x1b[32m[*]\x1b[0m " + "\x1b[36m" + url + path + "\x1b[0m"
  except:
    pass
  
banner = """\x1b[1;31m _____    _           _ _      _   _ _____ 
|_   _|  | |         (_) |    | | | |_   _|
  | | ___| | ___ _ __ _| | __ | | | | | |  
  | |/ _ \ |/ _ \ '__| | |/ / | | | | | |  
  | |  __/ |  __/ |  | |   <  | |_| |_| |_ 
  \_/\___|_|\___|_|  |_|_|\_\  \___/ \___/\x1b[0m
\t \x1b[33m -[Coded By KimiHmei7]- \x1b[0m
╔══════════════════════════════════════════
╚═[\x1b[41mMASS TELERIK FINDER\x1b[0m]
"""
print(banner)
url = open(raw_input('[input list:~# '),'r').read().split()
Thread = raw_input('[Threads :~# ')
pool = ThreadPool(int(Thread))
pool.map(telerik, url)
pool.close()
pool.join()