=======================
Requirements definition
=======================

Scope
*****
We will define what *WinPacMan* must do.

Main goal is to ease the deployment of Open Source application on Windows 
platform.

WinPacMan Client is an application which will be in charge of helping end user
to find/install/uninstall Open Source applications. Informations about available 
applications will be fetch from WinPacMan Repository Server. Informations stored 
onto the Repository will be added/updated by the developer using the Package 
Generator Tool or via the *administration* access on the URL.

The install/uninstall/update/enumerate installations will use scripts that will 
be embedded into the application package. This package can be of several types:

* Contain only scripts and description of the application. Official/Unofficial 
  application setup will be fetch from project's server.
* Contain scripts, description and binary data (setup or only files). These 
  packages will be executable that can be launched even if WinPacMan application 
  is not already installed. In this case, WinPacMan will be installed first to 
  handle package itself.

Technical requirement
*********************

1. The Repository Server
------------------------

It's a RESTful web application where each URL represent a package:

* GET access is public and can return JSON, YAML or HTML formats. GET access 
  will be used by WinPacMan client to get information about the package.
* POST, UPDATE and DELETE access are protected (authentification via OpenID or 
  Google Account). These access are used by the Package Generator Tool 
  to update information about the package.

