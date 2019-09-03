**These policies are in active development and so might contain changes that do not work with current versions of Firefox.**

**You should use the officially released versions (https://github.com/mozilla/policy-templates/releases) if you are deploying changes.**

Policies can be specified using the Group Policy templates on Windows (https://github.com/mozilla/policy-templates/tree/master/windows), configuration profiles on macOS (https://github.com/mozilla/policy-templates/tree/master/mac), or by creating a file called `policies.json`. On Windows, create a directory called `distribution` where the EXE is located and place the file there. On Mac, the file goes into `Firefox.app/Contents/Resources/distribution`.  On Linux, the file goes into `firefox/distribution`, where `firefox` is the installation directory for firefox, which varies by distribution.

| Policy Name | Description
| --- | --- |
| **[`AppUpdateURL`](#AppUpdateURL)** | Change the URL for application update.
| **[`Authentication`](#Authentication)** | Configure sites that support integrated authentication.
| **[`BlockAboutAddons`](#blockaboutaddons)** | Block access to the Add-ons Manager (about:addons).
| **[`BlockAboutConfig`](#blockaboutconfig)** | Block access to about:config.
| **[`BlockAboutProfiles`](#blockaboutprofiles)** | Block access to About Profiles (about:profiles).
| **[`BlockAboutSupport`](#blockaboutsupport)** | Block access to Troubleshooting Information (about:support).
| **[`Bookmarks`](#bookmarks)** | Add bookmarks in either the bookmarks toolbar or menu.
| **[`CaptivePortal`](#captiveportal)** | Enable or disable the detection of captive portals.
| **[`Certificates`](#certificates)** |
| **[`Certificates -> ImportEnterpriseRoots`](#certificates--importenterpriseroots)** | Trust certificates that have been added to the operating system certificate store by a user or administrator.
| **[`Certificates -> Install`](#certificates--install)** | Install certificates into the Firefox certificate store.
| **[`Cookies`](#cookies)** | Configure cookie preferences.
| **[`DisableSetDesktopBackground`](#disablesetdesktopbackground)** | Remove the "Set As Desktop Background..." menuitem when right clicking on an image.
| **[`DisableMasterPasswordCreation`](#disablemasterpasswordcreation)** | Remove the master password functionality.
| **[`DisableAppUpdate`](#disableappupdate)** | Turn off application updates.
| **[`DisableBuiltinPDFViewer`](#disablebuiltinpdfviewer)** | Disable the built in PDF viewer.
| **[`DisableDeveloperTools`](#disabledevelopertools)** | Remove access to all developer tools.
| **[`DisableFeedbackCommands`](#disablefeedbackcommands)** | Disable the menus for reporting sites.
| **[`DisableFirefoxScreenshots`](#disablefirefoxscreenshots)** | Remove access to Firefox Screenshots.
| **[`DisableFirefoxAccounts`](#disablefirefoxaccounts)** | Disable Firefox Accounts integration (Sync).
| **[`DisableFirefoxStudies`](#disablefirefoxstudies)** | Disable Firefox studies (Shield).
| **[`DisableForgetButton`](#disableforgetbutton)** | Disable the "Forget" button.
| **[`DisableFormHistory`](#disableformhistory)** | Turn off saving information on web forms and the search bar.
| **[`DisablePocket`](#disablepocket)** | Remove Pocket in the Firefox UI.
| **[`DisablePrivateBrowsing`](#disableprivatebrowsing)** | Remove access to private browsing.
| **[`DisableProfileImport`](#disableprofileimport)** | Disables the "Import data from another browser" option in the bookmarks window.
| **[`DisableProfileRefresh`](#disableprofilerefresh)** | Disable the Refresh Firefox button on about:support and support.mozilla.org
| **[`DisableSafeMode`](#disablesafemode)** | Disable safe mode within the browser.
| **[`DisableSecurityBypass`](#disablesecuritybypass)** | Prevent the user from bypassing security in certain cases.
| **[`DisableSystemAddonUpdate`](#disablesystemaddonupdate)** | Prevent system add-ons from being installed or update.
| **[`DisableTelemetry`](#disabletelemetry)** | DisableTelemetry
| **[`DisplayBookmarksToolbar`](#displaybookmarkstoolbar)** | Set the initial state of the bookmarks toolbar.
| **[`DisplayMenuBar`](#displaymenubar)** | Set the initial state of the menubar.
| **[`DNSOverHTTPS`](#dnsoverhttps)** | Configure DNS over HTTPS.
| **[`DontCheckDefaultBrowser`](#dontcheckdefaultbrowser)** | Don't check if Firefox is the default browser at startup.
| **[`DefaultDownloadDirectory`](#defaultdownloaddirectory)** | Set the default download directory.
| **[`DownloadDirectory`](#downloaddirectory)** | Set and lock the download directory.
| **[`EnableTrackingProtection`](#enabletrackingprotection)** | Configure tracking protection.
| **[`EnterprisePoliciesEnabled`](#enterprisepoliciesenabled)** | Enable policy support on macOS.
| **[`Extensions`](#extensions)** | Control the installation, uninstallation and locking of extensions.
| **[`ExtensionSettings`](#extensionsettings)** | Manage all aspects of extensions.
| **[`ExtensionUpdate`](#extensionupdate)** | Control extension updates.
| **[`FlashPlugin`](#flashplugin)** | Configure the default Flash plugin policy as well as origins for which Flash is allowed.
| **[`FirefoxHome`](#firefoxhome)** | Customize the Firefox Home page.
| **[`HardwareAcceleration`](#hardwareacceleration)** | Control hardware acceleration.
| **[`Homepage`](#homepage)** | Configure the default homepage and how Firefox starts.
| **[`InstallAddonsPermission`](#installaddonspermission)** | Configure the default extension install policy as well as origins for extension installs are allowed.
| **[`LocalFileLinks`](#localfilelinks)** | Enable linking to local files by origin.
| **[`NetworkPrediction`](#networkprediction)** | Enable or disable network prediction (DNS prefetching).
| **[`NewTabPage`](#newtabpage)** | Enable or disable the New Tab page.
| **[`NoDefaultBookmarks`](#nodefaultbookmarks)** | Disable the creation of default bookmarks.
| **[`OfferToSaveLogins`](#offertosavelogins)** | Control whether or not Firefox offers to save passwords.
| **[`OverrideFirstRunPage`](#overridefirstrunpage)** | Override the first run page.
| **[`OverridePostUpdatePage`](#overridepostupdatepage)** | Override the upgrade page.
| **[`Permissions`](#permissions)** | Set permissions associated with camera, microphone, location, and notifications.
| **[`PopupBlocking`](#popupblocking)** | Configure the default pop-up window policy as well as origins for which pop-up windows are allowed.
| **[`Preferences`](#preferences)** | Set and lock some preferences.
| **[`PromptForDownloadLocation`](#promptfordownloadlocation)** | Ask where to save each file before downloading.
| **[`Proxy`](#proxy)** | Configure proxy settings.
| **[`RequestedLocales`](#requestedlocales)** | Set the the list of requested locales for the application in order of preference.
| **[`SanitizeOnShutdown` (All)](#sanitizeonshutdown-all)** | Clear all data on shutdown.
| **[`SanitizeOnShutdown` (Selective)](#sanitizeonshutdown-selective)** | Clear data on shutdown.
| **[`SearchBar`](#searchbar)** | Set whether or not search bar is displayed.
| **[`SearchEngines`](#searchengines-this-policy-is-only-available-on-the-esr)** |
| **[`SearchEngines -> Default`](#searchengines--default)** | Set the default search engine.
| **[`SearchEngines -> PreventInstalls`](#searchengines--preventinstalls)** | Prevent installing search engines from webpages.
| **[`SearchEngines -> Remove`](#searchengines--remove)** | Hide built-in search engines.
| **[`SearchEngines -> Add`](#searchengines--add)** | Add new search engines.
| **[`SecurityDevices`](#securitydevices)** | Install PKCS #11 modules.
| **[`SearchSuggestEnabled`](#searchsuggestenabled)** | Enable search suggestions.
| **[`SSLVersionMax`](#sslversionmax)** | Set and lock the maximum version of TLS.
| **[`SSLVersionMin`](#sslversionmin)** | Set and lock the minimum version of TLS.
| **[`SupportMenu`](#supportmenu)** | Add a menuitem to the help menu for specifying support information.
| **[`WebsiteFilter`](#websitefilter)** | Block websites from being visited.

### AppUpdateURL

Change the URL for application update.

**Compatibility:** Firefox 62, Firefox ESR 60.2\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `app.update.url`

#### Windows
```
Software\Policies\Mozilla\Firefox\AppUpdateURL = "https://yoursite.com"
```
#### macOS
```
<dict>
  <key>AppUpdateURL</key>
  <string>https://yoursite.com</string>
</dict>
```
#### JSON
```
{
  "policies": {
    "AppUpdateURL": "https://yoursite.com"
  }
}
```
### Authentication

Configure sites that support integrated authentication.

See https://developer.mozilla.org/en-US/docs/Mozilla/Integrated_authentication for more information.

**Compatibility:** Firefox 60, Firefox ESR 60 (AllowNonFQDN added in 62/60.2)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.negotiate-auth.trusted-uris`, `network.negotiate-auth.delegation-uris`, `network.automatic-ntlm-auth.trusted-uris`, `network.automatic-ntlm-auth.allow-non-fqdn`, `network.negotiate-auth.allow-non-fqdn`

#### Windows
```
Software\Policies\Mozilla\Firefox\Authentication\SPNEGO\1 = "mydomain.com"
Software\Policies\Mozilla\Firefox\Authentication\SPNEGO\2 = "https://myotherdomain.com"
Software\Policies\Mozilla\Firefox\Authentication\Delegated\1 = "mydomain.com"
Software\Policies\Mozilla\Firefox\Authentication\Delegated\2 = "https://myotherdomain.com"
Software\Policies\Mozilla\Firefox\Authentication\NTLM\1 = "mydomain.com"
Software\Policies\Mozilla\Firefox\Authentication\NTLM\2 = "https://myotherdomain.com"
Software\Policies\Mozilla\Firefox\Authentication\AllowNonFQDN\SPNEGO = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Authentication\AllowNonFQDN\NTLM = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>Authentication</key>
  <dict>
    <key>SPNEGO</key>
    <array>
      <string>mydomain.com</string>
      <string>https://myotherdomain.com</string>
    </array>
    <key>Delegated</key>
    <array>
      <string>mydomain.com</string>
      <string>https://myotherdomain.com</string>
    </array>
    <key>NTLM</key>
    <array>
      <string>mydomain.com</string>
      <string>https://myotherdomain.com</string>
    </array>
    <key>AllowNonFQDN</key>
      <dict>
      <key>SPNEGO</key>
      <true/> | <false/>
      <key>NTLM</key>
      <true/> | <false/>
    </dict>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Authentication": {
      "SPNEGO": ["mydomain.com", "https://myotherdomain.com"],
      "Delegated": ["mydomain.com", "https://myotherdomain.com"],
      "NTLM": ["mydomain.com", "https://myotherdomain.com"],
      "AllowNonFQDN": {
        "SPNEGO": true | false,
        "NTLM": true | false
      }
    }
  }
}
```
### BlockAboutAddons

Block access to the Add-ons Manager (about:addons).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAddonsManager`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\BlockAboutAddons = 0x1 | 0x0
```
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

Block access to about:config.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAboutConfig`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\BlockAboutConfig = 0x1 | 0x0
```
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

Block access to About Profiles (about:profiles).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAboutProfiles`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\BlockAboutProfiles = 0x1 | 0x0
```
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

Block access to Troubleshooting Information (about:support).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAboutSupport`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\BlockAboutSupport = 0x1 | 0x0
```
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

Add bookmarks in either the bookmarks toolbar or menu. Only `Title` and `URL` are required. If `Placement` is not specified, the bookmark will be placed on the toolbar. If `Folder` is specified, it is automatically created and bookmarks with the same folder name are grouped together.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `bookmarks.toolbar`,`bookmarks.menu`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\Bookmarks\1\Title = "Example"
Software\Policies\Mozilla\Firefox\Bookmarks\1\URL = "https://example.com"
Software\Policies\Mozilla\Firefox\Bookmarks\1\Favicon = "https://example.com/favicon.ico"
Software\Policies\Mozilla\Firefox\Bookmarks\1\Placement = "toolbar" | "menu"
Software\Policies\Mozilla\Firefox\Bookmarks\1\Folder = "FolderName"
```
#### macOS
```
<dict>
  <key>Bookmarks</key>
  <array>
    <dict>
      <key>Title</key>
      <string>Example</string>
      <key>URL</key>
      <string>https://example.com</string>
      <key>Favicon</key>
      <string>https://example.com/favicon.ico</string>
      <key>Placement</key>
      <string>toolbar | menu</string>
      <key>Folder</key>
      <string>FolderName</string>
    </dict>
  </array>
</dict>
```
#### JSON
```
{
  "policies": {
    "Bookmarks": [
      {
        "Title": "Example",
        "URL": "https://example.com",
        "Favicon": "https://example.com/favicon.ico",
        "Placement": "toolbar" | "menu",
        "Folder": "FolderName"
      }
    ]
  }
}
```
### CaptivePortal
Enable or disable the detection of captive portals.

**Compatibility:** Firefox 67, Firefox ESR 60.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.captive-portal-service.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\CaptivePortal = 0x1 | 0x0
```
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

### Certificates | ImportEnterpriseRoots

Trust certificates that have been added to the operating system certificate store by a user or administrator.

See https://support.mozilla.org/kb/setting-certificate-authorities-firefox for more detail.

**Compatibility:** Firefox 60, Firefox ESR 60 (macOS support in Firefox 63, Firefox ESR 68)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.enterprise_roots.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\Certificates\ImportEnterpriseRoots = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>Certificates</key>
  <dict>
    <key>ImportEnterpriseRoots</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": true | false
    }
  }
}
```
### Certificates | Install

Install certificates into the Firefox certificate store. If only a filename is specified, Firefox searches for the file in the following locations:

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

Starting with Firefox 65, Firefox 60.5 ESR, a fully qualified path can be used, including UNC paths. You should use the native path style for your operating system. We do not support using %USERPROFILE% or other environment variables on Windows.

If you are specifying the path in the policies.json file on Windows, you need to escape your backslashes (`\\`) which means that for UNC paths, you need to escape both (`\\\\`). If you use group policy, you only need one backslash.

Certificates are installed using the trust string `CT,CT,`.

Binary (DER) and ASCII (PEM) certificates are both supported.

**Compatibility:** Firefox 64, Firefox ESR 64\
**CCK2 Equivalent:** `certs.ca`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\Certificates\Install\1 = "cert1.der"
Software\Policies\Mozilla\Firefox\Certificates\Install\2 = "C:\Users\username\cert2.pem"
```
#### macOS
```
<dict>
  <key>Certificates</key>
  <dict>
    <key>Install</key>
    <array>
      <string>cert1.der</string>
      <string>/Users/username/cert2.pem</string>
    </array>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Certificates": {
      "Install": ["cert1.der", "/home/username/cert2.pem"]
    }
  }
}
```
### Cookies
Configure cookie preferences.

`Allow` is a list of origins (not domains) where cookies are always allowed. You must include http or https.

`Block` is a list of origins (not domains) where cookies are always blocked. You must include http or https.

`Default` determines whether cookies are accepted at all.

`AcceptThirdParty` determines how third-party cookies are handled.

`ExpireAtSessionEnd` determines when cookies expire.

`RejectTracker` only rejects cookies for trackers.

`Locked` prevents the user from changing cookie preferences.

**Compatibility:** Firefox 60, Firefox ESR 60 (RejectTracker was added in Firefox 63)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.cookie.cookieBehavior`,`network.cookie.lifetimePolicy`

#### Windows
```
Software\Policies\Mozilla\Firefox\Cookies\Allow\1 = "https://example.com"
Software\Policies\Mozilla\Firefox\Cookies\Block\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Cookies\Default = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Cookies\AcceptThirdParty = "always" | "never" |"from-visited"
Software\Policies\Mozilla\Firefox\Cookies\ExpireAtSessionEnd = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Cookies\RejectTracker = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Cookies\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>Cookies</key>
  <dict>
    <key>Allow</key>
    <array>
      <string>http://example.com</string>
    </array>
    <key>Block</key>
    <array>
      <string>http://example.org</string>
    </array>
    <key>Default</key>
    <true/> | <false/>
    <key>AcceptThirdParty</key>
    <string>always | never | from-visited</string>
    <key>ExpireAtSessionEnd</key>
    <true/> | <false/>
    <key>RejectTracker</key>
    <true/> | <false/>
    <key>Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Cookies": {
      "Allow": ["http://example.org/"],
      "Block": ["http://example.edu/"],
      "Default": true | false,
      "AcceptThirdParty": "always" | "never" | "from-visited"],
      "ExpireAtSessionEnd": true | false,
      "RejectTracker": true | false,
      "Locked": true | false
    }
  }
}
```
### DisableSetDesktopBackground
Remove the "Set As Desktop Background..." menuitem when right clicking on an image.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeSetDesktopBackground`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableSetDesktopBackground = 0x1 | 0x0
```

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
Remove the master password functionality.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `noMasterPassword`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableMasterPasswordCreation = 0x1 | 0x0
```

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
Turn off application updates.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableFirefoxUpdates`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableAppUpdate = 0x1 | 0x0
```
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
Disable the built in PDF viewer. PDF files are downloaded and sent externally.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePDFjs`\
**Preferences Affected:** `pdfjs.disabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableBuiltinPDFViewer = 0x1 | 0x0
```

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
Remove access to all developer tools.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeDeveloperTools`\
**Preferences Affected:** `devtools.policy.disabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableDeveloperTools = 0x1 | 0x0`
```

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
Disable the menus for reporting sites (Submit Feedback, Report Deceptive Site).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableFeedbackCommands = 0x1 | 0x0
```
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
Remove access to Firefox Screenshots.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `extensions.screenshots.disabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableFirefoxScreenshots = 0x1 | 0x0
```
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
Disable Firefox Accounts integration (Sync).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableSync`\
**Preferences Affected:** `identity.fxaccounts.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableFirefoxAccounts = 0x1 | 0x0
```
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
Disable Firefox studies (Shield).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableForget`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableFirefoxStudies = 0x1 | 0x0
```
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
Disable the "Forget" button.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableForget`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableForgetButton = 0x1 | 0x0
```
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
Turn off saving information on web forms and the search bar.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableFormFill`\
**Preferences Affected:** ` browser.formfill.enable`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableFormHistory = 0x1 | 0x0
```
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
Remove Pocket in the Firefox UI. It does not remove it from the new tab page.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePocket`\
**Preferences Affected:** `extensions.pocket.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisablePocket = 0x1 | 0x0
```
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
Remove access to private browsing.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePrivateBrowsing`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisablePrivateBrowsing = 0x1 | 0x0
```
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
Disables the "Import data from another browser" option in the bookmarks window.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableProfileImport = 0x1 | 0x0
```
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
Disable the Refresh Firefox button on about:support and support.mozilla.org, as well as the prompt that displays offering to refresh Firefox when you haven't used it in a while.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableResetFirefox`\
**Preferences Affected:** `browser.disableResetPrompt`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableProfileRefresh = 0x1 | 0x0
```
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
Disable safe mode within the browser.

On Windows, this disables safe mode via the command line as well.

**Compatibility:** Firefox 60, Firefox ESR 60 (Windows, macOS)\
**CCK2 Equivalent:** `disableSafeMode`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableSafeMode = 0x1 | 0x0
```
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
Prevent the user from bypassing security in certain cases.

`InvalidCertificate` prevents adding an exception when an invalid certificate is shown.

`SafeBrowsing` prevents selecting "ignore the risk" and visiting a harmful site anyway.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.certerror.hideAddException`,`browser.safebrowsing.allowOverride`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableSecurityBypass\InvalidCertificate = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisableSecurityBypass\SafeBrowsing = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>DisableSecurityBypass</key>
  <dict>
    <key>InvalidCertificate</key>
    <true/> | <false/>
    <key><SafeBrowsing/key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "DisableSecurityBypass": {
      "InvalidCertificate": true false,
      "SafeBrowsing": true false
    }
  }
}
```
### DisableSystemAddonUpdate
Prevent system add-ons from being installed or update.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
```Software\Policies\Mozilla\Firefox\DisableSystemAddonUpdate = 0x1 | 0x0
```
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
Prevent the upload of telemetry data.

Mozilla recommends that you do not disable telemetry. Information collected through telemetry helps us build a better product for businesses like yours.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableTelemetry`\
**Preferences Affected:** `datareporting.healthreport.uploadEnabled,datareporting.policy.dataSubmissionEnabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\DisableTelemetry = 0x1 | 0x0
```
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
Set the initial state of the bookmarks toolbar. A user can still hide it and it will stay hidden.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `displayBookmarksToolbar`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisplayBookmarksToolbar = 0x1 | 0x0
```
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
### DisplayMenuBar
Set the initial state of the menubar. A user can still hide it and it will stay hidden.

**Compatibility:** Firefox 60, Firefox ESR 60 (Windows, some Linux)\
**CCK2 Equivalent:** `displayMenuBar`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\DisplayMenuBar = 0x1 | 0x0
```
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
### DNSOverHTTPS
Configure DNS over HTTPS.

`Enabled` determines whether DNS over HTTPS is enabled

`ProviderURL` is a URL to another provider.

`Locked` prevents the user from changing DNS over HTTPS preferences.

**Compatibility:** Firefox 63, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.trr.mode`,`network.trr.uri`

#### Windows
```
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\ProviderURL = "URL_TO_ALTERNATE_PROVIDER"
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>DNSOverHTTPS</key>
  <dict>
    <key>Enabled</key>
    <true/> | <false/>
    <key>ProviderURL</key>
    <string>URL_TO_ALTERNATE_PROVIDER</string>
    <key>Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "DNSOverHTTPS": {
      "Enabled":  true | false,
      "ProviderURL": "URL_TO_ALTERNATE_PROVIDER",
      "Locked": true | false
    }
  }
}
```
### DontCheckDefaultBrowser
Don't check if Firefox is the default browser at startup.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontCheckDefaultBrowser`\
**Preferences Affected:** `browser.shell.checkDefaultBrowser`

#### Windows
```
Software\Policies\Mozilla\Firefox\DontCheckDefaultBrowser = 0x1 | 0x0
```
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
### DefaultDownloadDirectory
Set the default download directory.

You can use ${home} for the native home directory.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.download.dir`,`browser.download.folderList`

#### Windows
```
Software\Policies\Mozilla\Firefox\DefaultDownloadDirectory = "${home}\Downloads"
```
#### macOS
```
<dict>
  <key>DefaultDownloadDirectory</key>
  <string>${home}/Downloads</string>
</dict>
```
#### JSON (macOS and Linux)
```
{
  "policies": {
    "DefaultDownloadDirectory": "${home}/Downloads"
}
```
#### JSON (Windows)
```
{
  "policies": {
    "DefaultDownloadDirectory": "${home}\\Downloads"
}
```
### DownloadDirectory
Set and lock the download directory.

You can use ${home} for the native home directory.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.download.dir`,`browser.download.folderList`,`browser.download.useDownloadDir`

#### Windows
```
Software\Policies\Mozilla\Firefox\DownloadDirectory = "${home}\Downloads"
```
#### macOS
```
<dict>
  <key>DownloadDirectory</key>
  <string>${home}/Downloads</string>
</dict>
```
#### JSON (macOS and Linux)
```
{
  "policies": {
    "DownloadDirectory": "${home}/Downloads"
}
```
#### JSON (Windows)
```
{
  "policies": {
    "DownloadDirectory": "${home}\\Downloads"
}
```
### EnableTrackingProtection
Configure tracking protection.

If this policy is not configured, tracking protection is not enabled by default in the browser, but it is enabled by default in private browsing and the user can change it.

If `Value` is set to false, tracking protection is disabled and locked in both the regular browser and private browsing.

If `Value` is set to true, tracking protection is enabled by default in both the regular browser and private browsing and the `Locked` value determines whether or not a user can change it.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontCheckDefaultBrowser`\
**Preferences Affected:** `privacy.trackingprotection.enabled`,`privacy.trackingprotection.pbmode.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Value = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>EnableTrackingProtection</key>
  <dict>
    <key>Value</key>
    <true/> | <false/>
 
    <key><Locked/key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "EnableTrackingProtection": {
      "Value": [true, false],
      "Locked": [true, false]
    }
}
```
### EnterprisePoliciesEnabled
Enable policy support on macOS.

**Compatibility:** Firefox 63, Firefox ESR 60.3 (macOS only)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### macOS
```
<dict>
  <key>EnterprisePoliciesEnabled</key>
  <true/>
</dict>
```
### Extensions
Control the installation, uninstallation and locking of extensions.

`Install` is a list of URLs or native paths for extensions to be installed. 

`Uninstall` is a list of extension IDs that should be uninstalled if found.

`Locked` is a list of extension IDs that the user cannot disable or uninstall.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `addons`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\Extensions\Install\1 = "https://addons.mozilla.org/firefox/downloads/somefile.xpi"
Software\Policies\Mozilla\Firefox\Extensions\Install\2 = "//path/to/xpi"
Software\Policies\Mozilla\Firefox\Extensions\Uninstall\1 = "bad_addon_id@mozilla.org"
Software\Policies\Mozilla\Firefox\Extensions\Locked\1 = "addon_id@mozilla.org"
```
#### macOS
```
<dict>
  <key>Extensions</key>
  <dict>
    <key>Install</key>
    <array>
      <string>https://addons.mozilla.org/firefox/downloads/somefile.xpi</string>
      <string>//path/to/xpi</string>
    </array>
    <key>Uninstall</key>
    <array>
      <string>bad_addon_id@mozilla.org</string>
    </array>
    <key>Locked</key>
    <array>
      <string>addon_id@mozilla.org</string>
    </array>
  </dict>
</dict>
```
#### JSON


```
{
  "policies": {
    "Extensions": {
      "Install": ["https://addons.mozilla.org/firefox/downloads/somefile.xpi", "//path/to/xpi"],
      "Uninstall": ["bad_addon_id@mozilla.org"],
      "Locked":  ["addon_id@mozilla.org"]
    }
  }
}
```
### ExtensionSettings
Manage all aspects of extensions. This policy is based heavily on the [Chrome policy](https://dev.chromium.org/administrators/policy-list-3/extension-settings-full) of the same name.

This policy maps an extension ID to its configuration. With an extension ID, the configuration will be applied to the specified extension only. A default configuration can be set for the special ID "*", which will apply to all extensions that don't have a custom configuration set in this policy.

To obtain an extension ID, install the extension and go to about:support. You will see the ID in the Extensions section.

The configuration for each extension is another dictionary that can contain the fields documented below.

| Name | Description |
| --- | --- |
| `installation_mode` | Maps to a string indicating the installation mode for the extension. The valid strings are `allowed`,`blocked`,`force_installed`, and `normal_installed`.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`allowed` | Allows the extension to be installed by the user. This is the default behavior.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`blocked`| Blocks installation of the extension and removes it from the device if already installed.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`force_installed`| The extension is automatically installed and can't be removed by the user. This option is not valid for the default configuration and requires an install_url.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`normal_installed`| The extension is automatically installed but can be disabled by the user. This option is not valid for the default configuration and requires an install_url.
| `install_url`| Maps to a URL indicating where Firefox can download a force_installed or normal_installed extension. If installing from the addons.mozilla.org, use the following URL (substituting SHORT_NAME from the URL on AMO), https://addons.mozilla.org/firefox/downloads/latest/SHORT_NAME/latest.xpi. If installing frmo the local file system, use a file:/// URL.
| `install_sources` | Each item in this list is an extension-style match pattern. Users will be able to easily install items from any URL that matches an item in this list. Both the location of the *.xpi file and the page where the download is started from (i.e.  the referrer) must be allowed by these patterns. This setting can be used only for the default configuration.
| `allowed_types` | This setting whitelists the allowed types of extension/apps that can be installed in Firefox. The value is a list of strings, each of which should be one of the following: "extension", "theme", "dictionary", "langpack" This setting can be used only for the default configuration.
| `blocked_install_message` | This maps to a string specifying the error message to display to users if they're blocked from installing an extension. This setting allows you to append text to the generic error message displayed when the extension is blocked. This could be be used to direct users to your help desk, explain why a particular extension is blocked, or something else.

**Compatibility:** Firefox 69, Firefox ESR 68.1\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\ExtensionSettings = '{"*": {"installation_mode": "blocked"}}'
```
#### macOS
```
<dict>
  <key>ExtensionSettings</key>
  <dict>
    <key>*</key>
    <dict>
      <key>blocked_install_message</key>
      <string>Custom error message.</string>
      <key>install_sources</key>
      <array>
        <string>https://addons.mozilla.org/</string>
      </array>
      <key>installation_mode</key>
      <string>blocked</string>
    </dict>
    <key>uBlock0@raymondhill.net</key>
    <dict>
      <key>installation_mode</key>
       <string>force_installed</string>
      <key>install_url</key>
      <string>https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi</string>
    </dict>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "ExtensionSettings": {
      "*": {
        "blocked_install_message": "Custom error message.",
        "install_sources": ["https://addons.mozilla.org/"],
        "installation_mode": "blocked"
      },
      "uBlock0@raymondhill.net": {
        "installation_mode": "force_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"
      }
    }
  }
}
```
### ExtensionUpdate
Control extension updates.

**Compatibility:** Firefox 67, Firefox ESR 60.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `extensions.update.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\ExtensionUpdate = 0x1 | 0x0
```
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
### FlashPlugin
Configure the default Flash plugin policy as well as origins for which Flash is allowed.

`Allow` is a list of origins where Flash are allowed.

`Block` is a list of origins where Flash is not allowed.

`Default` determines whether or not Flash is allowed by default.

`Locked` prevents the user from changing Flash preferences.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `permissions.plugin`\
**Preferences Affected:** `plugin.state.flash`

#### Windows
```
Software\Policies\Mozilla\Firefox\FlashPlugin\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\FlashPlugin\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\FlashPlugin\Default = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FlashPlugin\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>FlashPlugin</key>
  <dict>
    <key>Allow</key>
    <array>
      <string>http://example.org</string>
    </array>
    <key>Block</key>
    <array>
      <string>http://example.edu</string>
    </array>
    <key>Default</key>
    <true/> | <false/>
    <key>Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "FlashPlugin": {
      "Allow": ["http://example.org/"],
      "Block": ["http://example.edu/"],
      "Default": true | false,
      "Locked": true | false
    }
  }
}
```
### FirefoxHome
Customize the Firefox Home page.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.newtabpage.activity-stream.showSearch`,`browser.newtabpage.activity-stream.feeds.topsites`,`browser.newtabpage.activity-stream.feeds.section.highlights`,`browser.newtabpage.activity-stream.feeds.section.topstories`,`browser.newtabpage.activity-stream.feeds.snippets`

#### Windows
```
Software\Policies\Mozilla\Firefox\FirefoxHome\Search = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\TopSites = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Highlights = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Pocket = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Snippets = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>FirefoxHome</key>
  <dict>
    <key>Search</key>
    <true/> | <false/>
    <key>TopSites</key>
    <true/> | <false/>
    <key>Highlights</key>
    <true/> | <false/>
    <key>Pocket</key>
    <true/> | <false/>
    <key>Snippets</key>
    <true/> | <false/>
    <key>Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "FirefoxHome": {
      "Search": true | false,
      "TopSites": true | false,
      "Highlights": true | false,
      "Pocket": true | false,
      "Snippets": true | false,
      "Locked": true | false
    }
  }
}
```
### HardwareAcceleration
Control hardware acceleration.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `layers.acceleration.disabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\HardwareAcceleration = 0x1 | 0x0
```
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
### Homepage
Configure the default homepage and how Firefox starts.

`URL` is the default homepage.

`Locked` prevents the user from changing homepage preferences.

`Additional` allows for more than one homepage.

`StartPage` is how Firefox starts. The choices are no homepage, the default homepage or the previous session.

**Compatibility:** Firefox 60, Firefox ESR 60 (StartPage was added in Firefox 60, Firefox ESR 60.4)\
**CCK2 Equivalent:** `homePage`,`lockHomePage`\
**Preferences Affected:** `browser.startup.homepage`,`browser.startup.page`

#### Windows
```
Software\Policies\Mozilla\Firefox\Homepage\URL = "https://example.com"
Software\Policies\Mozilla\Firefox\Homepage\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Homepage\Additional\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Homepage\Additional\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Homepage\StartPage = "none" | "homepage" |  "previous-session"
```
#### macOS
```
<dict>
  <key>Homepage</key>
  <dict>
    <key>URL</key>
    <string>http://example.com</string>
    <key>Locked</key>
    <true/> | <false/>
    <key>Additional</key>
    <array>
      <string>http://example.org</string>
      <string>http://example.edu</string>
    </array>
    <key>StartPage</key>
    <string>always | never | from-visited</string>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Homepage": {
      "URL": "http://example.com/",
      "Locked": true | false,
      "Additional": ["http://example.org/",
                     "http://example.edu/"],
      "StartPage": "none" | "homepage" |  "previous-session"
    }
  }
}
```
### InstallAddonsPermission
Configure the default extension install policy as well as origins for extension installs are allowed. This policy does not override turning off all extension installs.

`Allow` is a list of origins where extension installs are allowed.

`Default` determines whether or not extension installs are allowed by default.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `permissions.install`\
**Preferences Affected:** `xpinstall.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\InstallAddonsPermission\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\InstallAddonsPermission\Allow\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\InstallAddonsPermission\Default = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>InstallAddonsPermission</key>
  <dict>
    <key>Allow</key>
    <array>
      <string>http://example.org</string>
      <string>http://example.edu</string>
    </array>
    <key>Default</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "InstallAddonsPermission": {
      "Allow": ["http://example.org/",
                "http://example.edu/"],
      "Default": true | false
    }
  }
}
```
### LocalFileLinks
Enable linking to local files by origin.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `capability.policy.localfilelinks.*`

#### Windows
```
Software\Policies\Mozilla\Firefox\LocalFileLinks\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\LocalFileLinks\2 = "https://example.edu"
```
#### macOS
```
<dict>
  <key>LocalFileLinks</key>
  <array>
    <string>http://example.org</string>
    <string>http://example.edu</string>
  </array>
</dict>
```
#### JSON
```
{
  "policies": {
    "LocalFileLinks": ["http://example.org/",
                       "http://example.edu/"]
  }
}
```
### NoDefaultBookmarks
Disable the creation of default bookmarks.

This policy is only effective if the user profile has not been created yet.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeDefaultBookmarks`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\NoDefaultBookmarks = 0x1 | 0x0
```
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
### NetworkPrediction
Enable or disable network prediction (DNS prefetching).

**Compatibility:** Firefox 67, Firefox ESR 60.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.dns.disablePrefetch`,`network.dns.disablePrefetchFromHTTPS`

#### Windows
```
Software\Policies\Mozilla\Firefox\NetworkPrediction = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>NetworkPrediction</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "NetworkPrediction": true | false
}
```
### NewTabPage
Enable or disable the New Tab page.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.newtabpage.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\NewTabPage = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>NewTabPage</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "NewTabPage": true | false
}
```
### OfferToSaveLogins
Control whether or not Firefox offers to save passwords.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontRememberPasswords`\
**Preferences Affected:** `signon.rememberSignons`

#### Windows
```
Software\Policies\Mozilla\Firefox\OfferToSaveLogins = 0x1 | 0x0
```
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
### OverrideFirstRunPage
Override the first run page. If the value is blank, no first run page is displayed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `welcomePage`,`noWelcomePage`\
**Preferences Affected:** `startup.homepage_welcome_url`

#### Windows
```
Software\Policies\Mozilla\Firefox\OverrideFirstRunPage = "http://example.org"
```
#### macOS
```
<dict>
  <key>OverrideFirstRunPage</key>
  <string>http://example.org</string>
</dict>
```
#### JSON
```
{
  "policies": {
    "OverrideFirstRunPage": "http://example.org"
}
```
### OverridePostUpdatePage
Override the upgrade page. If the value is blank, no upgrade page is displayed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `upgradePage`,`noUpgradePage`\
**Preferences Affected:** `startup.homepage_override_url`

#### Windows
```
Software\Policies\Mozilla\Firefox\OverridePostUpdatePage = "http://example.org"
```
#### macOS
```
<dict>
  <key>OverridePostUpdatePage</key>
  <string>http://example.org</string>
</dict>
```
#### JSON
```
{
  "policies": {
    "OverridePostUpdatePage": "http://example.org"
}
```
### Permissions
Set permissions associated with camera, microphone, location, and notifications

`Allow` is a list of origins where the feature is allowed.

`Block` is a list of origins where the feature is not allowed.

`BlockNewRequests` determines whether or not new requests can be made for the feature.

`Locked` prevents the user from changing preferences for the feature.

**Compatibility:** Firefox 62, Firefox ESR 60.2\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `permissions.default.camera`,`permissions.default.microphone`,`permissions.default.geo`,`permissions.default.desktop-notification`

#### Windows
```
Software\Policies\Mozilla\Firefox\Permissions\Camera\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Camera\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Camera\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Camera\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Microphone\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Location\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Location\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Location\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Location\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Notifications\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>Permissions</key>
  <dict>
    <key>Camera</key>
    <dict>
      <key>Allow</key>
      <array>
        <string>https://example.org</string>
      </array>
      <key>Block</key>
      <array>
        <string>https://example.edu</string>
      </array>
      <key>BlockNewRequests</key>
      <true/>
      <key>Locked</key>
      <true/>
    </dict>
    <key>Microphone</key>
    <dict>
      <key>Allow</key>
      <array>
        <string>https://example.org</string>
      </array>
      <key>Block</key>
      <array>
        <string>https://example.edu</string>
      </array>
      <key>BlockNewRequests</key>
      <true/>
      <key>Locked</key>
      <true/>
    </dict>
    <key>Location</key>
    <dict>
      <key>Allow</key>
      <array>
        <string>https://example.org</string>
      </array>
      <key>Block</key>
      <array>
        <string>https://example.edu</string>
      </array>
      <key>BlockNewRequests</key>
      <true/>
      <key>Locked</key>
      <true/>
    </dict>
    <key>Notifications</key>
    <dict>
      <key>Allow</key>
      <array>
        <string>https://example.org</string>
      </array>
      <key>Block</key>
      <array>
        <string>https://example.edu</string>
      </array>
      <key>BlockNewRequests</key>
      <true/>
      <key>Locked</key>
      <true/>
    </dict>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Permissions": {
      "Camera": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "BlockNewRequests": true | false,
        "Locked": true | false
      },
      "Microphone": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "BlockNewRequests": true | false,
        "Locked": true | false
      },
      "Location": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "BlockNewRequests": true | false,
        "Locked": true | false
      },
      "Notifications": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "BlockNewRequests": true | false,
        "Locked": true | false
      }
    }
  }
}
```
### PopupBlocking
Configure the default pop-up window policy as well as origins for which pop-up windows are allowed.

`Allow` is a list of origins where popup-windows are allowed.

`Default` determines whether or not pop-up windows are allowed by default.

`Locked` prevents the user from changing pop-up preferences.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `permissions.popup`\
**Preferences Affected:** `dom.disable_open_during_load`

#### Windows
```
Software\Policies\Mozilla\Firefox\PopupBlocking\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\PopupBlocking\Allow\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\PopupBlocking\Default = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\PopupBlocking\Locked = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>PopupBlocking</key>
  <dict>
    <key>Allow</key>
    <array>
      <string>http://example.org</string>
      <string>http://example.edu</string>
    </array>
    <key>Default</key>
    <true/> | <false/>
    <key>Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "PopupBlocking": {
      "Allow": ["http://example.org/",
                "http://example.edu/"],
      "Default": true | false,
      "Locked": true | false
    }
  }
}
```
### Preferences
Set and lock certain preferences.

**Compatibility:** See below\
**CCK2 Equivalent:** `preferences`\
**Preferences Affected:** See below

| Preference | Type | Compatibility
| --- | --- | ---
| app.update.auto | boolean | Firefox 68, Firefox 68 ESR
| browser.cache.disk.enable | boolean | Firefox 68, Firefox 68 ESR
| browser.cache.disk.parent_directory | string | Firefox 68, Firefox 68 ESR
| browser.fixup.dns_first_for_single_words | boolean | Firefox 68, Firefox 68 ESR
| browser.search.update | boolean | Firefox 68, Firefox 68 ESR
| browser.tabs.warnOnClose | boolean | Firefox 68, Firefox 68 ESR
| browser.urlbar.suggest.bookmark | boolean | Firefox 68, Firefox 68 ESR
| browser.urlbar.suggest.history | boolean | Firefox 68, Firefox 68 ESR
| browser.urlbar.suggest.openpage | boolean | Firefox 68, Firefox 68 ESR
| datareporting.policy.dataSubmissionPolicyBypassNotification | boolean | Firefox 68, Firefox 68 ESR
| dom.disable_window_flip | boolean | Firefox 68, Firefox 68 ESR
| dom.disable_window_move_resize | boolean | Firefox 68, Firefox 68 ESR
| dom.event.contextmenu.enabled | boolean | Firefox 68, Firefox 68 ESR
| dom.keyboardevent.keypress.hack.dispatch_non_printable_keys.addl | string | Firefox 68, Firefox 68 ESR
| dom.keyboardevent.keypress.hack.use_legacy_keycode_and_charcode.addl | string | Firefox 68, Firefox 68 ESR
| extensions.getAddons.showPane | boolean | Firefox 68, Firefox 68 ESR
| media.gmp-gmpopenh264.enabled | boolean | Firefox 68, Firefox 68 ESR
| media.gmp-widevinecdm.enabled | boolean | Firefox 68, Firefox 68 ESR
| network.dns.disableIPv6 | boolean | Firefox 68, Firefox 68 ESR
| network.IDN_show_punycode | boolean | Firefox 68, Firefox 68 ESR
| places.history.enabled | boolean | Firefox 68, Firefox 68 ESR
| security.default_personal_cert | string | Firefox 68, Firefox 68 ESR
| security.ssl.errorReporting.enabled | boolean | Firefox 68, Firefox 68 ESR
| ui.key.menuAccessKeyFocuses | boolean | Firefox 68, Firefox 68 ESR
#### Windows
```
Software\Policies\Mozilla\Firefox\Preferences\boolean_preference_name = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Preferences\string_preference_name = "string_value"
```
#### macOS
```
<dict>
  <key>Preferences</key>
  <dict>
    <key>boolean_preference_name</key>
    <true/> | <false/>
    <key>string_preference_name</key>
    <string>string_value</string>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Preferences": {
      "boolean_preference_name": true | false,
      "string_preference_name": "string_value"
    }
  }
}
```
### PromptForDownloadLocation
Ask where to save each file before downloading.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A
**Preferences Affected:** `browser.download.useDownloadDir`

#### Windows
```
Software\Policies\Mozilla\Firefox\PromptForDownloadLocation = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>PromptForDownloadLocation</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "PromptForDownloadLocation": true | false
  }
}
```
### Proxy
Configure proxy settings. These settings correspond to the connection settings in Firefox preferences.
To specify ports, append them to the hostnames with a colon (:).

`Mode` is the proxy method being used.

`Locked` is whether or not proxy settings can be changed.

`HTTPProxy` is the HTTP proxy server.

`UseHTTPProxyForAllProtocols` is whether or not the HTTP proxy should be used for all other proxies.

`SSLProxy` is the SSL proxy server.

`FTPProxy` is the FTP proxy server.

`SOCKSProxy` is the SOCKS proxy server

`SOCKSVersion` is the SOCKS version (4 or 5)

`Passthrough` is list of hostnames or IP addresses that will not be proxied. Use `<local>` to bypass proxying for all hostnames which do not contain periods.

`AutoConfigURL` is a  URL for proxy configuration (only used if Mode is autoConfig).

`AutoLogin` means do not prompt for authentication if password is saved.

`UseProxyForDNS` to use proxy DNS when using SOCKS v5.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `networkProxy*`\
**Preferences Affected:** `network.proxy.type`,`network.proxy.autoconfig_url`,`network.proxy.socks_remote_dns`,`signon.autologin.proxy`,`network.proxy.socks_version`,`network.proxy.no_proxies_on`,`network.proxy.share_proxy_settings`,`network.proxy.http`,`network.proxy.http_port`,`network.proxy.ftp`,`network.proxy.ftp_port`,`network.proxy.ssl`,`network.proxy.ssl_port`,`network.proxy.socks`,`network.proxy.socks_port`

#### Windows
```
Software\Policies\Mozilla\Firefox\Proxy\Mode = "none", "system", "manual", "autoDetect", "autoConfig"
Software\Policies\Mozilla\Firefox\Proxy\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\=Proxy\HTTPProxy = https://httpproxy.example.com
Software\Policies\Mozilla\Firefox\Proxy\UseHTTPProxyForAllProtocols = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Proxy\SSLProxy = https://sslproxy.example.com
Software\Policies\Mozilla\Firefox\Proxy\FTPProxy = https://ftpproxy.example.com
Software\Policies\Mozilla\Firefox\Proxy\SOCKSProxy = https://socksproxy.example.com
Software\Policies\Mozilla\Firefox\Proxy\SOCKSVersion = 0x4 | 0x5
Software\Policies\Mozilla\Firefox\Proxy\Passthrough = <local>
Software\Policies\Mozilla\Firefox\Proxy\AutoConfigURL = URL_TO_AUTOCONFIG
Software\Policies\Mozilla\Firefox\Proxy\AutoLogin = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Proxy\UseProxyForDNS = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>Proxy</key>
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
    <key>SOCKSVersion</key>
    <string>4 | 5</string>
    <key>Passthrough</key>
    <string>&lt;local>&gt;</string>
    <key>AutoConfigURL</key>
    <string>URL_TO_AUTOCONFIG</string>
    <key>AutoLogin</key>
    <true> | </false>
    <key>UseProxyForDNS</key>
    <true> | </false>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "Proxy": {
      "Mode": "none", "system", "manual", "autoDetect", "autoConfig",
      "Locked": [true, false],
      "HTTPProxy": "hostname",
      "UseHTTPProxyForAllProtocols": [true, false],
      "SSLProxy": "hostname",
      "FTPProxy": "hostname",
      "SOCKSProxy": "hostname",
      "SOCKSVersion": 4 | 5
      "Passthrough": "<local>",
      "AutoConfigURL": "URL_TO_AUTOCONFIG",
      "AutoLogin":  [true, false],
      "UseProxyForDNS": [true, false]
    }
  }
}
```
### RequestedLocales
Set the the list of requested locales for the application in order of preference. It will cause the corresponding language pack to become active.

Note: For Firefox 68, this can now be a string so that you can specify an empty value.

**Compatibility:** Firefox 64, Firefox ESR 60.4, Updated in Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A
#### Windows
```
Software\Policies\Mozilla\Firefox\RequestedLocales\1 = "de"
Software\Policies\Mozilla\Firefox\RequestedLocales\2 = "en-US"

or

Software\Policies\Mozilla\Firefox\RequestedLocales = "de,en-US"
```
#### macOS
```
<dict>
  <key>RequestedLocales</key>
  <array>
    <string>de</string>
    <string>en-US</string>
  </array>
</dict>

or

<dict>
  <key>RequestedLocales</key>
  <string>de,en-US</string>
</dict>

```
#### JSON
```
{
  "policies": {
    "RequestedLocales": ["de", "en-US"]
  }
}

or

{
  "policies": {
    "RequestedLocales": "de,en-US"
  }
}
```
### SanitizeOnShutdown (Selective)
Clear data on shutdown. Choose from Cache, Cookies, Download History, Form & Search History, Browsing History, Active Logins, Site Preferences and Offline Website Data.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown`,`privacy.clearOnShutdown.cache`,`privacy.clearOnShutdown.cookies`,`privacy.clearOnShutdown.downloads`,`privacy.clearOnShutdown.formdata`,`privacy.clearOnShutdown.history`,`privacy.clearOnShutdown.sessions`,`privacy.clearOnShutdown.siteSettings`,`privacy.clearOnShutdown.offlineApps`
#### Windows
```
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Cache = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Cookies = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Downloads = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\FormData = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\History = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Sessions = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\SiteSettings = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\OfflineApps = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>SanitizeOnShutdown</key>
  <dict>
    <key>Cache</key>
    <true/> | <false/>
    <key>Cookies</key>
    <true/> | <false/>
    <key>Downloads</key>
    <true/> | <false/>
    <key>FormData</key>
    <true/> | <false/>
    <key>History</key>
    <true/> | <false/>
    <key>Sessions</key>
    <true/> | <false/>
    <key>SiteSettings</key>
    <true/> | <false/>
    <key>OfflineApps</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "SanitizeOnShutdown": {
      "Cache": true | false,
      "Cookies": true | false,
      "Downloads": true | false,
      "FormData": true | false,
      "History": true | false,
      "Sessions": true | false,
      "SiteSettings": true | false,
      "OfflineApps": true | false
    }
  }
}
```
### SanitizeOnShutdown (All)
Clear all data on shutdown, including Browsing & Download History, Cookies, Active Logins, Cache, Form & Search History, Site Preferences and Offline Website Data.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown`,`privacy.clearOnShutdown.cache`,`privacy.clearOnShutdown.cookies`,`privacy.clearOnShutdown.downloads`,`privacy.clearOnShutdown.formdata`,`privacy.clearOnShutdown.history`,`privacy.clearOnShutdown.sessions`,`privacy.clearOnShutdown.siteSettings`,`privacy.clearOnShutdown.offlineApps`
#### Windows
```
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown = 0x1 | 0x0
```
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
### SearchBar
Set whether or not search bar is displayed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `showSearchBar`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SearchBar = "unified" | "separate"
```
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





### SearchEngines (This policy is only available on the ESR.)

### SearchEngines | Default

Set the default search engine. This policy is only available on the ESR.

**Compatibility:** Firefox ESR 60\
**CCK2 Equivalent:** `defaultSearchEngine`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SearchEngines\Default = NAME_OF_SEARCH_ENGINE
```
#### macOS
```
<dict>
  <key>SearchEngines</key>
  <dict>
    <key>Default</key>
    <string>NAME_OF_SEARCH_ENGINE</string>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "SearchEngines": {
      "Default": "NAME_OF_SEARCH_ENGINE"
    }
  }
}
```
### SearchEngines | PreventInstalls

Prevent installing search engines from webpages.

**Compatibility:** Firefox ESR 60\
**CCK2 Equivalent:** `disableSearchEngineInstall`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SearchEngines\PreventInstalls = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>SearchEngines</key>
  <dict>
    <key>PreventInstalls</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "SearchEngines": {
      "PreventInstalls": true | false
    }
  }
}
```
### SearchEngines | Remove

Hide built-in search engines. This policy is only available on the ESR.

**Compatibility:** Firefox ESR 60.2\
**CCK2 Equivalent:** `removeDefaultSearchEngines` (removed all built-in engines)\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SearchEngines\Remove\1 = NAME_OF_SEARCH_ENGINE
```
#### macOS
```
<dict>
  <key>SearchEngines</key>
  <dict>
    <key>Remove</key>
    <array>
      <string>NAME_OF_SEARCH_ENGINE</string>
    </array>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "SearchEngines": {
      "Remove": ["NAME_OF_SEARCH_ENGINE"]
    }
  }
}
```
### SearchEngines | Add

Add new search engines (up to five). This policy is only available on the ESR. `Name` and `URLTemplate` are required.

`Name` is the name of the search engine.

`URLTemplate` is the search URL with {searchTerms} to substitute for the search term.

`Method` is either GET or POST

`IconURL` is a URL for the icon to use.

`Alias` is a keyword to use for the engine.

`Description` is a description of the search engine.

`PostData` is the POST data as name value pairs separated by &.

`SuggestURLTemplate` is a search suggestions URL with {searchTerms} to substitute for the search term.

**Compatibility:** Firefox ESR 60 (POST support in Firefox ESR 68)\
**CCK2 Equivalent:** `searchplugins`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Name = "Example1"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\URLTemplate = "https://www.example.org/q={searchTerms}"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Method = "GET" | "POST"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\IconURL = "https://www.example.org/favicon.ico"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Alias = "example"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\Description = "Example Description"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\SuggestURLTemplate = "https://www.example.org/suggestions/q={searchTerms}"
Software\Policies\Mozilla\Firefox\SearchEngines\Add\1\PostData = "name=value&q={searchTerms}"
```

#### macOS
```
<dict>
  <key>SearchEngines</key>
  <dict>
    <key>Add</key>
    <array>
      <dict>
        <key>Name</key>
        <string>Example1</string>
        <key>URLTemplate</key>
        <string>https://www.example.org/q={searchTerms}</string>
        <key>Method</key>
        <string>GET | POST </string>
        <key>IconURL</key>
        <string>https://www.example.org/favicon.ico</string>
        <key>Alias</key>
        <string>example</string>
        <key>Description</key>
        <string>Example Description</string>
        <key>SuggestURLTemplate</key>
        <string>https://www.example.org/suggestions/q={searchTerms}</string>
        <key>PostData</key>
        <string>name=value&q={searchTerms}</string>
      </dict>
    <array>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "SearchEngines": {
      "Add": [
        {
          "Name": "Example1",
          "URLTemplate": "https://www.example.org/q={searchTerms}",
          "Method": "GET" | "POST",
          "IconURL": "https://www.example.org/favicon.ico",
          "Alias": "example",
          "Description": "Description",
          "PostData": "name=value&q={searchTerms}",
          "SuggestURLTemplate": "https://www.example.org/suggestions/q={searchTerms}"
        }
      ]
    }
  }
}
```
### SearchSuggestEnabled

Enable search suggestions.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.urlbar.suggest.searches`,`browser.search.suggest.enabled`

#### Windows
```
Software\Policies\Mozilla\Firefox\SearchSuggestEnabled = 0x1 | 0x0
```
#### macOS
```
<dict>
  <key>SearchSuggestEnabled</key>
  <true/> | <false/>
</dict>
```
#### JSON
```
{
  "policies": {
    "SearchSuggestEnabled": true | false
  }
}
```
### SecurityDevices

Install PKCS #11 modules.

**Compatibility:** Firefox 64, Firefox ESR 60.4\
**CCK2 Equivalent:** `certs.devices`\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SecurityDevices\NAME_OF_DEVICE = PATH_TO_LIBRARY_FOR_DEVICE
```
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

Set and lock the maximum version of TLS.

**Compatibility:** Firefox 66, Firefox ESR 60.6\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.tls.version.max`

#### Windows
```
Software\Policies\Mozilla\Firefox\SSLVersionMax = "tls1" | "tls1.1" | "tls1.2" | "tls1.3"
```
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

Set and lock the minimum version of TLS.

**Compatibility:** Firefox 66, Firefox ESR 60.6\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.tls.version.min`

#### Windows
```
Software\Policies\Mozilla\Firefox\SSLVersionMin = "tls1" | "tls1.1" | "tls1.2" | "tls1.3"
```
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
### SupportMenu
Add a menuitem to the help menu for specifying support information.

**Compatibility:** Firefox 68.0.1, Firefox ESR 68.0.1\
**CCK2 Equivalent:** helpMenu\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\SupportMenu\Title = "Support Menu"
Software\Policies\Mozilla\Firefox\SupportMenu\URL = "http://example.com/support"
Software\Policies\Mozilla\Firefox\SupportMenu\Title = "S"
```
#### macOS
```
<dict>
  <key>SupportMenu</key>
  <dict>
    <key>Title</key>
    <string>SupportMenu</string>
    <key>URL</key>
    <string>http://example.com/support</string>
    <key>AccessKey</key>
    <string>S</string>
  </dict>
</dict>
```
#### JSON
```
{
  "policies": {
    "SupportMenu": {
      "Title": "Support Menu",
      "URL": "http://example.com/support",
      "AccessKey": "S"
    }
  }
}
```
### WebsiteFilter
Block websites from being visited. The parameters take an array of Match Patterns, as documented in https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Match_patterns. Only http/https addresses are supported at the moment. The arrays are limited to 1000 entries each.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows
```
Software\Policies\Mozilla\Firefox\WebsiteFilters\Block\1 = "<all_urls>"
Software\Policies\Mozilla\Firefox\WebsiteFilters\Exceptions\1 = "http://example.org/*"
```
#### macOS
```
<dict>
  <key>WebsiteFilter</key>
  <dict>
    <key>Block</key>
    <array>
      <string><all_urls></string>
    </array>
    <key>Exceptions</key>
    <array>
      <string>http://example.org/*</string>
    </array>
  </dict>

</dict>
```
#### JSON
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
