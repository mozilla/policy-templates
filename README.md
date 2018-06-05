Policies can either be specified using the Group Policy templates or by creating a file called policies.json. On Windows, create a directory called distribution where the EXE is located and place the file there. On Mac, the file goes into `Firefox.app/Contents/Resources/distribution`.  On Linux, the file goes into `firefox/distribution`, where `firefox` is the installation directory for firefox, which varies by distribution.

The content of the JSON file should look like this:
```
{
  "policies": {
    ...POLICIES...
  }
}
```
Policies are documented below. **Note**: though comments are used in this readme file for documentation, comments are not valid in actual JSON files. Remove all comments before attempting to deploy.

Some of the policies are only available on the ESR for security reasons. These policies are marked ESR only.

### Authentication (ESR only)
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
### DisableSetDesktopBackground
This policy removes the "Set As Desktop Background..." menuitem when right clicking on an image.
```
{
  "policies": {
    "DisableSetDesktopBackground": true
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
      "AcceptThirdParty": ["always", "never", "from-visited"], /* This sets the default value for "Accept third-party cookies" */
      "ExpireAtSessionEnd":  [true|false], /* This determines when cookies expire */
      "Locked": [true|false] /* If this is true, cookies preferences can't be changed */
    }
  }
}
```
### DisableMasterPasswordCreation
This policy removes the master password functionality if set to true.
```
{
  "policies": {
    "DisableMasterPasswordCreation": [true|false]
  }
}
```
### DisableAppUpdate (ESR only)
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
    "DisableFirefoxStudies": true
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
### DisableProfileImport
This policy disables the"Import data from another browser" option in the bookmarks window.
```
{
  "policies": {
    "DisableProfileImport": true
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
This policy prevents the user from bypassing security in certain cases.
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
### DisableSystemAddonUpdate (ESR only)
This policy prevents system add-ons from being updated or installed.
```
{
  "policies": {
    "DisableSystemAddonUpdate": true
  }
}
```
### DisableTelemetry (ESR only)
This policy prevents the upload of telemetry data.

Mozilla recommends that you do not disable telemetry. Information collected through telemetry helps us build a better product for businesses like yours.
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
}
```
### Extensions (ESR only)
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
### OfferToSaveLogins
This policy sets the signon.rememberSignons preference. It determines whether or not Firefox offers to save passwords. It can either be enabled or disabled.
```
{
  "policies": {
    "OfferToSaveLogins": true
  }
}
```
### Homepage (ESR only)
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
### PopupBlocking
This policy sets domains for which pop-up windows are allowed. It also set the default pop-up policy
```
{
  "policies": {
    "PopupBlocking": {
      "Allow": ["http://example.org/",
                "http://example.edu/"],
      "Default": [true|false], /* If this is set to false, pop-up window are enabled by default. */
      "Locked": [true|false]
    }
  }
}
```
### InstallAddonsPermission
This policy sets domains that can install extensions, as well as the default behavior.
```
{
  "policies": {
    "InstallAddonsPermission": {
      "Allow": ["http://example.org/",
                "http://example.edu/"],
      "Default": [true|false] /* If this is set to false, add-ons cannot be installed by the user */
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
### OverrideFirstRunPage (ESR only)
This policy allowed you to override the first run page. If you leave the URL blank, the first run page will not be displayed.
```
{
  "policies": {
    "OverrideFirstRunPage": "http://example.org"
  }
}
```
### OverridePostUpdatePage (ESR only)
This policy allowed you to override the upgrade page page. If you leave the URL blank, the upgrade page will not be displayed.
```
{
  "policies": {
    "OverridePostUpdatePage": "http://example.org"
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
      {
        "Title": "Example",
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
  "policies": {
    "Proxy": {
      "Mode": ["none", "system", "manual", "autoDetect", "autoConfig"],
      "Locked": [true, false],
      "HTTPProxy": "hostname",
      "UseHTTPProxyForAllProtocols": [true, false],
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
}
```
### SanitizeOnShutdown
If this policy is set to true,  all data is cleared when Firefox is closed. This includes Browsing & Download History, Cookies, Active Logins, Cache, Form & Search History, Site Preferences and Offline Website Data.
```
{
  "policies": {
    "SanitizeOnShutdown": [true|false]
  }
}
```
### SearchBar (ESR only)
This policy can be used to determine if the search bar is separate or combined with the URL bar.
```
{
  "policies": {
    "SearchBar": ["unified", "separate"]
  }
}
```
### WebsiteFilter (ESR only)
Blocks websites from being visited. The parameters take an array of Match Patterns, as documented in https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Match_patterns. Only http/https accesses are supported at the moment. The arrays are limited to 1000 entries each.
```
{
  "policies": {
    "WebsiteFilter": {
      "Block": ["<all_urls>"],
      "Exceptions": ["http://example.org/*"]
    }
  }
}
```
### Search Engines (ESR only)
This policy allows you to add new search engines, as well as set the default and prevent the install of search engines from web pages. Only Name and URLTemplate is required.
```
{
  "policies": {
    "SearchEngines": {
      "Add": [
        {
          "Name": "",
          "URLTemplate": "URL including {searchTerms} to substitute for the terms",
          "Method": ["GET", "POST"],
          "IconURL": "URL to icon",
          "Alias": "Alias that can be used to access the engine",
          "Description": "Description",
          "SuggestURLTemplate": "URL for suggestions using {searchTerms}"
        }
      ],
      "Default": "Name of engine",
      "PreventInstalls": [true|false]
    }
  }
}
```
