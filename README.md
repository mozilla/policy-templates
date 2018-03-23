Policies can either be specified using the GPO templates or by putting a file called policies.json in the distribution directory.
The content of the JSON file should look like this:
```
{
  "policies": {
    ...POLICIES...
  }
}
```
Policies are documented below.

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
### DisableSafeMode
This policy disables safe mode on Windows only
```
{
  "policies": {
    "DisableSafeMode": true
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
This policy sets domains that can install extensions
```
{
  "policies": {
    "InstallAddons": {
      "Allow": ["http://example.org/",
                "http://example.edu/"]
    }
  }
}
```
### Cookies
This policy sets domains that can set or not set cookies.
```
{
  "policies": {
    "Cookies": {
      "Allow": ["http://example.org/"],
      "Block": ["http://example.edu/"]
    }
  }
}
```
### FlashPlugin
This policy sets domains that can use or not use Flash
```
{
  "policies": {
    "FlashPlugin": {
      "Allow": ["http://example.org/"],
      "Block": ["http://example.edu/"]
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
