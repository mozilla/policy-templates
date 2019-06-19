**IMPORTANT**: This file is in active development along with the policies in Firefox. To get the policy information that corresponds to a specific release, go to https://github.com/mozilla/policy-templates/releases.

Policies can be specified using the Group Policy templates on Windows (https://github.com/mozilla/policy-templates/tree/master/windows), configuration profiles on macOS (https://github.com/mozilla/policy-templates/tree/master/mac), or by creating a file called `policies.json`. On Windows, create a directory called `distribution` where the EXE is located and place the file there. On Mac, the file goes into `Firefox.app/Contents/Resources/distribution`.  On Linux, the file goes into `firefox/distribution`, where `firefox` is the installation directory for firefox, which varies by distribution.

The content of the JSON file should look like this:
```
{
  "policies": {
    ...POLICIES...
  }
}
```
Policies are documented below.   


**Note**: though comments are used in this readme file for documentation, comments are not valid in actual JSON files. Remove all comments before attempting to deploy.

### AppUpdateURL
This policy is for changing the URL used for application update
```
{
  "AppUpdateURL": "http://yoursite.com"
}
```


### Authentication
This policy is for configuring sites that support integrated authentication. See https://developer.mozilla.org/en-US/docs/Mozilla/Integrated_authentication for more information.
```
{
  "policies": {
    "Authentication": {
      "SPNEGO": ["mydomain.com", "https://myotherdomain.com"],
      "Delegated": ["mydomain.com", "https://myotherdomain.com"],
      "NTLM": ["mydomain.com", "https://myotherdomain.com"],
      "AllowNonFQDN": {
        "SPNEGO": true,
        "NTLM": true
      }
    }
  }
}
```
### BlockAboutAddons
A Boolean value that blocks access to about:addons.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAddonsManager`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\BlockAboutAddons` |

#### macOS
```
<dict>
  <key>BlockAboutAddons</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "BlockAboutAddons": true | false
  }
}
```
### BlockAboutConfig
A Boolean value that blocks access to about:config.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAboutConfig`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\BlockAboutConfig` |

#### macOS
```
<dict>
  <key>BlockAboutConfig</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "BlockAboutConfig": true | false
  }
}
```
### BlockAboutProfiles
A Boolean value that blocks access to about:profiles.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAboutProfiles`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\BlockAboutProfiles` |

#### macOS
```
<dict>
  <key>BlockAboutProfiles</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "BlockAboutProfiles": true | false
  }
}
```
### BlockAboutSupport
A Boolean value that blocks access to about:support.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAboutSupport`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\BlockAboutSupport` |

#### macOS
```
<dict>
  <key>BlockAboutSupport</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "BlockAboutSupport": true | false
  }
}
```
### Bookmarks
This policy allows you to specify bookmarks. You can have any number of bookmarks, although only ten are specified in the ADMX file.
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
### CaptivePortal
A Boolean value that enables or disables captive portal support by setting and locking the preference `network.captive-portal-service.enabled`.

**Compatibility:** Firefox 67, Firefox ESR 60.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.captive-portal-service.enabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\CaptivePortal` |

#### macOS
```
<dict>
  <key>CaptivePortal</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "CaptivePortal": true | false
  }
}
```
### Certificates
This policy can be used to install certificates or to read certificates from the system certificate store on Mac and Windows.

The ImportEnterpriseRoots key will cause Firefox to import 3rd party certificates that have been added by a user administrator from the system certificate store.
It does not import all certificates. These certificates will not display in the Firefox certificates manager.

The Install Certificates key by default will search for certificates in the locations listed below. 
Starting in Firefox 65 you can specify a fully qualified path including UNC. (See cert3.der and cert4.pem, in example).

**Be advised if you wish to load a certificate from a UNC path you must use double backslashes.**
Example: \\\\SERVER\\CERTS\\CERT5.PEM


If Firefox does not find something at your fully qualified path, it will search the default directories.

Certificates can be located in the following locations:
- Windows
  - %USERPROFILE%\AppData\Local\Mozilla\Certificates
  - %USERPROFILE%\AppData\Roaming\Mozilla\Certificates
- macOS
  - /Library/Application Support/Mozilla/Certificates
  - ~/Library/Application Support/Mozilla/Certificates
- Linux
  - /usr/lib/mozilla/certificates
  - /usr/lib64/mozilla/certificates
  - ~/.mozilla/certificates


```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": true,
      "Install": ["cert1.der", "cert2.pem", "%SYSTEMDRIVE%\\Company\\cert3.der", "/Library/Company/cert4.pem", "\\\\server\\certs\\cert.pem"]
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
      "RejectTracker": [true|false], /* Only reject trackers */
      "Locked": [true|false] /* If this is true, cookies preferences can't be changed */
    }
  }
}
```
### DNSOverHTTPS
This policy configures DNS over HTTPS.
```
{
  "policies": {
    "DNSOverHTTPS": {
      "Enabled": [true|false],
      "ProviderURL": "URL_TO_ALTERNATE_PROVIDER",
      "Locked": [true|false]
    }
  }
}
```
### DisableSetDesktopBackground
This policy removes the "Set As Desktop Background..." menuitem when right clicking on an image.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeSetDesktopBackground`\
**Preferences Affected:** `devtools.policy.disabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableSetDesktopBackground` |

