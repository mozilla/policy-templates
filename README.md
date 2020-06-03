**These policies are in active development and so might contain changes that do not work with current versions of Firefox.**

**You should use the [officially released versions](https://github.com/mozilla/policy-templates/releases) if you are deploying changes.**

Policies can be specified using the [Group Policy templates on Windows](https://github.com/mozilla/policy-templates/tree/master/windows), [Intune on Windows](https://support.mozilla.org/kb/managing-firefox-intune), [configuration profiles on macOS](https://github.com/mozilla/policy-templates/tree/master/mac), or by creating a file called `policies.json`. On Windows, create a directory called `distribution` where the EXE is located and place the file there. On Mac, the file goes into `Firefox.app/Contents/Resources/distribution`.  On Linux, the file goes into `firefox/distribution`, where `firefox` is the installation directory for firefox, which varies by distribution.

| Policy Name | Description
| --- | --- |
| **[`AppAutoUpdate`](#appautoupdate)** |  Enable or disable automatic application update.
| **[`AppUpdateURL`](#appupdateurl)** | Change the URL for application update.
| **[`Authentication`](#authentication)** | Configure sites that support integrated authentication.
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
| **[`DisabledCiphers`](#disabledciphers)** | Disable ciphers.
| **[`DisableDefaultBrowserAgent`](#disabledefaultbrowseragent)** | Prevent the default browser agent from taking any actions (Windows only).
| **[`DisableDeveloperTools`](#disabledevelopertools)** | Remove access to all developer tools.
| **[`DisableFeedbackCommands`](#disablefeedbackcommands)** | Disable the menus for reporting sites.
| **[`DisableFirefoxScreenshots`](#disablefirefoxscreenshots)** | Remove access to Firefox Screenshots.
| **[`DisableFirefoxAccounts`](#disablefirefoxaccounts)** | Disable Firefox Accounts integration (Sync).
| **[`DisableFirefoxStudies`](#disablefirefoxstudies)** | Disable Firefox studies (Shield).
| **[`DisableForgetButton`](#disableforgetbutton)** | Disable the "Forget" button.
| **[`DisableFormHistory`](#disableformhistory)** | Turn off saving information on web forms and the search bar.
| **[`DisablePasswordReveal`](#disablepasswordreveal)** | Do not allow passwords to be revealed in saved logins.
| **[`DisablePocket`](#disablepocket)** | Remove Pocket in the Firefox UI.
| **[`DisablePrivateBrowsing`](#disableprivatebrowsing)** | Remove access to private browsing.
| **[`DisableProfileImport`](#disableprofileimport)** | Disables the "Import data from another browser" option in the bookmarks window.
| **[`DisableProfileRefresh`](#disableprofilerefresh)** | Disable the Refresh Firefox button on about:support and support.mozilla.org
| **[`DisableSafeMode`](#disablesafemode)** | Disable safe mode within the browser.
| **[`DisableSecurityBypass`](#disablesecuritybypass)** | Prevent the user from bypassing security in certain cases.
| **[`DisableSystemAddonUpdate`](#disablesystemaddonupdate)** | Prevent system add-ons from being installed or update.
| **[`DisableTelemetry`](#disabletelemetry)** | DisableTelemetry
| **[`DisplayBookmarksToolbar`](#displaybookmarkstoolbar)** | Set the initial state of the bookmarks toolbar.
| **[`DisplayMenuBar (Deprecated)`](#displaymenubar-deprecated)** | Set the initial state of the menubar.
| **[`DisplayMenuBar`](#displaymenubar)** | Set the state of the menubar.
| **[`DNSOverHTTPS`](#dnsoverhttps)** | Configure DNS over HTTPS.
| **[`DontCheckDefaultBrowser`](#dontcheckdefaultbrowser)** | Don't check if Firefox is the default browser at startup.
| **[`DefaultDownloadDirectory`](#defaultdownloaddirectory)** | Set the default download directory.
| **[`DownloadDirectory`](#downloaddirectory)** | Set and lock the download directory.
| **[`EnableTrackingProtection`](#enabletrackingprotection)** | Configure tracking protection.
| **[`EncryptedMediaExtensions`](#encryptedmediaextensions)** | Enable or disable Encrypted Media Extensions and optionally lock it.
| **[`EnterprisePoliciesEnabled`](#enterprisepoliciesenabled)** | Enable policy support on macOS.
| **[`Extensions`](#extensions)** | Control the installation, uninstallation and locking of extensions.
| **[`ExtensionSettings`](#extensionsettings)** | Manage all aspects of extensions.
| **[`ExtensionUpdate`](#extensionupdate)** | Control extension updates.
| **[`FlashPlugin`](#flashplugin)** | Configure the default Flash plugin policy as well as origins for which Flash is allowed.
| **[`FirefoxHome`](#firefoxhome)** | Customize the Firefox Home page.
| **[`HardwareAcceleration`](#hardwareacceleration)** | Control hardware acceleration.
| **[`Homepage`](#homepage)** | Configure the default homepage and how Firefox starts.
| **[`InstallAddonsPermission`](#installaddonspermission)** | Configure the default extension install policy as well as origins for extension installs are allowed.
| **[`LegacyProfiles`](#legacyprofiles)** | Disable the feature enforcing a separate profile for each installation.
| **[`LocalFileLinks`](#localfilelinks)** | Enable linking to local files by origin.
| **[`NetworkPrediction`](#networkprediction)** | Enable or disable network prediction (DNS prefetching).
| **[`NewTabPage`](#newtabpage)** | Enable or disable the New Tab page.
| **[`NoDefaultBookmarks`](#nodefaultbookmarks)** | Disable the creation of default bookmarks.
| **[`OfferToSaveLogins`](#offertosavelogins)** | Control whether or not Firefox offers to save passwords.
| **[`OfferToSaveLoginsDefault`](#offertosaveloginsdefault)** | Set the default value for whether or not Firefox offers to save passwords.
| **[`OverrideFirstRunPage`](#overridefirstrunpage)** | Override the first run page.
| **[`OverridePostUpdatePage`](#overridepostupdatepage)** | Override the upgrade page.
| **[`PasswordManagerEnabled`](#passwordmanagerenabled)** | Remove (some) access to the password manager.
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
| **[`SearchSuggestEnabled`](#searchsuggestenabled)** | Enable search suggestions.
| **[`SecurityDevices`](#securitydevices)** | Install PKCS #11 modules.
| **[`SSLVersionMax`](#sslversionmax)** | Set and lock the maximum version of TLS.
| **[`SSLVersionMin`](#sslversionmin)** | Set and lock the minimum version of TLS.
| **[`SupportMenu`](#supportmenu)** | Add a menuitem to the help menu for specifying support information.
| **[`UserMessaging`](#usermessaging)** | Don't show certain messages to the user.
| **[`WebsiteFilter`](#websitefilter)** | Block websites from being visited.

### AppAutoUpdate

Enable or disable **automatic** application update.

If set to true, application updates are installed without user approval.

If set to false, application updates are downloaded but the user can choose when to install the update.

If you have disabled updates via DisableAppUpdate, this policy has no effect.

**Compatibility:** Firefox 75, Firefox ESR 68.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** app.update.auto

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AppAutoUpdate = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppAutoUpdate
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>AppAutoUpdate</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AppAutoUpdate": true | false
  }
}
```
### AppUpdateURL

Change the URL for application update.

**Compatibility:** Firefox 62, Firefox ESR 60.2\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `app.update.url`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AppUpdateURL = "https://yoursite.com"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppUpdateURL
```
Value (string):
```
<enabled/>
<data id="AppUpdateURL" value="https://yoursite.com"/>
```
#### macOS
```
<dict>
  <key>AppUpdateURL</key>
  <string>https://yoursite.com</string>
</dict>
```
#### policies.json
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

`PrivateBrowsing` enables integrated authentication in prviate browsing.

**Compatibility:** Firefox 60, Firefox ESR 60 (AllowNonFQDN added in 62/60.2, AllowProxies added in 70/68.2, Locked added in 71/68.3, PrivateBrowsing added in 77/68.9)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.negotiate-auth.trusted-uris`,`network.negotiate-auth.delegation-uris`,`network.automatic-ntlm-auth.trusted-uris`,`network.automatic-ntlm-auth.allow-non-fqdn`,`network.negotiate-auth.allow-non-fqdn`,`network.automatic-ntlm-auth.allow-proxies`,`network.negotiate-auth.allow-proxies`,`network.auth.private-browsing-sso`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Authentication\SPNEGO\1 = "mydomain.com"
Software\Policies\Mozilla\Firefox\Authentication\SPNEGO\2 = "https://myotherdomain.com"
Software\Policies\Mozilla\Firefox\Authentication\Delegated\1 = "mydomain.com"
Software\Policies\Mozilla\Firefox\Authentication\Delegated\2 = "https://myotherdomain.com"
Software\Policies\Mozilla\Firefox\Authentication\NTLM\1 = "mydomain.com"
Software\Policies\Mozilla\Firefox\Authentication\NTLM\2 = "https://myotherdomain.com"
Software\Policies\Mozilla\Firefox\Authentication\AllowNonFQDN\SPNEGO = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Authentication\AllowNonFQDN\NTLM = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Authentication\AllowProxies\SPNEGO = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Authentication\AllowProxies\NTLM = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Authentication\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Authentication\PrivateBrowsing = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_SPNEGO
```
Value (string):
```
<enabled/>
<data id="Authentication" value="1&#xF000;mydomain&#xF000;2&#xF000;https://myotherdomain.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_Delegated
```
Value (string):
```
<enabled/>
<data id="Authentication" value="1&#xF000;mydomain&#xF000;2&#xF000;https://myotherdomain.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_NTLM
```
Value (string):
```
<enabled/>
<data id="Authentication" value="1&#xF000;mydomain&#xF000;2&#xF000;https://myotherdomain.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_AllowNonFQDN
```
Value (string):
```
<enabled/>
<data id="Authentication_AllowNonFQDN_NTLM" value="true | false"/>
<data id="Authentication_AllowNonFQDN_SPNEGO" value="true | false"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_PrivateBrowsing
```
Value (string):
```
<enabled/> or <disabled/>
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
    <key>AllowProxies</key>
      <dict>
      <key>SPNEGO</key>
      <true/> | <false/>
      <key>NTLM</key>
      <true/> | <false/>
    </dict>
    <key>Locked</key>
    <true/> | <false/>
    <key>PrivateBrowsing</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### policies.json
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
      },
      "AllowProxies": {
        "SPNEGO": true | false,
        "NTLM": true | false
      },
      "Locked": true | false,
      "PrivateBrowsing": true | false
    }
  }
}
```
### BlockAboutAddons

Block access to the Add-ons Manager (about:addons).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableAddonsManager`\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\BlockAboutAddons = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutAddons
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>BlockAboutAddons</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\BlockAboutConfig = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutConfig
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>BlockAboutConfig</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\BlockAboutProfiles = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutProfiles
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>BlockAboutProfiles</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\BlockAboutSupport = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutSupport
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>BlockAboutSupport</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Bookmarks\1\Title = "Example"
Software\Policies\Mozilla\Firefox\Bookmarks\1\URL = "https://example.com"
Software\Policies\Mozilla\Firefox\Bookmarks\1\Favicon = "https://example.com/favicon.ico"
Software\Policies\Mozilla\Firefox\Bookmarks\1\Placement = "toolbar" | "menu"
Software\Policies\Mozilla\Firefox\Bookmarks\1\Folder = "FolderName"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Bookmarks/Bookmark01
```
Value (string):
```
<enabled/>
<data id="BookmarkTitle" value="Example"/>
<data id="BookmarkURL" value="https://example.com"/>
<data id="BookmarkFavicon" value="https://example.com/favicon.ico"/>
<data id="BookmarkPlacement" value="toolbar | menu"/>
<data id="BookmarkFolder" value="FolderName"/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\CaptivePortal = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/CaptivePortal
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>CaptivePortal</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Certificates\ImportEnterpriseRoots = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Certificates/Certificates_ImportEnterpriseRoots
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Certificates\Install\1 = "cert1.der"
Software\Policies\Mozilla\Firefox\Certificates\Install\2 = "C:\Users\username\cert2.pem"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Certificates/Certificates_Install
```
Value (string):
```
<enabled/>
<data id="Certificates_Install" value="1&#xF000;cert1.der&#xF000;2&#xF000;C:\Users\username\cert2.pem"/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Cookies\Allow\1 = "https://example.com"
Software\Policies\Mozilla\Firefox\Cookies\Block\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Cookies\Default = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Cookies\AcceptThirdParty = "always" | "never" | "from-visited"
Software\Policies\Mozilla\Firefox\Cookies\ExpireAtSessionEnd = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Cookies\RejectTracker = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Cookies\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Allow
```
Value (string):
```
<enabled/>
<data id="Cookies_Allow" value="1&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Block
```
Value (string):
```
<enabled/>
<data id="Cookies_Block" value="1&#xF000;https://example.org"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Default
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_AcceptThirdParty
```
Value (string):
```
<enabled/>
<data id="Cookies_AcceptThirdParty" value="always | never | from-visited"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_ExpireAtSessionEnd
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_RejectTracker
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Locked
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
```
{
  "policies": {
    "Cookies": {
      "Allow": ["http://example.org/"],
      "Block": ["http://example.edu/"],
      "Default": true | false,
      "AcceptThirdParty": "always" | "never" | "from-visited",
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableSetDesktopBackground = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableSetDesktopBackground
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableSetDesktopBackground</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableMasterPasswordCreation = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableMasterPasswordCreation
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableMasterPasswordCreation</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableAppUpdate = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableAppUpdate
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableAppUpdate</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableBuiltinPDFViewer = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableBuiltinPDFViewer
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableBuiltinPDFViewer</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisableBuiltinPDFViewer": true | false
  }
}
```
### DisabledCiphers
Disable specific cryptographic ciphers.

**Compatibility:** Firefox 76, Firefox ESR 68.8\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_RSA_WITH_AES_128_CBC_SHA = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_RSA_WITH_AES_256_CBC_SHA = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisabledCiphers\TLS_RSA_WITH_3DES_EDE_CBC_SHA = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_DHE_RSA_WITH_AES_128_CBC_SHA
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_DHE_RSA_WITH_AES_256_CBC_SHA
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_AES_128_CBC_SHA
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_AES_256_CBC_SHA
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_3DES_EDE_CBC_SHA
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisabledCiphers</key>
    <dict>
      <key>TLS_DHE_RSA_WITH_AES_128_CBC_SHA</key>
      <true/> | <false/>
      <key>TLS_DHE_RSA_WITH_AES_256_CBC_SHA</key>
      <true/> | <false/>
      <key>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</key>
      <true/> | <false/>
      <key>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</key>
      <true/> | <false/>
      <key>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</key>
      <true/> | <false/>
      <key>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</key>
      <true/> | <false/>
      <key>TLS_RSA_WITH_AES_128_CBC_SHA</key>
      <true/> | <false/>
      <key>TLS_RSA_WITH_AES_256_CBC_SHA</key>
      <true/> | <false/>
      <key>TLS_RSA_WITH_3DES_EDE_CBC_SHA</key>
      <true/> | <false/>
    </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisabledCiphers" {
      "TLS_DHE_RSA_WITH_AES_128_CBC_SHA": true | false,
      "TLS_DHE_RSA_WITH_AES_256_CBC_SHA": true | false,
      "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA": true | false,
      "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA": true | false,
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256": true | false,
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256": true | false,
      "TLS_RSA_WITH_AES_128_CBC_SHA": true | false,
      "TLS_RSA_WITH_AES_256_CBC_SHA": true | false,
      "TLS_RSA_WITH_3DES_EDE_CBC_SHA": true | false
    }
  }
}
```
### DisableDefaultBrowserAgent
Prevent the default browser agent from taking any actions. Only applicable to Windows; other platforms don’t have the agent.

**Compatibility:** Firefox 75, Firefox ESR 68.7 (Windows only)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableDefaultBrowserAgent = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableDefaultBrowserAgent
```
Value (string):
```
<enabled/> or <disabled/>
```
#### policies.json
```
{
  "policies": {
    "DisableDefaultBrowserAgent": true | false
  }
}
```
### DisableDeveloperTools
Remove access to all developer tools.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeDeveloperTools`\
**Preferences Affected:** `devtools.policy.disabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableDeveloperTools = 0x1 | 0x0`
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableDeveloperTools
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableDeveloperTools</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableFeedbackCommands = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFeedbackCommands
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableFeedbackCommands</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableFirefoxScreenshots = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFirefoxScreenshots
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableFirefoxScreenshots</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableFirefoxAccounts = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFirefoxAccounts
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableFirefoxAccounts</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableFirefoxStudies = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFirefoxStudies
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableFirefoxStudies</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableForgetButton = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableForgetButton
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableForgetButton</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableFormHistory = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFormHistory
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableFormHistory</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisableFormHistory": true | false
  }
}
```
### DisablePasswordReveal
Do not allow passwords to be shown in saved logins

**Compatibility:** Firefox 71, Firefox ESR 68.3\
**CCK2 Equivalent:** N/A
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisablePasswordReveal = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisablePasswordReveal
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisablePasswordReveal</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisablePasswordReveal": true | false
  }
}
```
### DisablePocket
Remove Pocket in the Firefox UI. It does not remove it from the new tab page.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePocket`\
**Preferences Affected:** `extensions.pocket.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisablePocket = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisablePocket
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisablePocket</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisablePrivateBrowsing = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisablePrivateBrowsing
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisablePrivateBrowsing</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableProfileImport = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableProfileImport
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableProfileImport</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableProfileRefresh = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableProfileRefresh
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableProfileRefresh</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableSafeMode = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableSafeMode
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableSafeMode</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableSecurityBypass\InvalidCertificate = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DisableSecurityBypass\SafeBrowsing = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/P_DisableSecurityBypass_InvalidCertificate
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/P_DisableSecurityBypass_SafeBrowsing
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
```
{
  "policies": {
    "DisableSecurityBypass": {
      "InvalidCertificate": true | false,
      "SafeBrowsing": true | false
    }
  }
}
```
### DisableSystemAddonUpdate
Prevent system add-ons from being installed or update.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableSystemAddonUpdate = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableSystemAddonUpdate
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableSystemAddonUpdate</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableTelemetry = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableTelemetry
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableTelemetry</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisplayBookmarksToolbar = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisplayBookmarksToolbar
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisplayBookmarksToolbar</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisplayBookmarksToolbar": true | false
  }
}
```
### DisplayMenuBar (Deprecated)
Set the initial state of the menubar. A user can still hide it and it will stay hidden.

**Compatibility:** Firefox 60, Firefox ESR 60 (Windows, some Linux)\
**CCK2 Equivalent:** `displayMenuBar`\
**Preferences Affected:** N/A

#### Windows (GPO)
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
#### policies.json
```
{
  "policies": {
    "DisplayMenuBar": true | false
  }
}
```
### DisplayMenuBar
Set the state of the menubar.

`always` means the menubar is shown and cannot be hidden.

`never` means the menubar is hidden and cannot be shown.

`default-on` means the menubar is on by default but can be hidden.

`default-off` means the menubar is off by default but can be shown.

**Compatibility:** Firefox 73, Firefox ESR 68.5 (Windows, some Linux)\
**CCK2 Equivalent:** `displayMenuBar`\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisplayMenuBar = "always", "never", "default-on", "default-off"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisplayMenuBar_Enum
```
Value (string):
```
<enabled/>
<data id="DisplayMenuBar" value="always | never | default-on | default-off"/>
```
#### macOS
```
<dict>
  <key>DisplayMenuBar</key>
  <string>always | never | default-on | default-off</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisplayMenuBar": "always", "never", "default-on", "default-off"
  }
}
```
### DNSOverHTTPS
Configure DNS over HTTPS.

`Enabled` determines whether DNS over HTTPS is enabled

`ProviderURL` is a URL to another provider.

`Locked` prevents the user from changing DNS over HTTPS preferences.

`ExcludedDomains` excludes domains from DNS over HTTPS.

**Compatibility:** Firefox 63, Firefox ESR 68 (ExcludedDomains added in 75/68.7)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.trr.mode`,`network.trr.uri`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\ProviderURL = "URL_TO_ALTERNATE_PROVIDER"
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\ExcludedDomains\1 = "example.com"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_Enabled
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_ProviderURL
```
Value (string):
```
<enabled/>
<data id="String" value="URL_TO_ALTERNATE_PROVIDER"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_ExcludedDomains
```
Value (string):
```
<enabled/>
<data id="List" value="1&#xF000;example.com"/>
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
    <key>ExcludedDomains</key>
    <array>
      <string>example.com</string>
    </array>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DNSOverHTTPS": {
      "Enabled":  true | false,
      "ProviderURL": "URL_TO_ALTERNATE_PROVIDER",
      "Locked": true | false,
      "ExcludedDomains": ["example.com"]
    }
  }
}
```
### DontCheckDefaultBrowser
Don't check if Firefox is the default browser at startup.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontCheckDefaultBrowser`\
**Preferences Affected:** `browser.shell.checkDefaultBrowser`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DontCheckDefaultBrowser = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DontCheckDefaultBrowser
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DontCheckDefaultBrowser</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DefaultDownloadDirectory = "${home}\Downloads"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DefaultDownloadDirectory
```
Value (string):
```
<enabled/>
<data id="Preferences_String" value="${home}\Downloads"/>
```
#### macOS
```
<dict>
  <key>DefaultDownloadDirectory</key>
  <string>${home}/Downloads</string>
</dict>
```
#### policies.json (macOS and Linux)
```
{
  "policies": {
    "DefaultDownloadDirectory": "${home}/Downloads"
}
```
#### policies.json (Windows)
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DownloadDirectory = "${home}\Downloads"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DownloadDirectory
```
Value (string):
```
<enabled/>
<data id="Preferences_String" value="${home}\Downloads"/>
```
#### macOS
```
<dict>
  <key>DownloadDirectory</key>
  <string>${home}/Downloads</string>
</dict>
```
#### policies.json (macOS and Linux)
```
{
  "policies": {
    "DownloadDirectory": "${home}/Downloads"
}
```
#### policies.json (Windows)
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

If `Cryptomining` is set to true, cryptomining scripts on websites are blocked.

If `Fingerprinting` is set to true, fingerprinting scripts on websites are blocked.

`Exceptions` are origins for which tracking protection is not enabled.

**Compatibility:** Firefox 60, Firefox ESR 60 (Cryptomining and Fingerprinting added in 70/68.2, Exceptions added in 73/68.5)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.trackingprotection.enabled`,`privacy.trackingprotection.pbmode.enabled`,`privacy.trackingprotection.cryptomining.enabled`,`privacy.trackingprotection.fingerprinting.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Value = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Cryptomining = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Fingerprinting = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Exceptions\1 = "https://example.com"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/TrackingProtection
```
Value (string):
```
<enabled/>
<data id="TrackingProtectionLocked" value="true | false"/>
<data id="Cryptomining" value="true | false"/>
<data id="Fingerprinting" value="true | false"/>
<data id=TrackingProtection_Exceptions" value="1&#xF000;https://example.com"/>
```
#### macOS
```
<dict>
  <key>EnableTrackingProtection</key>
  <dict>
    <key>Value</key>
    <true/> | <false/>
    <key><Locked</key>
    <true/> | <false/>
    <key><Cryptomining</key>
    <true/> | <false/>
    <key><Fingerprinting</key>
    <true/> | <false/>
    <key>Exceptions</key>
    <array>
      <string>https://example.com</string>
    </array>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "EnableTrackingProtection": {
      "Value": true | false,
      "Locked": true | false,
      "Cryptomining": true | false,
      "Fingerprinting": true | false,
      "Exceptions": ["https://example.com"]
    }
}
```
### EncryptedMediaExtensions
Enable or disable Encrypted Media Extensions and optionally lock it.

If `Enabled` is set to false, encrypted media extensions (like Widevine) are not downloaded by Firefox unless the user consents to installing them.

If `Locked` is set to true and `Enabled` is set to false, Firefox will not download encrypted media extensions (like Widevine) or ask the user to install them.

**Compatibility:** Firefox 77, Firefox ESR 68.9\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `media.eme.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\EncryptedMediaExtensions\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EncryptedMediaExtensions\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~EncryptedMediaExtensions/EncryptedMediaExtensions_Enabled
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~EncryptedMediaExtensions/EncryptedMediaExtensions_Locked
```
Value (string):
```
<enabled/>or <disabled/>
```
#### macOS
```
<dict>
  <key>EncryptedMediaExtensions</key>
  <dict>
    <key>Enabled</key>
    <true/> | <false/>
    <key><Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "EncryptedMediaExtensions": {
      "Enabled": true | false,
      "Locked": true | false
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

#### Windows (GPO)
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
#### policies.json
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
| `install_url`| Maps to a URL indicating where Firefox can download a force_installed or normal_installed extension. If installing from the addons.mozilla.org, use the following URL (substituting SHORT_NAME from the URL on AMO), https://addons.mozilla.org/firefox/downloads/latest/SHORT_NAME/latest.xpi. If installing from the local file system, use a file:/// URL. Languages packs are available from https://releases.mozilla.org/pub/firefox/releases/VERSION/PLATFORM/xpi/LANGUAGE.xpi.
| `install_sources` | Each item in this list is an extension-style match pattern. Users will be able to easily install items from any URL that matches an item in this list. Both the location of the *.xpi file and the page where the download is started from (i.e.  the referrer) must be allowed by these patterns. This setting can be used only for the default configuration.
| `allowed_types` | This setting whitelists the allowed types of extension/apps that can be installed in Firefox. The value is a list of strings, each of which should be one of the following: "extension", "theme", "dictionary", "langpack" This setting can be used only for the default configuration.
| `blocked_install_message` | This maps to a string specifying the error message to display to users if they're blocked from installing an extension. This setting allows you to append text to the generic error message displayed when the extension is blocked. This could be be used to direct users to your help desk, explain why a particular extension is blocked, or something else.

**Compatibility:** Firefox 69, Firefox ESR 68.1\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\ExtensionSettings (REG_MULTI_SZ) =
{
  "*": {
    "blocked_install_message": "Custom error message.",
    "install_sources": ["https://addons.mozilla.org/"],
    "installation_mode": "blocked",
    "allowed_types": ["extension"]
  },
  "uBlock0@raymondhill.net": {
    "installation_mode": "force_installed",
    "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"
  }
}
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionSettings
```
Value (string):
```
<enabled/>
<data id="ExtensionSettings" value='
  "*": {
      "blocked_install_message": "Custom error message.",
      "install_sources": ["https://addons.mozilla.org/"],
      "installation_mode": "blocked",
      "allowed_types": ["extension"]
    },
    "uBlock0@raymondhill.net": {
      "installation_mode": "force_installed",
      "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"
    }'/>
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
      <key>allowed_types</key>
      <array>
        <string>extension</string>
      </array>
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
#### policies.json
```
{
  "policies": {
    "ExtensionSettings": {
      "*": {
        "blocked_install_message": "Custom error message.",
        "install_sources": ["https://addons.mozilla.org/"],
        "installation_mode": "blocked",
        "allowed_types": ["extension"]
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\ExtensionUpdate = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ExtensionUpdate
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>ExtensionUpdate</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\FlashPlugin\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\FlashPlugin\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\FlashPlugin\Default = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FlashPlugin\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Default
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\FirefoxHome\Search = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\TopSites = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Highlights = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Pocket = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Snippets = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/CustomizeFirefoxHome
```
Value (string):
```
<enabled/>
<data id="FirefoxHome_Search"  value="true | false"/>
<data id="FirefoxHome_TopSites"  value="true | false"/>
<data id="FirefoxHome_Highlights"  value="true | false"/>
<data id="FirefoxHome_Pocket"  value="true | false"/>
<data id="FirefoxHome_Snippets"  value="true | false"/>
<data id="FirefoxHome_Locked"  value="true | false"/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\HardwareAcceleration = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HardwareAcceleration
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>HardwareAcceleration</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Homepage\URL = "https://example.com"
Software\Policies\Mozilla\Firefox\Homepage\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Homepage\Additional\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Homepage\Additional\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Homepage\StartPage = "none" | "homepage" |  "previous-session"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/HomepageURL
```
Value (string):
```
<enabled/>

<data id="HomepageURL" value="https://example.com"/>
<data id="HomepageLocked" value="true | false"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/HomepageAdditional
```
Value (string):
```
<enabled/>

<data id="HomepageAdditional" value="1&#xF000;http://example.org&#xF000;2&#xF000;http://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/HomepageStartPage
```
Value (string):
```
<enabled/>

<data id="StartPage" value="none | homepage | previous-session"/>
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
    <string>none | homepage | previous-session</string>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "Homepage": {
      "URL": "http://example.com/",
      "Locked": true | false,
      "Additional": ["http://example.org/",
                     "http://example.edu/"],
      "StartPage": "none" | "homepage" | "previous-session"
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\InstallAddonsPermission\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\InstallAddonsPermission\Allow\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\InstallAddonsPermission\Default = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Addons/InstallAddonsPermission_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Addons/InstallAddonsPermission_Default
```
Value (string):
```
<enabled/>
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
#### policies.json
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
### LegacyProfiles
Disable the feature enforcing a separate profile for each installation.

If this policy set to true, Firefox will not try to create different profiles for installations of Firefox in different directories. This is the equivalent of the MOZ_LEGACY_PROFILES environment variable.

If this policy set to false, Firefox will create a new profile for each unique installation of Firefox.

This policy only work on Windows via GPO (not policies.json).

**Compatibility:** Firefox 70, Firefox ESR 68.2 (Windows only, GPO only)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\LegacyProfiles = = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LegacyProfiles
```
Value (string):
```
<enabled/> or <disabled/>
```
### LocalFileLinks
Enable linking to local files by origin.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `capability.policy.localfilelinks.*`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\LocalFileLinks\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\LocalFileLinks\2 = "https://example.edu"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LocalFileLinks
```
Value (string):
```
<enabled/>
<data id="LocalFileLinks" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.edu"/>
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
#### policies.json
```
{
  "policies": {
    "LocalFileLinks": ["http://example.org/",
                       "http://example.edu/"]
  }
}
```
### NetworkPrediction
Enable or disable network prediction (DNS prefetching).

**Compatibility:** Firefox 67, Firefox ESR 60.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.dns.disablePrefetch`,`network.dns.disablePrefetchFromHTTPS`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\NetworkPrediction = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/NetworkPrediction
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>NetworkPrediction</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\NewTabPage = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/NewTabPage
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>NewTabPage</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "NewTabPage": true | false
}
```
### NoDefaultBookmarks
Disable the creation of default bookmarks.

This policy is only effective if the user profile has not been created yet.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `removeDefaultBookmarks`\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\NoDefaultBookmarks = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/NoDefaultBookmarks
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>NoDefaultBookmarks</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "NoDefaultBookmarks": true | false
  }
}
```
### OfferToSaveLogins
Control whether or not Firefox offers to save passwords.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `dontRememberPasswords`\
**Preferences Affected:** `signon.rememberSignons`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\OfferToSaveLogins = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OfferToSaveLogins
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>OfferToSaveLogins</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "OfferToSaveLogins": true | false
  }
}
```
### OfferToSaveLoginsDefault
Sets the default value of signon.rememberSignons without locking it.

**Compatibility:** Firefox 70, Firefox ESR 60.2\
**CCK2 Equivalent:** `dontRememberPasswords`\
**Preferences Affected:** `signon.rememberSignons`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\OfferToSaveLoginsDefault = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OfferToSaveLoginsDefault
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>OfferToSaveLoginsDefault</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "OfferToSaveLoginsDefault": true | false
  }
}
```
### OverrideFirstRunPage
Override the first run page. If the value is blank, no first run page is displayed.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `welcomePage`,`noWelcomePage`\
**Preferences Affected:** `startup.homepage_welcome_url`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\OverrideFirstRunPage = "http://example.org"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OverrideFirstRunPage
```
Value (string):
```
<enabled/>
<data id="OverridePage" value="https://example.com"/>
```
#### macOS
```
<dict>
  <key>OverrideFirstRunPage</key>
  <string>http://example.org</string>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\OverridePostUpdatePage = "http://example.org"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OverridePostUpdatePage
```
Value (string):
```
<enabled/>
<data id="OverridePage" value="https://example.com"/>
```
#### macOS
```
<dict>
  <key>OverridePostUpdatePage</key>
  <string>http://example.org</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "OverridePostUpdatePage": "http://example.org"
}
```
### PasswordManagerEnabled
Remove access to the password manager via preferences and blocks about:logins on Firefox 70.

**Compatibility:** Firefox 70, Firefox ESR 60.2\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `pref.privacy.disable_button.view_passwords`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PasswordManagerEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PasswordManagerEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>PasswordManagerEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PasswordManagerEnabled": true | false
  }
}
```
### Permissions
Set permissions associated with camera, microphone, location, notifications, and autoplay. Because these are origins, not domains, entries with unique ports must be specified separately. See examples below.

`Allow` is a list of origins where the feature is allowed.

`Block` is a list of origins where the feature is not allowed.

`BlockNewRequests` determines whether or not new requests can be made for the feature.

`Locked` prevents the user from changing preferences for the feature.

`Default` specifies the default value for Autoplay. block-audio-video is not supported on Firefox ESR 68.

**Compatibility:** Firefox 62, Firefox ESR 60.2 (Autoplay added in Firefox 74, Firefox ESR 68.6, Autoplay Default/Locked added in Firefox 76, Firefox ESR 68.8)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `permissions.default.camera`,`permissions.default.microphone`,`permissions.default.geo`,`permissions.default.desktop-notification`,`media.autoplay.default`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Permissions\Camera\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Camera\Allow\2 = "https://example.org:1234"
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
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Default = "allow-audio-video" | "block-audio" | "block-audio-video"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_BlockNewRequests
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_BlockNewRequests
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Default
```
Value (string):
```
<enabled/>
<data id="Autoplay_Default" value="allow-audio-video | block-audio | block-audio-video"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Locked
```
Value (string):
```
<enabled/> or <disabled/>
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
        <string>https://example.org:1234</string>
      </array>
      <key>Block</key>
      <array>
        <string>https://example.edu</string>
      </array>
      <key>BlockNewRequests</key>
      <true/> | <false/>
      <key>Locked</key>
      <true/> | <false/>
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
      <true/> | <false/>
      <key>Locked</key>
      <true/> | <false/>
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
      <true/> | <false/>
      <key>Locked</key>
      <true/> | <false/>
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
    <key>Autoplay</key>
    <dict>
      <key>Allow</key>
      <array>
        <string>https://example.org</string>
      </array>
      <key>Block</key>
      <array>
        <string>https://example.edu</string>
      </array>
      <key>Default</key>
      <string>allow-audio-video | block-audio | block-audio-video</string>
      <key>Locked</key>
      <true/> | <false/>
    </dict>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "Permissions": {
      "Camera": {
        "Allow": ["https://example.org","https://example.org:1234"],
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
      },
      "Autoplay": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "Default": "allow-audio-video" | "block-audio" | "block-audio-video",
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PopupBlocking\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\PopupBlocking\Allow\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\PopupBlocking\Default = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\PopupBlocking\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Popups/PopupBlocking_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Popups/PopupBlocking_Default
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Popups/PopupBlocking_Locked
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
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

| Preference | Type | Compatibility | Default
| --- | --- | --- | ---
| accessibility.force_disabled | integer | Firefox 70, Firefox ESR 68.2 | 0
| &nbsp;&nbsp;&nbsp;&nbsp;If set to 1, platform accessibility is disabled.
| app.update.auto (Deprecated - Switch to AppAutoUpdate policy) | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, Firefox doesn't automatically install update.
| browser.bookmarks.autoExportHTML | boolean | Firefox 70, Firefox ESR 68.2 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, bookmarks are exported on shutdown.
| browser.bookmarks.file | string | Firefox 70, Firefox ESR 68.2 | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If set, the name of the file where bookmarks are exported and imported.
| browser.bookmarks.restore_default_bookmarks | boolean | Firefox 70, Firefox ESR 68.2 | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If true, bookmarks are restored to their defaults.
| browser.cache.disk.enable | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, don't store cache on the hard drive.
| ~browser.cache.disk.parent_directory~ | string | Firefox 68, Firefox ESR 68 | Profile temporary directory
| &nbsp;&nbsp;&nbsp;&nbsp;~If set, changes the location of the disk cache.~ This policy doesn't work. It's being worked on.
| browser.fixup.dns_first_for_single_words | boolean | Firefox 68, Firefox ESR 68 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, single words are sent to DNS, not directly to search.
| browser.newtabpage.activity-stream.default.sites | string | Firefox 72, ESR 68.4 | Locale dependent
| &nbsp;&nbsp;&nbsp;&nbsp;If set, a list of URLs to use as the default top sites on the new tab page.
| browser.places.importBookmarksHTML | boolean | Firefox 70, Firefox ESR 68.2
| &nbsp;&nbsp;&nbsp;&nbsp;If true, bookmarks are always imported on startup.
| browser.safebrowsing.phishing.enabled | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, phishing protection is not enabled (Not recommended)
| browser.safebrowsing.malware.enabled | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, malware protection is not enabled (Not recommended)
| browser.search.update | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, updates for search engines are not checked.
| browser.slowStartup.notificationDisabled | boolean | Firefox 70, Firefox ESR 68.2 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, a notification isn't shown if startup is slow.
| browser.tabs.warnOnClose | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, there is no warning when the browser is closed.
| browser.taskbar.previews.enable | boolean | Firefox 70, Firefox ESR 68.2 (Windows only) | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, tab previews are shown in the Windows taskbar.
| browser.urlbar.suggest.bookmark | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, bookmarks aren't suggested when typing in the URL bar.
| browser.urlbar.suggest.history | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, history isn't suggested when typing in the URL bar.
| browser.urlbar.suggest.openpage | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, open tabs aren't suggested when typing in the URL bar.
| datareporting.policy.dataSubmissionPolicyBypassNotification | boolean | Firefox 68, Firefox ESR 68 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, don't show the privacy policy tab on first run.
| dom.allow_scripts_to_close_windows | boolean | Firefox 70, Firefox ESR 68.2 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If false, web page can close windows.
| dom.disable_window_flip | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, web pages can focus and activate windows.
| dom.disable_window_move_resize | boolean | Firefox 68, Firefox ESR 68 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, web pages can't move or resize windows.
| dom.event.contextmenu.enabled | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, web pages can't override context menus.
| dom.keyboardevent.keypress.hack.dispatch_non_printable_keys.addl | string | Firefox 68, Firefox ESR 68 | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;See https://support.mozilla.org/en-US/kb/dom-events-changes-introduced-firefox-66
| dom.keyboardevent.keypress.hack.use_legacy_keycode_and_charcode.addl | string | Firefox 68, Firefox ESR 68 | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;See https://support.mozilla.org/en-US/kb/dom-events-changes-introduced-firefox-66
| dom.xmldocument.load.enabled | boolean | Firefox ESR 68.5 | true.
| &nbsp;&nbsp;&nbsp;&nbsp;If false, XMLDocument.load is not available.
| dom.xmldocument.async.enabled | boolean | Firefox ESR 68.5 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, XMLDocument.async is not available.
| extensions.blocklist.enabled | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the extensions blocklist is not used (Not recommended)
| extensions.getAddons.showPane | boolean | Firefox 68, Firefox ESR 68 | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the Recommendations tab is not displayed in the Add-ons Manager.
| extensions.htmlaboutaddons.recommendations.enabled | boolean | Firefox 72, Firefox ESR 68.4 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, recommendations are not shown on the Extensions tab in the Add-ons Manager.
| geo.enabled | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the geolocation API is disabled. | Language dependent
| intl.accept_languages | string | Firefox 70, Firefox ESR 68.2
| &nbsp;&nbsp;&nbsp;&nbsp;If set, preferred language for web pages.
| media.eme.enabled (Deprecated - Switch to EncryptedMediaExtensions policy) | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, Encrypted Media Extensions are not enabled.
| media.gmp-gmpopenh264.enabled | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the OpenH264  plugin is not downloaded.
| media.gmp-widevinecdm.enabled | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the Widevine plugin is not downloaded.
| media.peerconnection.enabled | boolean | Firefox 72, Firefox ESR 68.4 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, WebRTC is disabled
| media.peerconnection.ice.obfuscate_host_addresses.whitelist | string | Firefox 72, Firefox ESR 68.4 | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If set, a list of domains for which mDNS hostname obfuscation is
disabled
| network.dns.disableIPv6 | boolean | Firefox 68, Firefox ESR 68 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, IPv6 DNS lokoups are disabled.
| network.IDN_show_punycode | boolean | Firefox 68, Firefox ESR 68 | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, display the punycode version of internationalized domain names. 
| places.history.enabled | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, history is not enabled.
| print.save_print_settings | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, print settings are not saved between jobs.
| security.default_personal_cert | string | Firefox 68, Firefox ESR 68 | Ask Every Time
| &nbsp;&nbsp;&nbsp;&nbsp;If set to Select Automatically, Firefox automatically chooses the default personal certificate.
| security.mixed_content.block_active_content | boolean | Firefox 70, Firefox ESR 68.2 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, mixed active content (HTTP and HTTPS) is not blocked.
| security.osclientcerts.autoload | boolean | Firefox 72 (Windows), Firefox 75 (macOS)  | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, client certificates are loaded from the operating system certificate store.
| security.ssl.errorReporting.enabled | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, SSL errors cannot be sent to Mozilla.
| security.tls.hello_downgrade_check | boolean | Firefox 72, Firefox ESR 68.4 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the TLS 1.3 downgrade check is disabled.
| ui.key.menuAccessKeyFocuses | boolean | Firefox 68, Firefox ESR 68 | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the Alt key doesn't show the menubar on Windows.
| widget.content.gtk-theme-override | string | Firefox 72, Firefox ESR 68.4 (Linux only) | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If set, overrides the GTK theme for widgets.
#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Preferences\boolean_preference_name = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Preferences\string_preference_name = "string_value"
```
#### Windows (Intune)
OMA-URI: (periods are replaced by underscores)
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Preferences/boolean_preference_name
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
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
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.download.useDownloadDir`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PromptForDownloadLocation = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PromptForDownloadLocation
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>PromptForDownloadLocation</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
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
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Proxy
```
Value (string):
```
<enabled/>
<data id="ProxyLocked" value="true | false"/>
<data id="ConnectionType" value="none | system | manual | autoDetect | autoConfig"/>
<data id="HTTPProxy" value="https://httpproxy.example.com"/>
<data id="UseHTTPProxyForAllProtocols" value="true | false"/>
<data id="SSLProxy" value="https://sslproxy.example.com"/>
<data id="FTPProxy" value="https://ftpproxy.example.com"/>
<data id="SOCKSProxy" value="https://socksproxy.example.com"/>
<data id="SOCKSVersion" value="4 | 5"/>
<data id="AutoConfigURL" value="URL_TO_AUTOCONFIG"/>
<data id="Passthrough" value="<local>"/>
<data id="AutoLogin" value="true | false"/>
<data id="UseProxyForDNS" value="true | false"/>
```
#### macOS
```
<dict>
  <key>Proxy</key>
  <dict>
    <key>Mode</key>
    <string>none | system | manual | autoDetect | autoConfig</string>
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
#### policies.json
```
{
  "policies": {
    "Proxy": {
      "Mode": "none", "system", "manual", "autoDetect", "autoConfig",
      "Locked": true | false,
      "HTTPProxy": "hostname",
      "UseHTTPProxyForAllProtocols": true | false,
      "SSLProxy": "hostname",
      "FTPProxy": "hostname",
      "SOCKSProxy": "hostname",
      "SOCKSVersion": 4 | 5
      "Passthrough": "<local>",
      "AutoConfigURL": "URL_TO_AUTOCONFIG",
      "AutoLogin": true | false,
      "UseProxyForDNS": true | false
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
#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\RequestedLocales\1 = "de"
Software\Policies\Mozilla\Firefox\RequestedLocales\2 = "en-US"

or

Software\Policies\Mozilla\Firefox\RequestedLocales = "de,en-US"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/RequestedLocalesString
```
Value (string):
```
<enabled/>
<data id="Preferences_String" value="de,en-US"/>
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
#### policies.json
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
<a name="SanitizeOnShutdown"></a>

### SanitizeOnShutdown (Selective)
Clear data on shutdown. Choose from Cache, Cookies, Download History, Form & Search History, Browsing History, Active Logins, Site Preferences and Offline Website Data.

Previously, these values were always locked. Starting with Firefox 74 and Firefox ESR 68.6, you can use the `Locked` option to either keep the values unlocked (set it to false), or lock only the values you set (set it to true). If you want the old behavior of locking everything, do not set `Locked` at all.

**Compatibility:** Firefox 68, Firefox ESR 68 (Locked added in 74/68.6)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown`,`privacy.clearOnShutdown.cache`,`privacy.clearOnShutdown.cookies`,`privacy.clearOnShutdown.downloads`,`privacy.clearOnShutdown.formdata`,`privacy.clearOnShutdown.history`,`privacy.clearOnShutdown.sessions`,`privacy.clearOnShutdown.siteSettings`,`privacy.clearOnShutdown.offlineApps`
#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Cache = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Cookies = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Downloads = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\FormData = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\History = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Sessions = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\SiteSettings = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\OfflineApps = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/I_SanitizeOnShutdown_Locked
```
Value (string):
```
<enabled/> or <disabled/>
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
    <key>Locked</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### policies.json
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
      "OfflineApps": true | false,
      "Locked": true | false
    }
  }
}
```
### SanitizeOnShutdown (All)
Clear all data on shutdown, including Browsing & Download History, Cookies, Active Logins, Cache, Form & Search History, Site Preferences and Offline Website Data.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown`,`privacy.clearOnShutdown.cache`,`privacy.clearOnShutdown.cookies`,`privacy.clearOnShutdown.downloads`,`privacy.clearOnShutdown.formdata`,`privacy.clearOnShutdown.history`,`privacy.clearOnShutdown.sessions`,`privacy.clearOnShutdown.siteSettings`,`privacy.clearOnShutdown.offlineApps`
#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/C_SanitizeOnShutdown
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>SanitizeOnShutdown</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SearchBar = "unified" | "separate"
```

#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SearchBar
```
Value (string):
```
<enabled/>
<data id="Permissions" value="unified | separate"/>
#### macOS
```
<dict>
  <key>SearchBar</key>
  <string>unified | separate</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "SearchBar": "unified" | "separate"
  }
}
```
<a name="SearchEngines"></a>

### SearchEngines (This policy is only available on the ESR.)

### SearchEngines | Default

Set the default search engine. This policy is only available on the ESR.

**Compatibility:** Firefox ESR 60\
**CCK2 Equivalent:** `defaultSearchEngine`\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SearchEngines\Default = NAME_OF_SEARCH_ENGINE
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_Default
```
Value (string):
```
<enabled/>
<data id="SearchEngines_Default" value="NAME_OF_SEARCH_ENGINE"/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SearchEngines\PreventInstalls = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_PreventInstalls
```
Value (string):
```
<enabled/> or <disabled/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SearchEngines\Remove\1 = NAME_OF_SEARCH_ENGINE
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_Remove
```
Value (string):
```
<enabled/>
<data id="SearchEngines_Remove" value="1&#xF000;NAME_OF_SEARCH_ENGINE"/>
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
#### policies.json
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

#### Windows (GPO)
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
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_1
```
Value (string):
```
<enabled/>
<data id="SearchEngine_Name" value="Example1"/>
<data id="SearchEngine_URLTemplate" value="https://www.example.org/q={searchTerms"/>
<data id="SearchEngine_Method" value="GET | POST"/>
<data id="SearchEngine_IconURL" value="https://www.example.org/favicon.ico"/>
<data id="SearchEngine_Alias" value="example"/>
<data id="SearchEngine_Description" value="Example Description"/>
<data id="SearchEngine_SuggestURLTemplate" value="https://www.example.org/suggestions/q={searchTerms}"/>
<data id="SearchEngine_PostData" value="name=value&amp;q={searchTerms}"/>
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
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SearchSuggestEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SearchSuggestEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>SearchSuggestEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SecurityDevices\NAME_OF_DEVICE = PATH_TO_LIBRARY_FOR_DEVICE
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SecurityDevices
```
Value (string):
```
<enabled/>
<data id="SecurityDevices" value="NAME_OF_DEVICE&#xF000;PATH_TO_LIBRARY_FOR_DEVICE"/>
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

#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SSLVersionMax = "tls1" | "tls1.1" | "tls1.2" | "tls1.3"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SSLVersionMax
```
Value (string):
```
<enabled/>
<data id="SSLVersion" value="tls1 | tls1.2 | tls1.3"/>
```
#### macOS
```
<dict>
  <key>SSLVersionMax</key>
  <string>tls1 | tls1.1 | tls1.2 | tls1.3</string>
</dict>
```

#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SSLVersionMin = "tls1" | "tls1.1" | "tls1.2" | "tls1.3"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SSLVersionMin
```
Value (string):
```
<enabled/>
<data id="SSLVersion" value="tls1 | tls1.2 | tls1.3"/>
```
#### macOS
```
<dict>
  <key>SSLVersionMin</key>
  <string>tls1 | tls1.1 | tls1.2 | tls1.3</string>
</dict>
```

#### policies.json
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

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SupportMenu\Title = "Support Menu"
Software\Policies\Mozilla\Firefox\SupportMenu\URL = "http://example.com/support"
Software\Policies\Mozilla\Firefox\SupportMenu\AccessKey = "S"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SupportMenu
```
Value (string):
```
<enabled/>
<data id="SupportMenuTitle" value="Support Menu"/>
<data id="SupportMenuURL" value="http://example.com/support"/>
<data id="SupportMenuAccessKey" value="S">
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
#### policies.json
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
### UserMessaging

Prevent installing search engines from webpages.

`WhatsNew` Remove the "What's New" icon and menuitem. (Firefox 75 only)

`ExtensionRecommendations` Don't recommend extensions.

`FeatureRecommendations` Don't recommend browser features.

`UrlbarInterventions` Don't offer Firefox specific suggestions in the URL bar. (Firefox 75 only)

**Compatibility:** Firefox 75, Firefox ESR 68.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.messaging-system.whatsNewPanel.enabled`,`browser.newtabpage.activity-stream.asrouter.userprefs.cfr.addons`,`browser.newtabpage.activity-stream.asrouter.userprefs.cfr.features`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\UserMessaging\WhatsNew = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\ExtensionRecommendations = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\FeatureRecommendations = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\UrlbarInterventions = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/UserMessaging_WhatsNew
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/UserMessaging_ExtensionRecommendations
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/UserMessaging_FeatureRecommendations
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/UserMessaging_UrlbarInterventions
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>UserMessaging</key>
  <dict>
    <key>WhatsNew</key>
    <true/> | <false/>
    <key>ExtensionRecommendations</key>
    <true/> | <false/>
    <key>FeatureRecommendations</key>
    <true/> | <false/>
    <key>UrlbarInterventions</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "UserMessaging": {
      "WhatsNew": true | false,
      "ExtensionRecommendations": true | false,
      "FeatureRecommendations": true | false,
      "UrlbarInterventions": true | false
    }
  }
}
```
### WebsiteFilter
Block websites from being visited. The parameters take an array of Match Patterns, as documented in https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Match_patterns. Only http/https addresses are supported at the moment. The arrays are limited to 1000 entries each.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\WebsiteFilter\Block\1 = "<all_urls>"
Software\Policies\Mozilla\Firefox\WebsiteFilter\Exceptions\1 = "http://example.org/*"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/B_WebsiteFilter_Block
```
Value (string):
```
<enabled/>
<data id="WebsiteFilter" value="1&#xF000;<all_urls>"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/B_WebsiteFilter_Exceptions
```
Value (string):
```
<enabled/>
<data id="WebsiteFilter" value="1&#xF000;http://example.org/*"/>
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
#### policies.json
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
