Policies can either be specified using the Group Policy templates or by creating a file called policies.json. On Windows, create a directory called distribution where the EXE is located and place the file there. On Mac, the file goes into Firefox.app/Content/Resources/distribution.

The content of the JSON file should look like this:
```
{
  "policies": {
    ...POLICIES...
  }
}
```
Policies are documented below. Note that even though comments are used in this file for documentation, comments are not allowed for JSON files.
### Authentication
This policy is for configuring sites that support integrated authentication. See https://developer.mozilla.org/en-US/docs/Mozilla/Integrated_authentication for more information.
```
{
  "policies": {
    "Authentication": {
      "SPNEGO": ["mydomain.com", "https://myotherdomain.com"],
      "Delegated": ["mydomain.com", "https://myotherdomain.com"],
      "NTLM": ["mydomain.com", "https://myotherdomain.com"]
    }
  }
}
```
### BlockAboutAddons
This policy removes access to about:addons.
```
{
  "policies": {
    "BlockAboutAddons": true
  }
}
```
### BlockAboutConfig
This policy removes access to about:config.
```
{
  "policies": {
    "BlockAboutConfig": true
  }
}
```
### BlockAboutProfiles
This policy removes access to about:profiles.
```
{
  "policies": {
    "BlockAboutProfiles": true
  }
}
```
### BlockAboutSupport
This policy removes access to about:support.
```
{
  "policies": {
    "BlockAboutSupport": true
}
```
### BlockSetDesktopBackground
This policy removes the "Set As Desktop Background..." menuitem when right clicking on an image.
```
{
  "policies": {
    "BlockAboutSupport": true
  }
}
```
### Certificates
This is a Windows only policy that tells Firefox to read certificates from the Windows certificate store.
```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": [true|false]
    }
  }
}
```
### Cookies
This policy controls various settings related to cookies.
```
{
  "policies": {
    "Cookies": {
      "Allow": ["http://example.org/"], /* Domains where cookies are always allowed */
      "Block": ["http://example.edu/"], /* Domains where cookies are always blocked */
      "Default": [true|false], /* This sets the default value for "Accept cookies from websites" */
      "AcceptThirdParty": ["all", "none", "from-visited"], /* This sets the default value for "Accept third-party cookies" */
      "ExpireAtSessionEnd":  [true|false], /* This determines when cookies expire */
      "Locked": [true|false] /* If this is true, cookies preferences can't be changed */
    }
  }
}
```
### CreateMasterPassword
This policy removes the master password functionality.
```
{
  "policies": {
    "CreateMasterPassword": false
  }
}
```
### DisableAppUpdate
This policy turns off application updates.
```
{
  "policies": {
    "DisableAppUpdate": true
  }
}
```
### DisableBuiltinPDFViewer
This policy disables the built in PDF viewer. PDF files are downloaded and sent externally.
```
{
  "policies": {
    "DisableBuiltinPDFViewer": true
  }
}
```
### DisableDeveloperTools
This policy removes access to all developer tools.
```
{
  "policies": {
    "DisableDeveloperTools": true
  }
}
```
### DisableFeedbackCommands
This policy disables the menus for reporting sites (Submit Feedback, Report Deceptive Site)
```
{
  "policies": {
    "DisableFeedbackCommands": true
  }
}
```
### DisableFirefoxScreenshots
This policy removes access to Firefox Screenshots
```
{
  "policies": {
    "DisableFirefoxScreenshots": true
  }
}
```
### DisableFirefoxAccounts
This policy disables Sync
```
{
  "policies": {
    "DisableFirefoxAccounts": true
  }
}
```
### DisableFirefoxStudies
This policy disables Firefox studies (Shield)
```
{
  "policies": {
    "DisableFirefoxAccounts": true
  }
}
```
### DisableForgetButton
This policy disables the "Forget" button
```
{
  "policies": {
    "DisableForgetButton": true
  }
}
```
### DisableFormHistory
This policy turns off the browser.formfill.enable preferences
```
{
  "policies": {
    "DisableFormHistory": true
  }
}
```
### DisablePocket
This policy turns off Pocket
```
{
  "policies": {
    "DisablePocket": true
  }
}
```
### DisablePrivateBrowsing
This policy removes access to private browsing
```
{
  "policies": {
    "DisablePrivateBrowsing": true
  }
}
```
### DisableProfileRefresh
This policy disables the Refresh Firefox button on about:support and support.mozilla.org.
```
{
  "policies": {
    "DisableProfileRefresh": true
  }
}
```
### DisableSafeMode
This policy disables safe mode on Windows only
```
{
  "policies": {
    "DisableSafeMode": true
  }
}
```
### DisableSecurityBypass
This policy prevents the user from bypassign security in certain cases.
```
{
  "policies": {
    "DisableSecurityBypass": {
      "InvalidCertificate": [true|false], /* Prevents adding an exception when an invalid certificate is shown */
      "SafeBrowsing": [true|false]        /* Prevents selecting "ignore the risk" and visiting a harmful site anyway */
    }
  }
}
```
### DisableSysAddonUpdate
This policy prevents system add-ons from being updated or installed.
```
{
  "policies": {
    "DisableSysAddonUpdate": true
  }
}
```
### DisableTelemetry
This policy prevents the upload of telemetry data. Mozilla strongly recommends that you do NOT disable telemetry if you do not have a business need to do so.
```
{
  "policies": {
    "DisableTelemetry": true
  }
}
```
### DisplayBookmarksToolbar
This policy turns on the bookmarks toolbar by default. A user can still turn it off and it will stay off.
```
{
  "policies": {
    "DisplayBookmarksToolbar": true
  }
}
```
### DisplayMenuBar
This policy turns on the menubar by default. A user can still turn it off and it will stay off.
```
{
  "policies": {
    "DisplayMenuBar": true
  }
}
```
### DontCheckDefaultBrowser
This policy stops Firefox from checking if it is the default browser at startup.
```
{
  "policies": {
    "DontCheckDefaultBrowser": true
  }
}
```
### EnableTrackingProtection
This policy affects tracking protection.