#### macOS
```
<dict>
  <key>DisableSetDesktopBackground</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableSetDesktopBackground": true | false
  }
}
```
### DisableMasterPasswordCreation
If this policy is set to true, the master password functionality is removed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `noMasterPassword`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableMasterPasswordCreation` |

#### macOS
```
<dict>
  <key>DisableMasterPasswordCreation</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableMasterPasswordCreation": true | false
  }
}
```
### DisableAppUpdate
This policy turns off application updates.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableFirefoxUpdates`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableAppUpdate` |

#### macOS
```
<dict>
  <key>DisableAppUpdate</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableAppUpdate": true | false
  }
}
```
### DisableBuiltinPDFViewer
This policy disables the built in PDF viewer. PDF files are downloaded and sent externally.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePDFjs`\
**Preferences Affected:** `pdfjs.disabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableBuiltinPDFViewer` |

#### macOS
```
<dict>
  <key>DisableBuiltinPDFViewer</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableBuiltinPDFViewer": true | false
  }
}
```
### DisableDeveloperTools
This policy removes access to all developer tools.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeDeveloperTools`\
**Preferences Affected:** `devtools.policy.disabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableDeveloperTools` |

#### macOS
```
<dict>
  <key>DisableDeveloperTools</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableDeveloperTools": true | false
  }
}
```
### DisableFeedbackCommands
This policy disables the menus for reporting sites (Submit Feedback, Report Deceptive Site).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableFeedbackCommands` |

#### macOS
```
<dict>
  <key>DisableFeedbackCommands</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableFeedbackCommands": true | false
  }
}
```
### DisableFirefoxScreenshots
This policy removes access to Firefox Screenshots.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `extensions.screenshots.disabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableFirefoxScreenshots` |

#### macOS
```
<dict>
  <key>DisableFirefoxScreenshots</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableFirefoxScreenshots": true | false
  }
}
```
### DisableFirefoxAccounts
A boolean possibly that disables sync.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableSync`\
**Preferences Affected:** `identity.fxaccounts.enabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableFirefoxAccounts` |

#### macOS
```
<dict>
  <key>DisableFirefoxAccounts</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableFirefoxAccounts": true | false
  }
}
```
### DisableFirefoxStudies
This policy disables Firefox studies (Shield).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableForget`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableFirefoxStudies` |

#### macOS
```
<dict>
  <key>DisableFirefoxStudies</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableFirefoxStudies": true | false
  }
}
```
### DisableForgetButton
This policy turns disables the "Forget" button.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableForget`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableForgetButton` |

#### macOS
```
<dict>
  <key>DisableForgetButton</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableForgetButton": true | false
  }
}
```
### DisableFormHistory
This policy turns off saving information on web forms and the search bar.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableFormFill`\
**Preferences Affected:** ` browser.formfill.enable`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableFormHistory` |

#### macOS
```
<dict>
  <key>DisableFormHistory</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableFormHistory": true | false
  }
}
```
### DisablePocket
This policy removes Pocket in the Firefox UI. It does not remove it from the new tab page.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePocket`\
**Preferences Affected:** `extensions.pocket.enabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisablePocket` |

#### macOS
```
<dict>
  <key>DisablePocket</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisablePocket": true | false
  }
}
```
### DisablePrivateBrowsing
This policy removes access to private browsing.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePrivateBrowsing`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisablePrivateBrowsing` |

#### macOS
```
<dict>
  <key>DisablePrivateBrowsing</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisablePrivateBrowsing": true | false
  }
}
```
### DisableProfileImport
This policy disables the "Import data from another browser" option in the bookmarks window.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableProfileImport` |

#### macOS
```
<dict>
  <key>DisableProfileImport</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableProfileImport": true | false
  }
}
```
### DisableProfileRefresh
This policy disables the Refresh Firefox button on about:support and support.mozilla.org, as well as the prompt that displays offering to refresh Firefox when you haven't used it in a while.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableResetFirefox`\
**Preferences Affected:** `browser.disableResetPrompt`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableProfileRefresh` |

#### macOS
```
<dict>
  <key>DisableProfileRefresh</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableProfileRefresh": true | false
  }
}
```
### DisableSafeMode
This boolean value disables safe mode.

**Compatibility:** Firefox 60, Firefox ESR 60 (Windows, macOS)\
**CCK2 Equivalent:** `disableSafeMode`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableSafeMode` |

#### macOS
```
<dict>
  <key>DisableSafeMode</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableSafeMode": true | false
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
### DisableSystemAddonUpdate
This boolean value prevents system add-ons from being updated or installed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableSystemAddonUpdate` |

#### macOS
```
<dict>
  <key>DisableSystemAddonUpdate</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableSystemAddonUpdate": true | false
  }
}
```
### DisableTelemetry
This boolean value prevents the upload of telemetry data.

Mozilla recommends that you do not disable telemetry. Information collected through telemetry helps us build a better product for businesses like yours.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableTelemetry`\
**Preferences Affected:** `datareporting.healthreport.uploadEnabled,datareporting.policy.dataSubmissionEnabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisableTelemetry` |

#### macOS
```
<dict>
  <key>DisableTelemetry</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableTelemetry": true | false
  }
}
```
### DisplayBookmarksToolbar
This boolean value turns on the bookmarks toolbar by default. A user can still turn it off, and it will stay off.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `displayBookmarksToolbar`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisplayBookmarksToolbar` |

#### macOS
```
<dict>
  <key>DisplayBookmarksToolbar</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisplayBookmarksToolbar": true | false
  }
}
```
### DontCheckDefaultBrowser
This boolean value turns on the menubar by default. A user can still turn it off, and it will stay off.

**Compatibility:** Firefox 60, Firefox ESR 60 (Windows, some Linux)\
**CCK2 Equivalent:** `displayMenuBar`\
**Preferences Affected:** N/~

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DisplayMenuBar` |

#### macOS
```
<dict>
  <key>DisplayMenuBar</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisplayMenuBar": true | false
  }
}
```
### DontCheckDefaultBrowser
This boolean value stops Firefox from checking if it is the default browser at startup.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontCheckDefaultBrowser`\
**Preferences Affected:** `browser.shell.checkDefaultBrowser`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\DontCheckDefaultBrowser` |

#### macOS
```
<dict>
  <key>DontCheckDefaultBrowser</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "DontCheckDefaultBrowser": true | false
  }
}
```
### EnableTrackingProtection
This policy affects tracking protection.

If this policy is not configured, tracking protection is not enabled by default in the browser, but it is enabled by default in private browsing and the user can change it.

If Value is set to false, tracking protection is disabled and locked in both the regular browser and private browsing.

If Value is set to true, tracking protection is enabled by default in both the regular browser and private browsing.

You can choose to set the Locked value if you want to prevent the user from changing it.
```
{
  "policies": {
    "EnableTrackingProtection": {
      "Value": [true, false],
      "Locked": [true, false]
    }
}
```
### Extensions
This policy controls the installation, uninstallation and locking of extensions. Locked extensions cannot be disabled or uninstalled.
For Install, you specify a list of URLs or paths.
For Uninstall and Locked, you specify extension IDs.
```
{
  "policies": {
    "Extensions": {
      "Install": ["https://addons.mozilla.org/firefox/downloads/somefile.xpi", "//path/to/xpi"],
      "Uninstall": ["addon_id@mozilla.org"],
      "Locked":  ["addon_id@mozilla.org"]
    }
  }
}
```
### ExtensionUpdate
This boolean value determines extension update are enabled.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `extensions.update.enabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\ExtensionUpdate` |

#### macOS
```
<dict>
  <key>ExtensionUpdate</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "ExtensionUpdate": true | false
  }
}
```
### HardwareAcceleration
This boolean value determines if hardware acceleration is enabled.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `layers.acceleration.disabled`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\HardwareAcceleration` |