If this policy is not configured, tracking protection is not enabled by default in the browser but it is enabled by default in private browsing and the user can change it.

If Value is set to false, tracking protection is disabled and locked in both the browser and private browsing.

If Value is set to true, private browsing is enabled by default in both the browser and private browsing and you can choose set the Locked value if you want to prevent the user from changing it.
```
{
  "policies": {
    "EnableTrackingProtection": {
      "Value": [true, false],
      "Locked": [true, false]
    }
```
### Extensions
This policy controls the install, uninstall and locking of extensions. Locked extensions cannot be disabled or uninstalled.
For Install, you can specify a list of URLs or paths.
For Uninstall and Locked, you specify extension IDs.
```
{
  "policies": {
    "Extensions": {
      "Install": ["https://addons.mozilla.org/firefox/downloads/somefile.xpi", "//path/to/xpi"]
      "Uninstall": ["addon_id@mozilla.org"],
      "Locked":  ["addon_id@mozilla.org"]
    }
```
### NoDefaultBookmarks
Don't create the default bookmarks or the Smart Bookmarks (Most Visited, Recent Tags). Note: this policy is only effective if used before the first run of the profile.
```
{
  "policies": {
    "NoDefaultBookmarks": true
  }
}
```
### RememberPasswords
This policy sets the signon.rememberSignons preference. It can either be enabled or disabled.
```
{
  "policies": {
    "RememberPasswords": true
  }
}
```
### Homepage
This policy sets the default homepage value. It can also be used to lock the homepage and add additional homepages.
```
{
  "policies": {
    "Homepage": {
      "URL": "http://example.com/",
      "Locked": true,
      "Additional": ["http://example.org/",
                     "http://example.edu/"]
    }
  }
}
```
### Popups
This policy sets domains for which popups are allowed
```
{
  "policies": {
    "Popups": {
      "Allow": ["http://example.org/",
                "http://example.edu/"]
    }
  }
}
```
### InstallAddons
This policy sets domains that can install extensions, as well as the default behavior.
```
{
  "policies": {
    "InstallAddons": {
      "Allow": ["http://example.org/",
                "http://example.edu/"]
      "Default": [true|false], /* If this is set to false, add-ons cannot be installed by the user */
    }
  }
}
```
### FlashPlugin
This policy sets the behavior of Flash on the specified domains, as well as the default behavior.
```
{
  "policies": {
    "FlashPlugin": {
      "Allow": ["http://example.org/"], /* Sites on the allow list do not override Flash being completely disabled */
      "Block": ["http://example.edu/"],
      "Default": [true|false], /* If this is set to true, flash is always enabled. If it is set to false, Flash is never enabled */
      "Locked": [true|false]
    }
  }
}
```
### Bookmarks
This policy allows you to specify bookmarks. You can have any number of bookmarks although only ten are specified in the ADMX file.
Placement can be specified as either toolbar or menu. If a folder is specified, it is automatically created and bookmarks with the
same folder name are grouped together.

```
{
  "policies": {
    "Bookmarks": [
    {"Title": "Example",
     "URL": "http://example.org",
     "Favicon": "http://example.com/favicon.ico",
     "Placement": ["toolbar", "menu"],
     "Folder": "FolderName"
     }
    ]
  }
}
```
### Proxy
This policy allows you to specify proxy settings. These settings correspond to the connection settings in Firefox preferences.
To specify ports, append them to the hostnames with a colon (:). If Locked is set to true, the values can't be changed by the user.
```
{
  "Proxy": {
    "Mode": ["none", "system", "manual", "autoDetect", "autoConfig"]
    "Locked": [true, false]
    "HTTPProxy": "hostname",
    "UseHTTPProxyForAllProtocols": [true, false]
    "SSLProxy": "hostname",
    "FTPProxy": "hostname",
    "SOCKSProxy": "hostname",
    "SOCKSVersion": [4, 5],
    "Passthrough": "List of passthrough addresses/domains",
    "AutoConfigURL": "URL_TO_AUTOCONFIG",
    "AutoLogin":  [true, false],
    "UseProxyForDNS": [true, false]
  }
}
```