#### macOS
```
<dict>
  <key>HardwareAcceleration</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "HardwareAcceleration": true | false
  }
}
```
### NoDefaultBookmarks
A Boolean value that prevents the default bookmarks and Smart Bookmarks (Most Visited, Recent Tags) from being created. Note: this policy is only effective if used before the first run of the profile. Also, the smart bookmarks were removed in Firefox 63.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeDefaultBookmarks`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\NoDefaultBookmarks` |

#### macOS
```
<dict>
  <key>NoDefaultBookmarks</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "NoDefaultBookmarks": true | false
  }
}
```
### OfferToSaveLogins
This boolean value determines whether or not Firefox offers to save passwords.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontRememberPasswords`\
**Preferences Affected:** `signon.rememberSignons`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\OfferToSaveLogins` |

#### macOS
```
<dict>
  <key>OfferToSaveLogins</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "OfferToSaveLogins": true | false
  }
}
```
### Homepage
This policy sets the default homepage value and the default start page.  It can also be used to lock the homepage or add additional homepages.
```
{
  "policies": {
    "Homepage": {
      "URL": "http://example.com/",
      "Locked": true,
      "Additional": ["http://example.org/",
                     "http://example.edu/"],
      "StartPage": ["none", "homepage", "previous-session"]
    }
  }
}
```
### PopupBlocking
This policy sets domains for which pop-up windows are allowed. It also sets the default pop-up policy.
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
      "Default": [true|false], /* If this is set to true, Flash is always enabled. If it is set to false, Flash is never enabled */
      "Locked": [true|false]
    }
  }
}
```
### NetworkPrediction
This policy enables or disables network prediction (DNS prefetching) by setting and locking the preferences `network.dns.disablePrefetch` and `network.dns.disablePrefetchFromHTTPS`.
```
{
  "policies": {
    "NetworkPrediction": [true|false]
}
```
### OverrideFirstRunPage
This policy allows you to override the first run page. If you leave the URL blank, the first run page will not be displayed.
```
{
  "policies": {
    "OverrideFirstRunPage": "http://example.org"
  }
}
```
### OverridePostUpdatePage
This policy allows you to override the upgrade page. If you leave the URL blank, the upgrade page will not be displayed.
```
{
  "policies": {
    "OverridePostUpdatePage": "http://example.org"
  }
}
```
### Permissions
This policy allows you to change the permissions associated with camera, microphone, location, and notifications
```
{
  "policies": {
    "Permissions": {
      "Camera": {
        "Allow": ["http://example.org/"], /* Origins where camera access is allowed by default */
        "Block": ["http://example.org/"], /* Origins where camera access is blocked by default */
        "BlockNewRequests": [true|false], /* Block new requests to access the camera */
        "Locked": [true|false] /* Don't allow the user to change the camera preferences */
      },
      "Microphone": {
        "Allow": ["http://example.org/"], /* Origins where microphone access is allowed by default */
        "Block": ["http://example.org/"], /* Origins where microphone access  is blocked by default */
        "BlockNewRequests": [true|false], /* Block new requests to access the microphone */
        "Locked": [true|false] /* Don't allow the user to change the microphone preferences */
      },
      "Location": {
        "Allow": ["http://example.org/"], /* Origins where location access is allowed by default */
        "Block": ["http://example.org/"], /* Origins where location access is blocked by default */
        "BlockNewRequests": [true|false], /* Block new requests to access location */
        "Locked": [true|false] /* Don't allow the user to change the location preferences */
      },
      "Notifications": {
        "Allow": ["http://example.org/"], /* Origins where sending notifications is allowed by default */
        "Block": ["http://example.org/"], /* Origins where sending notifications is blocked by default */
        "BlockNewRequests": [true|false], /* Block new requests to send notifications */
        "Locked": [true|false] /* Don't allow the user to change the notification preferences */
      }
    }
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
**Compatibility:** Firefox ESR 60\
**CCK2 Equivalent:** `networkProxy*`\
**Preferences Affected:** N/A

### Keys
| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `Mode` | String | _required_ | The name of the search engine. |
| `Locked` | Boolean | _required_ | Search URL with {searchTerms} to substitute for the search term. |
| `HTTPProxy` | String | GET | GET or POST |
| `UseHTTPProxyForAllProtocols` | Boolean | — | URL for the icon to use. |
| `SSLProxy` | String | — | Keyword to use for the engine. |
| `FTPProxy` | String | —| Description of the search engine. |
| `SOCKSProxy` | String | — | Search suggestions URL with {searchTerms} to substitute for the search term. |
| `SOCKSVersion` | String | — | Search suggestions URL with {searchTerms} to substitute for the search term. |
| `Passthrough` | String | — | Search suggestions URL with {searchTerms} to substitute for the search term. |
| `AutoConfigURL` | String | — | Search suggestions URL with {searchTerms} to substitute for the search term. |
| `AutoLogin` | Boolean | — | Search suggestions URL with {searchTerms} to substitute for the search term. |
| `UseProxyForDNS` | Boolean | — | Search suggestions URL with {searchTerms} to substitute for the search term. |

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\Mode` |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\Locked` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\HTTPProxy` |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\UseHTTPProxyForAllProtocols` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\SSLProxy` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\FTPProxy` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\SOCKSProxy` |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\SOCKSVersion` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\Passthrough` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\AutoConfigURL` |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\AutoLogin` |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\SearchEngines\Proxy\UseProxyForDNS` |

#### macOS
```
<dict>
  <key>Search</key>
  <dict>
    <key>Proxy</key>
    <array>
      <dict>
        <key>Mode</key>
        <string>none | system | manual | autoDetect| autoConfig</string>
        <key>Locked</key>
        <true> | </false>
        <key>HTTPProxy</key>
        <string>https://httpproxy.example.com</string>
        <key>UseHTTPProxyForAllProtocols</key>
        <true> | </false>
        <key>SSLProxy</key>
        <string>https://sslproxy.example.com</string>
        <key>FTPProxy</key>
        <string>https://ftpproxy.example.com</string>
        <key>SOCKSProxy</key>
        <string>https://socksproxy.example.com</string>
      </dict>
    <array>
  </dict>
</dict>
```
### JSON
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
      ]
    }
  }
}
```
### RequestedLocales
This policy sets the list of requested locales for the application in order of preference. It will cause the corresponding language pack to become active.
```
{
  "policies": {
    "RequestedLocales": ["de", "en-US"]
  }
}
```
### SanitizeOnShutdown
A boolean value that tells Firefox to clear all data on shutdown, including Browsing & Download History, Cookies, Active Logins, Cache, Form & Search History, Site Preferences and Offline Website Data.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown,privacy.clearOnShutdown.cache,privacy.clearOnShutdown.cookies,privacy.clearOnShutdown.downloads,privacy.clearOnShutdown.formdata,privacy.clearOnShutdown.history,privacy.clearOnShutdown.sessions,privacy.clearOnShutdown.siteSettings,privacy.clearOnShutdown.offlineApps`
#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_DWORD` | `Software\Policies\Mozilla\Firefox\SanitizeOnShutdown` |

#### macOS
```
<dict>
  <key>SanitizeOnShutdown</key>
  <true/> | <false/>
</dict>
```

#### JSON
```
{
  "policies": {
    "SanitizeOnShutdown": true | false
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
### SearchBar
A String value that sets whether or not the search bar is displayed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `showSearchBar`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchBar` |

#### macOS
```
<dict>
  <key>SearchBar</key>
  <string>unified | separate</string>
</dict>
```

#### JSON
```
{
  "policies": {
    "SearchBar": "unified" | "separate"
  }
}
```
### WebsiteFilter
This policy blocks websites from being visited. The parameters take an array of Match Patterns, as documented in https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Match_patterns. Only http/https addresses are supported at the moment. The arrays are limited to 1000 entries each.
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
### Search Engines (This policy is only available on the ESR.)
This policy allows you to add new search engines, remove or hide search engines, as well as set the default and prevent the install of search engines from web pages. Only Name and URLTemplate is required.
```
{
  "policies": {
    "SearchEngines": {
      "Default": "Name of engine",
      "PreventInstalls": [true|false],
      "Remove": ["Twitter", "Wikipedia (en)"]
    }
  }
}
```
### Search Engines

### Search Engines | Add

This policy allows you to add up to five new search engines. This policy is only available on the ESR.

**Compatibility:** Firefox ESR 60\
**CCK2 Equivalent:** `config.searchplugins`\
**Preferences Affected:** N/A

### Keys
| Key | Type | Default | Description |
| --- | ---- | ------- | ----------- |
| `Name` | String | _required_ | The name of the search engine. |
| `URLTemplate` | String | _required_ | Search URL with {searchTerms} to substitute for the search term. |
| `Method` | String | GET | GET or POST |
| `IconURL` | String | — | URL for the icon to use. |
| `Alias` | String | — | Keyword to use for the engine. |
| `Description` | String | —| Description of the search engine. |
| `SuggestURLTemplate` | String | — | Search suggestions URL with {searchTerms} to substitute for the search term. |

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Name` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\URLTemplate` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Method` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\IconURL` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Alias` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Description` |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\SuggestURLTemplate` |

#### macOS
```
<dict>
  <key>Search</key>
  <dict>
    <key>Add</key>
    <array>
      <dict>
        <key>Name</key>
        <string>Example1</string>
        <key>URLTemplate</key>
        <string>https://www.example.org</string>
        <key>Method</key>
        <string>https://www.example.org/favicon.ico</string>
        <key>IconURL</key>
        <string>toolbar</string>
        <key>Alias</key>
        <string>Example1Folder</string>
        <key>Description</key>
        <string>Example1Folder</string>
        <key>Alias</key>
        <string>SuggestURLTemplate</string>
      </dict>
    <array>
  </dict>
</dict>
```
### JSON
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
      ]
    }
  }
}
```
### SecurityDevices
A dictionary with the names and locations of PKCS #11 modules to be installed.

**Compatibility:** Firefox 64, Firefox ESR 60.4\
**CCK2 Equivalent:** `certs.devices`\
**Preferences Affected:** N/A

#### Windows
| Type | Registry Location | Registry Value |
| ---- | ----------------- | -------------- |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SecurityDevices\NAME_OF_DEVICE` | `PATH_TO_LIBRARY_FOR_DEVICE`

#### macOS
```
<dict>
  <key>SecurityDevices</key>
  <dict>
    <key>NAME_OF_DEVICE</key>
    <string>PATH_TO_LIBRARY_FOR_DEVICE</string>
  </dict>
</dict>
```

#### JSON
```
{
  "policies": {
    "SecurityDevices": {
      "NAME_OF_DEVICE": "PATH_TO_LIBRARY_FOR_DEVICE"
    }
  }
}
```
### SSLVersionMax
A String value that sets and locks the maximum version of TLS

**Compatibility:** Firefox 66, Firefox ESR 60.6\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.tls.version.max`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SSLVersionMax` |

#### macOS
```
<dict>
  <key>SSLVersionMax</key>
  <string>tls1 | tls1.1 | tls1.2 | tls1.3</string>
</dict>
```

#### JSON
```
{
  "policies": {
    "SSLVersionMax": "tls1" | "tls1.1" | "tls1.2" | "tls1.3"
  }
}
```
### SSLVersionMin
A String value that sets and locks the minimum version of TLS

**Compatibility:** Firefox 66, Firefox ESR 60.6\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.tls.version.min`

#### Windows
| Type | Registry Location |
| ---- | ----------------- |
| `Windows:REG_SZ` | `Software\Policies\Mozilla\Firefox\SSLVersionMin` |

#### macOS
```
<dict>
  <key>SSLVersionMin</key>
  <string>tls1 | tls1.1 | tls1.2 | tls1.3</string>
</dict>
```

#### JSON
```
{
  "policies": {
    "SSLVersionMin": "tls1" | "tls1.1" | "tls1.2" | "tls1.3"
  }
}
```
