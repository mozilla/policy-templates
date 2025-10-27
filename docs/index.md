Firefox policies can be specified using the [Group Policy templates on Windows](https://github.com/mozilla/policy-templates/tree/master/windows), [Intune on Windows](https://support.mozilla.org/kb/managing-firefox-intune), [configuration profiles on macOS](https://github.com/mozilla/policy-templates/tree/master/mac), or by creating a file called `policies.json`. On Windows, create a directory called `distribution` where the EXE is located and place the file there. On Mac, the file goes into `Firefox.app/Contents/Resources/distribution`.  On Linux, the file goes into `firefox/distribution`, where `firefox` is the installation directory for firefox, which varies by distribution or you can specify system-wide policy by placing the file in `/etc/firefox/policies`.

Unfortunately, JSON files do not support comments, but you can add extra entries to the JSON to use as comments. You will see an error in about:policies, but the policies will still work properly. For example:
```
{
  "policies": {
    "Authentication": {
      "SPNEGO": ["mydomain.com", "https://myotherdomain.com"]
    }
    "Authentication_Comment": "These domains are required for us"
  }
}
```
Note: The `policies.json` must use the UTF-8 encoding.

| Policy Name | Description
| --- | --- |
| **[`3rdparty`](#3rdparty)** | Set policies that WebExtensions can access via chrome.storage.managed.
| **[`AllowedDomainsForApps`](#alloweddomainsforapps)** | Define domains allowed to access Google Workspace.
| **[`AllowFileSelectionDialogs`](#allowfileselectiondialogs)** | Allow file selection dialogs.
| **[`AppAutoUpdate`](#appautoupdate)** | Enable or disable automatic application update.
| **[`AppUpdatePin`](#appupdatepin)** | Prevent Firefox from being updated beyond the specified version.
| **[`AppUpdateURL`](#appupdateurl)** | Change the URL for application update.
| **[`Authentication`](#authentication)** | Configure sites that support integrated authentication.
| **[`AutofillAddressEnabled`](#autofilladdressenabled)** | Enable autofill for addresses.
| **[`AutofillCreditCardEnabled`](#autofillcreditcardenabled)** | Enable autofill for payment methods.
| **[`AutoLaunchProtocolsFromOrigins`](#autolaunchprotocolsfromorigins)** | Define a list of external protocols that can be used from listed origins without prompting the user.
| **[`BackgroundAppUpdate`](#backgroundappupdate)** | Enable or disable the background updater (Windows only).
| **[`BlockAboutAddons`](#blockaboutaddons)** | Block access to the Add-ons Manager (about:addons).
| **[`BlockAboutConfig`](#blockaboutconfig)** | Block access to about:config.
| **[`BlockAboutProfiles`](#blockaboutprofiles)** | Block access to About Profiles (about:profiles).
| **[`BlockAboutSupport`](#blockaboutsupport)** | Block access to Troubleshooting Information (about:support).
| **[`Bookmarks`](#bookmarks)** | Add bookmarks in either the bookmarks toolbar or menu.
| **[`CaptivePortal`](#captiveportal)** | Enable or disable the detection of captive portals.
| **[`Certificates`](#certificates)** |
| **[`Certificates -> ImportEnterpriseRoots`](#certificates--importenterpriseroots)** | Trust certificates that have been added to the operating system certificate store by a user or administrator.
| **[`Certificates -> Install`](#certificates--install)** | Install certificates into the Firefox certificate store.
| **[`Containers`](#containers)** | Set policies related to [containers](https://addons.mozilla.org/firefox/addon/multi-account-containers/).
| **[`ContentAnalysis`](#contentanalysis)** | Configure Firefox to use an agent for Data Loss Prevention (DLP) that is compatible with the [Google Chrome Content Analysis Connector Agent SDK](https://github.com/chromium/content_analysis_sdk).
| **[`Cookies`](#cookies)** | Configure cookie preferences.
| **[`DefaultDownloadDirectory`](#defaultdownloaddirectory)** | Set the default download directory.
| **[`DisableAppUpdate`](#disableappupdate)** | Turn off application updates.
| **[`DisableBuiltinPDFViewer`](#disablebuiltinpdfviewer)** | Disable the built in PDF viewer.
| **[`DisabledCiphers`](#disabledciphers)** | Disable ciphers.
| **[`DisableDefaultBrowserAgent`](#disabledefaultbrowseragent)** | Prevent the default browser agent from taking any actions (Windows only).
| **[`DisableDeveloperTools`](#disabledevelopertools)** | Remove access to all developer tools.
| **[`DisableEncryptedClientHello`](#disableencryptedclienthello)** | Disable the TLS Feature Encrypted Client Hello (ECH).
| **[`DisableFeedbackCommands`](#disablefeedbackcommands)** | Disable the menus for reporting sites.
| **[`DisableFirefoxAccounts`](#disablefirefoxaccounts)** | Disable Firefox Accounts integration (Sync).
| **[`DisableFirefoxScreenshots`](#disablefirefoxscreenshots)** | Remove access to Firefox Screenshots.
| **[`DisableFirefoxStudies`](#disablefirefoxstudies)** | Disable Firefox studies (Shield).
| **[`DisableForgetButton`](#disableforgetbutton)** | Disable the "Forget" button.
| **[`DisableFormHistory`](#disableformhistory)** | Turn off saving information on web forms and the search bar.
| **[`DisableMasterPasswordCreation`](#disablemasterpasswordcreation)** | Remove the master password functionality.
| **[`DisablePasswordReveal`](#disablepasswordreveal)** | Do not allow passwords to be revealed in saved logins.
| **[`DisablePocket`](#disablepocket-deprecated)** | Remove Pocket in the Firefox UI.
| **[`DisablePrivateBrowsing`](#disableprivatebrowsing)** | Remove access to private browsing.
| **[`DisableProfileImport`](#disableprofileimport)** | Disables the "Import data from another browser" option in the bookmarks window.
| **[`DisableProfileRefresh`](#disableprofilerefresh)** | Disable the Refresh Firefox button on about:support and support.mozilla.org
| **[`DisableSafeMode`](#disablesafemode)** | Disable safe mode within the browser.
| **[`DisableSecurityBypass`](#disablesecuritybypass)** | Prevent the user from bypassing security in certain cases.
| **[`DisableSetDesktopBackground`](#disablesetdesktopbackground)** | Remove the "Set As Desktop Background..." menuitem when right clicking on an image.
| **[`DisableSystemAddonUpdate`](#disablesystemaddonupdate)** | Prevent system add-ons from being installed or updated.
| **[`DisableTelemetry`](#disabletelemetry)** | DisableTelemetry
| **[`DisableThirdPartyModuleBlocking`](#disablethirdpartymoduleblocking)** | Do not allow blocking third-party modules.
| **[`DisplayBookmarksToolbar`](#displaybookmarkstoolbar)** | Set the initial state of the bookmarks toolbar.
| **[`DisplayMenuBar`](#displaymenubar)** | Set the state of the menubar.
| **[`DNSOverHTTPS`](#dnsoverhttps)** | Configure DNS over HTTPS.
| **[`DontCheckDefaultBrowser`](#dontcheckdefaultbrowser)** | Don't check if Firefox is the default browser at startup.
| **[`DownloadDirectory`](#downloaddirectory)** | Set and lock the download directory.
| **[`EnableTrackingProtection`](#enabletrackingprotection)** | Configure tracking protection.
| **[`EncryptedMediaExtensions`](#encryptedmediaextensions)** | Enable or disable Encrypted Media Extensions and optionally lock it.
| **[`EnterprisePoliciesEnabled`](#enterprisepoliciesenabled)** | Enable policy support on macOS.
| **[`ExemptDomainFileTypePairsFromFileTypeDownloadWarnings`](#exemptdomainfiletypepairsfromfiletypedownloadwarnings)** | Disable warnings based on file extension for specific file types on domains.
| **[`Extensions`](#extensions)** | Control the installation, uninstallation and locking of extensions.
| **[`ExtensionSettings`](#extensionsettings)** | Manage all aspects of extensions.
| **[`ExtensionUpdate`](#extensionupdate)** | Control extension updates.
| **[`FirefoxHome`](#firefoxhome)** | Customize the Firefox Home page.
| **[`FirefoxSuggest`](#firefoxsuggest)** | Customize Firefox Suggest.
| **[`GenerativeAI`](#generativeai)** | Configure generative AI features.
| **[`GoToIntranetSiteForSingleWordEntryInAddressBar`](#gotointranetsiteforsinglewordentryinaddressbar)** | Force direct intranet site navigation instead of searching when typing single word entries in the address bar.
| **[`Handlers`](#handlers)** | Configure default application handlers.
| **[`HardwareAcceleration`](#hardwareacceleration)** | Control hardware acceleration.
| **[`Homepage`](#homepage)** | Configure the default homepage and how Firefox starts.
| **[`HttpAllowlist`](#httpallowlist)** | Configure origins that will not be upgraded to HTTPS.
| **[`HttpsOnlyMode`](#httpsonlymode)** | Configure HTTPS-Only Mode.
| **[`InstallAddonsPermission`](#installaddonspermission)** | Configure the default extension install policy as well as origins for extension installs are allowed.
| **[`LegacyProfiles`](#legacyprofiles)** | Disable the feature enforcing a separate profile for each installation.
| **[`LegacySameSiteCookieBehaviorEnabled`](#legacysamesitecookiebehaviorenabled)** | Enable default legacy SameSite cookie behavior setting.
| **[`LegacySameSiteCookieBehaviorEnabledForDomainList`](#legacysamesitecookiebehaviorenabledfordomainlist)** | Revert to legacy SameSite behavior for cookies on specified sites.
| **[`LocalFileLinks`](#localfilelinks)** | Enable linking to local files by origin.
| **[`ManagedBookmarks`](#managedbookmarks)** | Configures a list of bookmarks managed by an administrator that cannot be changed by the user.
| **[`ManualAppUpdateOnly`](#manualappupdateonly)** | Allow manual updates only and do not notify the user about updates.
| **[`MicrosoftEntraSSO`](#microsoftentrasso)** | Allow single sign-on for Microsoft Entra accounts on macOS.
| **[`NetworkPrediction`](#networkprediction)** | Enable or disable network prediction (DNS prefetching).
| **[`NewTabPage`](#newtabpage)** | Enable or disable the New Tab page.
| **[`NoDefaultBookmarks`](#nodefaultbookmarks)** | Disable the creation of default bookmarks.
| **[`OfferToSaveLogins`](#offertosavelogins)** | Control whether or not Firefox offers to save passwords.
| **[`OfferToSaveLoginsDefault`](#offertosaveloginsdefault)** | Set the default value for whether or not Firefox offers to save passwords.
| **[`OverrideFirstRunPage`](#overridefirstrunpage)** | Override the first run page.
| **[`OverridePostUpdatePage`](#overridepostupdatepage)** | Override the upgrade page.
| **[`PasswordManagerEnabled`](#passwordmanagerenabled)** | Remove (some) access to the password manager.
| **[`PasswordManagerExceptions`](#passwordmanagerexceptions)** | Prevent Firefox from saving passwords for specific sites.
| **[`PDFjs`](#pdfjs)** | Disable or configure PDF.js, the built-in PDF viewer.
| **[`Permissions`](#permissions)** | Set permissions associated with camera, microphone, location, and notifications.
| **[`PictureInPicture`](#pictureinpicture)** | Enable or disable Picture-in-Picture.
| **[`PopupBlocking`](#popupblocking)** | Configure the default pop-up window policy as well as origins for which pop-up windows are allowed.
| **[`PostQuantumKeyAgreementEnabled`](#postquantumkeyagreementenabled)** | Enable post-quantum key agreement for TLS.
| **[`Preferences`](#preferences)** | Set and lock preferences.
| **[`PrimaryPassword`](#primarypassword)** | Require or prevent using a primary (formerly master) password.
| **[`PrintingEnabled`](#printingenabled)** | Enable or disable printing.
| **[`PrivateBrowsingModeAvailability`](#privatebrowsingmodeavailability)** | Set availability of private browsing mode.
| **[`PromptForDownloadLocation`](#promptfordownloadlocation)** | Ask where to save each file before downloading.
| **[`Proxy`](#proxy)** | Configure proxy settings.
| **[`RequestedLocales`](#requestedlocales)** | Set the list of requested locales for the application in order of preference.
| **[`SanitizeOnShutdown` (All)](#sanitizeonshutdown-all)** | Clear all data on shutdown.
| **[`SanitizeOnShutdown` (Selective)](#sanitizeonshutdown-selective)** | Clear data on shutdown.
| **[`SearchBar`](#searchbar)** | Set whether or not search bar is displayed.
| **[`SearchEngines`](#searchengines)** |
| **[`SearchEngines -> Add`](#searchengines--add)** | Add new search engines.
| **[`SearchEngines -> Default`](#searchengines--default)** | Set the default search engine.
| **[`SearchEngines -> PreventInstalls`](#searchengines--preventinstalls)** | Prevent installing search engines from webpages.
| **[`SearchEngines -> Remove`](#searchengines--remove)** | Hide built-in search engines.
| **[`SearchSuggestEnabled`](#searchsuggestenabled)** | Enable search suggestions.
| **[`SecurityDevices`](#securitydevices)** | Install PKCS #11 modules.
| **[`ShowHomeButton`](#showhomebutton)** | Show the home button on the toolbar.
| **[`SkipTermsOfUse`](#skiptermsofuse)** | Don't display the Firefox [Terms of Use](https://www.mozilla.org/about/legal/terms/firefox/) and [Privacy Notice](https://www.mozilla.org/privacy/firefox/) upon startup. You represent that you accept and have the authority to accept the Terms of Use on behalf of all individuals to whom you provide access to this browser.
| **[`SSLVersionMax`](#sslversionmax)** | Set and lock the maximum version of TLS.
| **[`SSLVersionMin`](#sslversionmin)** | Set and lock the minimum version of TLS.
| **[`StartDownloadsInTempDirectory`](#startdownloadsintempdirectory)** | Force downloads to start off in a local, temporary location rather than the default download directory.
| **[`SupportMenu`](#supportmenu)** | Add a menuitem to the help menu for specifying support information.
| **[`TranslateEnabled`](#translateenabled)** | Enable or disable webpage translation.
| **[`UserMessaging`](#usermessaging)** | Don't show certain messages to the user.
| **[`UseSystemPrintDialog`](#usesystemprintdialog)** | Print using the system print dialog instead of print preview.
| **[`VisualSearchEnabled`](#visualsearchenabled)** | Enable or disable visual search.
| **[`WebsiteFilter`](#websitefilter)** | Block websites from being visited.
| **[`WindowsSSO`](#windowssso)** | Allow Windows single sign-on for Microsoft, work, and school accounts.

### 3rdparty

Allow WebExtensions to configure policy. For more information, see [Adding policy support to your extension](https://extensionworkshop.com/documentation/enterprise/enterprise-development/#how-to-add-policy).

For GPO and Intune, the extension developer should provide an ADMX file.

**Compatibility:** Firefox 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### macOS
```
<dict>
  <key>3rdparty</key>
  <dict>
    <key>Extensions</key>
    <dict>
      <key>uBlock0@raymondhill.net</key>
      <dict>
        <key>adminSettings</key>
        <dict>
          <key>selectedFilterLists</key>
          <array>
            <string>ublock-privacy</string>
            <string>ublock-badware</string>
            <string>ublock-filters</string>
            <string>user-filters</string>
          </array>
        </dict>
      </dict>
    </dict>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "3rdparty": {
      "Extensions": {
        "uBlock0@raymondhill.net": {
          "adminSettings": {
            "selectedFilterLists": [
              "ublock-privacy",
              "ublock-badware",
              "ublock-filters",
              "user-filters"
            ]
          }
        }
      }
    }
  }
}
```

### AllowedDomainsForApps

Define domains allowed to access Google Workspace.

This policy is based on the [Chrome policy](https://chromeenterprise.google/policies/#AllowedDomainsForApps) of the same name.

If this policy is enabled, users can only access Google Workspace using accounts from the specified domains. If you want to allow Gmail, you can add ```consumer_accounts``` to the list.

**Compatibility:** Firefox 89, Firefox ESR 78.11\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AllowedDomainsForApps = "managedfirefox.com,example.com"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AllowedDomainsForApps
```
Value (string):
```
<enabled/>
<data id="AllowedDomainsForApps" value="managedfirefox.com,example.com"/>
```
#### macOS
```
<dict>
  <key>AllowedDomainsForApps</key>
  <string>managedfirefox.com,example.com</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AllowedDomainsForApps": "managedfirefox.com,example.com"
  }
}
```
### AllowFileSelectionDialogs

Enable or disable file selection dialogs.

**Compatibility:** Firefox 124\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `widget.disable_file_pickers`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AllowFileSelectionDialogs = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppAutoAllowFileSelectionDialogsUpdate
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>AllowFileSelectionDialogs</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AllowFileSelectionDialogs": true | false
  }
}
```
### AppAutoUpdate

Enable or disable **automatic** application update.

If set to true, application updates are installed without user approval within Firefox. The operating system might still require approval.

If set to false, application updates are downloaded but the user can choose when to install the update.

If you have disabled updates via `DisableAppUpdate`, this policy has no effect.

**Compatibility:** Firefox 75, Firefox ESR 68.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `app.update.auto`

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
### AppUpdatePin

Prevent Firefox from being updated beyond the specified version.

You can specify the any version as ```xx.``` and Firefox will be updated with all minor versions, but will not be updated beyond the major version.

You can also specify the version as ```xx.xx``` and Firefox will be updated with all patch versions, but will not be updated beyond the minor version.

You should specify a version that exists or is guaranteed to exist. If you specify a version that doesn't end up existing, Firefox will update beyond that version.

**Compatibility:** Firefox 102,\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AppUpdatePin = "106."
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppUpdatePin
```
Value (string):
```
<enabled/>
<data id="String" value="106."/>
```
#### macOS
```
<dict>
  <key>AppUpdatePin</key>
  <string>106.</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AppUpdatePin": "106."
  }
}
```
### AppUpdateURL

Change the URL for application update if you are providing Firefox updates from a custom update server.

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

See [Integrated authentication](https://htmlpreview.github.io/?https://github.com/mdn/archived-content/blob/main/files/en-us/mozilla/integrated_authentication/raw.html) for more information.

`PrivateBrowsing` enables integrated authentication in private browsing.

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
### AutofillAddressEnabled

Enables or disables autofill for addresses.

This only applies when address autofill is enabled for a particular Firefox version or region. See [this page](https://support.mozilla.org/kb/automatically-fill-your-address-web-forms) for more information.

**Compatibility:** Firefox 125, Firefox ESR 115.10\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `extensions.formautofill.addresses.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AutofillAddressEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutofillAddressEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>AutofillAddressEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AutofillAddressEnabled": true | false
  }
}
```
### AutofillCreditCardEnabled

Enables or disables autofill for payment methods.

This only applies when payment method autofill is enabled for a particular Firefox version or region. See [this page](https://support.mozilla.org/kb/credit-card-autofill) for more information.

**Compatibility:** Firefox 125, Firefox ESR 115.10\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `extensions.formautofill.creditCards.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\AutofillCreditCardEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutofillCreditCardEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>AutofillCreditCardEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AutofillCreditCardEnabled": true | false
  }
}
```
### AutoLaunchProtocolsFromOrigins
Define a list of external protocols that can be used from listed origins without prompting the user. The origin is the scheme plus the hostname.

The syntax of this policy is exactly the same as the [Chrome AutoLaunchProtocolsFromOrigins policy](https://chromeenterprise.google/policies/#AutoLaunchProtocolsFromOrigins) except that you can only use valid origins (not just hostnames). This also means that you cannot specify an asterisk for all origins.

The schema is:
```
{
 "items": {
  "properties": {
   "allowed_origins": {
    "items": {
     "type": "string"
    },
    "type": "array"
   },
   "protocol": {
    "type": "string"
   }
  },
  "required": [
   "protocol",
   "allowed_origins"
  ],
  "type": "object"
 },
 "type": "array"
}
```
**Compatibility:** Firefox 90, Firefox ESR 78.12\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\AutoLaunchProtocolsFromOrigins (REG_MULTI_SZ) =
```
[
  {
    "protocol": "zoommtg",
    "allowed_origins": [
      "https://somesite.zoom.us"
    ]
  }
]
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutoLaunchProtocolsFromOrigins
```
Value (string):
```
<enabled/>
<data id="JSON" value='
[
  {
    "protocol": "zoommtg",
    "allowed_origins": [
      "https://somesite.zoom.us"
    ]
  }
]'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutoLaunchProtocolsFromOriginsOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='[]'/>
```
#### macOS
```
<dict>
  <key>AutoLaunchProtocolsFromOrigins</key>
  <array>
    <dict>
      <key>protocol</key>
      <string>zoommtg</string>
      <key>allowed_origins</key>
      <array>
        <string>https://somesite.zoom.us</string>
      </array>
    </dict>
  </array>
</dict>
```
#### policies.json
```
{
  "policies": {
    "AutoLaunchProtocolsFromOrigins": [{
      "protocol": "zoommtg",
      "allowed_origins": [
        "https://somesite.zoom.us"
      ]
    }]
  }
}
```
### BackgroundAppUpdate

Enable or disable **automatic** application update **in the background**, when the application is not running.

If set to true, application updates may be installed (without user approval) in the background, even when the application is not running. The operating system might still require approval.

If set to false, the application will not try to install updates when the application is not running.

If you have disabled updates via `DisableAppUpdate` or disabled automatic updates via `AppAutoUpdate`, this policy has no effect.

If you are having trouble getting the background task to run, verify your configuration with the ["Requirements to run" section in this support document](https://support.mozilla.org/en-US/kb/enable-background-updates-firefox-windows).

**Compatibility:** Firefox 90 (Windows only)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `app.update.background.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\BackgroundAppUpdate = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BackgroundAppUpdate
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>BackgroundAppUpdate</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "BackgroundAppUpdate": true | false
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

Note: [`ManagedBookmarks`](#managedbookmarks) is the new recommended way to add bookmarks. This policy will continue to be supported.

Add bookmarks in either the bookmarks toolbar or menu. Only `Title` and `URL` are required. If `Placement` is not specified, the bookmark will be placed on the toolbar. If `Folder` is specified, it is automatically created and bookmarks with the same folder name are grouped together.

If you want to clear all bookmarks set with this policy, you can set the value to an empty array (```[]```). This can be on Windows via the new Bookmarks (JSON) policy available with GPO and Intune.

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

Software\Policies\Mozilla\Firefox\Bookmarks (REG_MULTI_SZ) =
```
[]
```

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
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Bookmarks
```
Value (string):
```
<enabled/>
<data id="JSON" value='[]'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BookmarksOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='[]'/>
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

Note: This policy only works on Windows and macOS. For Linux discussion, see [bug 1600509](https://bugzilla.mozilla.org/show_bug.cgi?id=1600509).

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
### Containers
Set policies related to [containers](https://addons.mozilla.org/firefox/addon/multi-account-containers/).

Currently you can set the initial set of containers.

For each container, you can specify the name, icon, and color.

| Name | Description |
| --- | --- |
| `name`| Name of container
| `icon` | Can be `fingerprint`, `briefcase`, `dollar`, `cart`, `vacation`, `gift`, `food`, `fruit`, `pet`, `tree`, `chill`, `circle`, `fence`
| `color` | Can be `blue`, `turquoise`, `green`, `yellow`, `orange`, `red`, `pink`, `purple`, `toolbar`

**Compatibility:** Firefox 113\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\Containers (REG_MULTI_SZ) =
```
{
  "Default": [
    {
      "name": "My container",
      "icon": "pet",
      "color": "turquoise"
    }
  ]
}
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Containers
```
Value (string):
```
<enabled/>
<data id="JSON" value='
{
  "Default": [
    {
      "name": "My container",
      "icon": "pet",
      "color": "turquoise"
    }
  ]
}
'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ContainersOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='{}'/>
```
#### macOS
```
<dict>
  <key>Default</key>
  <dict>
    <key>Containers</key>
    <array>
      <dict>
        <key>name</key>
        <string>My container</string>
        <key>icon</key>
        <string>pet</string>
        <key>color</key>
        <string>turquoise</string>
      </dict>
    </array>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "Containers": {
      "Default": [
        {
          "name": "My container",
          "icon": "pet",
          "color": "turquoise"
        }
      ]
    }
  }
}
```
### ContentAnalysis
Configure Firefox to use an agent for Data Loss Prevention (DLP) that is compatible with the [Google Chrome Content Analysis Connector Agent SDK](https://github.com/chromium/content_analysis_sdk).

`AgentName` is the name of the DLP agent. This is used in dialogs and notifications about DLP operations. The default is "A DLP Agent".

`AgentTimeout` is the timeout in number of seconds after a DLP request is sent to the agent. After this timeout, the request will be denied unless `TimeoutResult` is set to 1 or 2. The default is 300.

`AllowUrlRegexList` is a space-separated list of regular expressions that indicates URLs for which DLP operations will always be allowed without consulting the agent. The default is "^about:(?!blank&#124;srcdoc).*", meaning that any pages that start with "about:" will be exempt from DLP except for "about:blank" and "about:srcdoc", as these can be controlled by web content.

`BypassForSameTabOperations` indicates whether Firefox will automatically allow DLP requests whose data comes from the same tab and frame - for example, if data is copied to the clipboard and then pasted on the same page. The default is false.

`ClientSignature` indicates the required signature of the DLP agent connected to the pipe. If this is a non-empty string and the DLP agent does not have a signature with a Subject Name that exactly matches this value, Firefox will not connect to the pipe. The default is the empty string.

`DefaultResult` indicates the desired behavior for DLP requests if there is a problem connecting to the DLP agent. The default is 0.

| Value | Description
| --- | --- |
| 0 | Deny the request (default)
| 1 | Warn the user and allow them to choose whether to allow or deny
| 2 | Allow the request

`DenyUrlRegexList` is a space-separated list of regular expressions that indicates URLs for which DLP operations will always be denied without consulting the agent. The default is the empty string.

`Enabled` indicates whether Firefox should use DLP. Note that if this value is true and no DLP agent is running, all DLP requests will be denied unless `DefaultResult` is set to 1 or 2.

`InterceptionPoints` controls settings for specific interception points.

* The `Clipboard` entry controls clipboard operations for files and text.
  * `Enabled` indicates whether clipboard operations should use DLP. The default is true.
  * `PlainTextOnly` indicates whether to only analyze the text/plain format on the clipboard. If this
    value is false, all formats will be analyzed, which some DLP agents may not expect. Regardless of
    this value, files will be analyzed as usual. The default is true.
* The `Download` entry controls download operations. (Added in Firefox 142, Firefox ESR 140.2)
  * `Enabled` indicates whether download operations should use DLP. The default is false.
* The `DragAndDrop` entry controls drag and drop operations for files and text.
  * `Enabled` indicates whether drag and drop operations should use DLP. The default is true.
  * `PlainTextOnly` indicates whether to only analyze the text/plain format in what is being dropped.
    If this value is false, all formats will be analyzed, which some DLP agents may not expect.
    Regardless of this value, files will be analyzed as usual. The default is true.
* The `FileUpload` entry controls file upload operations for files chosen from the file picker.
  * `Enabled` indicates whether file upload operations should use DLP. The default is true.
* The `Print` entry controls print operation.
  * `Enabled` indicates whether print operations should use DLP. The default is true.

`IsPerUser` indicates whether the pipe the DLP agent has created is per-user or per-system. The default is true, meaning per-user.

`PipePathName` is the name of the pipe the DLP agent has created and Firefox will connect to. The default is "path_user".

`ShowBlockedResult` indicates whether Firefox should show a notification when a DLP request is denied. The default is true.

`TimeoutResult` indicates the desired behavior for DLP requests if the DLP agent does not respond to a request in less than `AgentTimeout` seconds. The default is 0.

| Value | Description
| --- | --- |
| 0 | Deny the request (default)
| 1 | Warn the user and allow them to choose whether to allow or deny
| 2 | Allow the request


**Compatibility:** Firefox 137\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.contentanalysis.agent_name`, `browser.contentanalysis.agent_timeout`, `browser.contentanalysis.allow_url_regex_list`, `browser.contentanalysis.bypass_for_same_tab_operations`, `browser.contentanalysis.client_signature`, `browser.contentanalysis.default_result`, `browser.contentanalysis.deny_url_regex_list`, `browser.contentanalysis.enabled`, `browser.contentanalysis.interception_point.clipboard.enabled`, `browser.contentanalysis.interception_point.clipboard.plain_text_only`, `browser.contentanalysis.interception_point.download.enabled`, `browser.contentanalysis.interception_point.drag_and_drop.enabled`, `browser.contentanalysis.interception_point.drag_and_drop.plain_text_only`, `browser.contentanalysis.interception_point.file_upload.enabled`, `browser.contentanalysis.interception_point.print.enabled`, `browser.contentanalysis.is_per_user`, `browser.contentanalysis.pipe_path_name`, `browser.contentanalysis.show_blocked_result`, `browser.contentanalysis.timeout_result`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\ContentAnalysis\AgentName = "My DLP Product"
Software\Policies\Mozilla\Firefox\ContentAnalysis\AgentTimeout = 60
Software\Policies\Mozilla\Firefox\ContentAnalysis\AllowUrlRegexList = "https://example\.com/.* https://subdomain\.example\.com/.*"
Software\Policies\Mozilla\Firefox\ContentAnalysis\BypassForSameTabOperations = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\ClientSignature = "My DLP Company"
Software\Policies\Mozilla\Firefox\ContentAnalysis\DefaultResult = 0x0 | 0x1 | 0x2
Software\Policies\Mozilla\Firefox\ContentAnalysis\DenyUrlRegexList = "https://example\.com/.* https://subdomain\.example\.com/.*"
Software\Policies\Mozilla\Firefox\ContentAnalysis\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\Clipboard\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\Clipboard\PlainTextOnly = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\Download\Enabled = 0x0 | 0x1
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\DragAndDrop\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\DragAndDrop\PlainTextOnly = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\FileUpload\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\InterceptionPoints\Print\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\IsPerUser = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\PipePathName = "pipe_custom_name"
Software\Policies\Mozilla\Firefox\ContentAnalysis\ShowBlockedResult = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\ContentAnalysis\TimeoutResult = 0x0 | 0x1 | 0x2
```

#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_AgentName
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_AgentName" value="My DLP Product"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_AgentTimeout
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_AgentTimeout" value="60"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_AllowUrlRegexList
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_AllowUrlRegexList" value="https://example\.com/.* https://subdomain\.example\.com/.*"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_BypassForSameTabOperations
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_ClientSignature
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_ClientSignature" value="My DLP Company"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_DefaultResult
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_DefaultResult" value="1"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_DenyUrlRegexList
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_DenyUrlRegexList" value="https://example\.com/.* https://subdomain\.example\.com/.*"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_Enabled
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~Clipboard/ContentAnalysis_InterceptionPoints_Clipboard
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~Clipboard/ContentAnalysis_InterceptionPoints_Clipboard_PlainTextOnly
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints/ContentAnalysis_InterceptionPoints_Download_Enabled
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~DragAndDrop/ContentAnalysis_InterceptionPoints_DragAndDrop
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~DragAndDrop/ContentAnalysis_InterceptionPoints_DragAndDrop_PlainTextOnly
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints/ContentAnalysis_InterceptionPoints_FileUpload_Enabled
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints/ContentAnalysis_InterceptionPoints_Print_Enabled
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_IsPerUser
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_PipePathName
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_PipePathName" value="pipe_custom_name"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_ShowBlockedResult
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_TimeoutResult
```
Value (string):
```
<enabled/>
<data id="ContentAnalysis_TimeoutResult" value="1"/>
```

#### policies.json
```
{
  "policies": {
    "ContentAnalysis": {
      "AgentName": "My DLP Product",
      "AgentTimeout": 60,
      "AllowUrlRegexList": "https://example\.com/.* https://subdomain\.example\.com/.*",
      "BypassForSameTabOperations": true | false,
      "ClientSignature": "My DLP Company",
      "DefaultResult": 0 | 1 | 2,
      "DenyUrlRegexList": "https://example\.com/.* https://subdomain\.example\.com/.*",
      "Enabled": true | false,
      "InterceptionPoints": {
        "Clipboard": {
          "Enabled": true | false,
          "PlainTextOnly": true | false
        },
        "Download": {
          "Enabled": false | true,
        },
        "DragAndDrop": {
          "Enabled": true | false,
          "PlainTextOnly": true | false
        },
        "FileUpload": {
          "Enabled": true | false
        },
        "Print": {
          "Enabled": true | false
        }
      },
      "IsPerUser": true | false,
      "PipePathName": "pipe_custom_name",
      "ShowBlockedResult": true | false,
      "TimeoutResult": 0 | 1 | 2,
    }
  }
}
```

### Cookies
Configure cookie preferences.

`Allow` is a list of origins (not domains) where cookies are always allowed. You must include http or https.

`AllowSession` is a list of origins (not domains) where cookies are only allowed for the current session. You must include http or https.

`Block` is a list of origins (not domains) where cookies are always blocked. You must include http or https.

`Behavior` sets the default behavior for cookies based on the values below.

`BehaviorPrivateBrowsing` sets the default behavior for cookies in private browsing based on the values below.

| Value | Description
| --- | --- |
| accept | Accept all cookies
| reject-foreign | Reject third party cookies
| reject | Reject all cookies
| limit-foreign | Reject third party cookies for sites you haven't visited
| reject-tracker | Reject cookies for known trackers (default)
| reject-tracker-and-partition-foreign | Reject cookies for known trackers and partition third-party cookies (Total Cookie Protection) (default for private browsing)

`Locked` prevents the user from changing cookie preferences.

`Default` determines whether cookies are accepted at all. (*Deprecated*. Use `Behavior` instead)

`AcceptThirdParty` determines how third-party cookies are handled. (*Deprecated*. Use `Behavior` instead)

`RejectTracker` only rejects cookies for trackers. (*Deprecated*. Use `Behavior` instead)

`ExpireAtSessionEnd` determines when cookies expire. (*Deprecated*. Use [`SanitizeOnShutdown`](#sanitizeonshutdown-selective) instead)

**Compatibility:** Firefox 60, Firefox ESR 60 (RejectTracker added in Firefox 63, AllowSession added in Firefox 79/78.1, Behavior added in Firefox 95/91.4)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.cookie.cookieBehavior`, `network.cookie.cookieBehavior.pbmode`, `network.cookie.lifetimePolicy`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Cookies\Allow\1 = "https://example.com"
Software\Policies\Mozilla\Firefox\Cookies\AllowSession\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Cookies\Block\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Cookies\Behavior = "accept" | "reject-foreign" | "reject" | "limit-foreign" | "reject-tracker" | "reject-tracker-and-partition-foreign"
Software\Policies\Mozilla\Firefox\Cookies\BehaviorPrivateBrowsing = "accept" | "reject-foreign" | "reject" | "limit-foreign" | "reject-tracker" | "reject-tracker-and-partition-foreign"
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
<data id="Permissions" value="1&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_AllowSession
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Behavior
```
Value (string):
```
<enabled/>
<data id="Cookies_Behavior" value="accept | reject-foreign | reject | limit-foreign | reject-tracker | reject-tracker-and-partition-foreign"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_BehaviorPrivateBrowsing
```
Value (string):
```
<enabled/>
<data id="Cookies_BehaviorPrivateBrowsing" value="accept | reject-foreign | reject | limit-foreign | reject-tracker | reject-tracker-and-partition-foreign"/>
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
    <key>AllowSession</key>
    <array>
      <string>http://example.edu</string>
    </array>
    <key>Block</key>
    <array>
      <string>http://example.org</string>
    </array>
    <key>Locked</key>
    <true/> | <false/>
    <key>Behavior</key>
    <string>accept | reject-foreign | reject | limit-foreign | reject-tracker | reject-tracker-and-partition-foreign</string>
    <key>BehaviorPrivateBrowsing</key>
    <string>accept | reject-foreign | reject | limit-foreign | reject-tracker | reject-tracker-and-partition-foreign</string>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "Cookies": {
      "Allow": ["http://example.org/"],
      "AllowSession": ["http://example.edu/"],
      "Block": ["http://example.edu/"],
      "Locked": true | false,
      "Behavior": "accept" | "reject-foreign" | "reject" | "limit-foreign" | "reject-tracker" | "reject-tracker-and-partition-foreign",
      "BehaviorPrivateBrowsing": "accept" | "reject-foreign" | "reject" | "limit-foreign" | "reject-tracker" | "reject-tracker-and-partition-foreign",
    }
  }
}
```
### DefaultDownloadDirectory
Set the default download directory.

You can use ${home} for the native home directory.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.download.dir`, `browser.download.folderList`

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
}
```
#### policies.json (Windows)
```
{
  "policies": {
    "DefaultDownloadDirectory": "${home}\\Downloads"
  }
}
```
### DisableAppUpdate
Turn off application updates within Firefox.

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

Note: As of Firefox 140, this policy no longer completely disables PDF.js; it changes the handler to send PDF files to the operating system. Embedded PDF files are shown in the browser. If you need to completely disable PDF.js, you can use the [`PDFjs`](#pdfjs) policy. 

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disablePDFjs`\
**Preferences Affected:** N/A

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
Disable specific cryptographic ciphers, listed below.

```
TLS_DHE_RSA_WITH_AES_128_CBC_SHA
TLS_DHE_RSA_WITH_AES_256_CBC_SHA
TLS_RSA_WITH_AES_128_CBC_SHA
TLS_RSA_WITH_AES_256_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
TLS_RSA_WITH_3DES_EDE_CBC_SHA
TLS_RSA_WITH_AES_128_GCM_SHA256 (Firefox 78)
TLS_RSA_WITH_AES_256_GCM_SHA384 (Firefox 78)
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 (Firefox 97 and Firefox ESR 91.6)
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (Firefox 97 and Firefox ESR 91.6)
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (Firefox 97 and Firefox ESR 91.6)
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (Firefox 97 and Firefox ESR 91.6)
TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (Firefox 97 and Firefox ESR 91.6)
TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (Firefox 97 and Firefox ESR 91.6)
TLS_CHACHA20_POLY1305_SHA256 (Firefox 138, Firefox ESR 128.10)
TLS_AES_128_GCM_SHA256 (Firefox 138, Firefox ESR 128.10)
TLS_AES_256_GCM_SHA384 (Firefox 138, Firefox ESR 128.10)
```

**Preferences Affected:** `security.ssl3.ecdhe_rsa_aes_128_gcm_sha256`, `security.ssl3.ecdhe_ecdsa_aes_128_gcm_sha256`, `security.ssl3.ecdhe_ecdsa_chacha20_poly1305_sha256`, `security.ssl3.ecdhe_rsa_chacha20_poly1305_sha256`, `security.ssl3.ecdhe_ecdsa_aes_256_gcm_sha384`, `security.ssl3.ecdhe_rsa_aes_256_gcm_sha384`, `security.ssl3.ecdhe_rsa_aes_128_sha`, `security.ssl3.ecdhe_ecdsa_aes_128_sha`, `security.ssl3.ecdhe_rsa_aes_256_sha`, `security.ssl3.ecdhe_ecdsa_aes_256_sha`, `security.ssl3.dhe_rsa_aes_128_sha`, `security.ssl3.dhe_rsa_aes_256_sha`, `security.ssl3.rsa_aes_128_gcm_sha256`, `security.ssl3.rsa_aes_256_gcm_sha384`, `security.ssl3.rsa_aes_128_sha`, `security.ssl3.rsa_aes_256_sha`, `security.ssl3.deprecated.rsa_des_ede3_sha`, `security.tls13.chacha20_poly1305_sha256`, `security.tls13.aes_128_gcm_sha256`, `security.tls13.aes_256_gcm_sha384`

---
**Note:**

This policy was updated in Firefox 78 to allow enabling ciphers as well. Setting the value to true disables the cipher, setting the value to false enables the cipher. Previously setting the value to true or false disabled the cipher.

---
**Compatibility:** Firefox 76, Firefox ESR 68.8\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisabledCiphers\CIPHER_NAME = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_CIPHER_NAME

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
      <key>CIPHER_NAME</key>
      <true/> | <false/>
    </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisabledCiphers": {
      "CIPHER_NAME": true | false,
    }
  }
}
```
### DisableDefaultBrowserAgent
Prevent the default browser agent from taking any actions. Only applicable to Windows; other platforms don’t have the agent.

The browser agent is a Windows-only scheduled task which runs in the background to collect and submit data about the browser that the user has set as their OS default. More information is available [here](https://firefox-source-docs.mozilla.org/toolkit/mozapps/defaultagent/default-browser-agent/index.html).

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
### DisableEncryptedClientHello
Disable the TLS Feature for Encrypted Client Hello. Note that TLS Client Hellos will still contain an ECH extension, but this extension will not be used by Firefox during the TLS handshake. 

**Compatibility:** Firefox 127, Firefox ESR 128\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.dns.echconfig.enabled`, `network.dns.http3_echconfig.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableEncryptedClientHello = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableEncryptedClientHello
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>DisableEncryptedClientHello</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisableEncryptedClientHello": true | false
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
### DisableFirefoxStudies
Disable Firefox studies (Shield).

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.newtabpage.activity-stream.asrouter.userprefs.cfr.addons`, `browser.newtabpage.activity-stream.asrouter.userprefs.cfr.features`

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
**Preferences Affected:** `browser.formfill.enable`

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
### DisableMasterPasswordCreation
Remove the master password functionality.

If this value is true, it works the same as setting [`PrimaryPassword`](#primarypassword) to false and removes the primary password functionality.

If both `DisableMasterPasswordCreation` and `PrimaryPassword` are used, `DisableMasterPasswordCreation` takes precedent.

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
### DisablePocket (Deprecated)

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

This policy is superseded by [`PrivateBrowsingModeAvailability`](#privatebrowsingmodeavailability)

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

These policies only affect what happens when an error is shown, they do not affect any settings in preferences.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.certerror.hideAddException`, `browser.safebrowsing.allowOverride`

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
    <key>SafeBrowsing</key>
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
### DisableSystemAddonUpdate
Prevent system add-ons from being installed or updated.

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

As of Firefox 83 and Firefox ESR 78.5, local storage of telemetry data is disabled as well.

Mozilla recommends that you do not disable telemetry. Information collected through telemetry helps us build a better product for businesses like yours.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `disableTelemetry`\
**Preferences Affected:** `datareporting.healthreport.uploadEnabled`, `datareporting.policy.dataSubmissionEnabled`, `toolkit.telemetry.archive.enabled`, `datareporting.usage.uploadEnabled`

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
### DisableThirdPartyModuleBlocking
Do not allow blocking third-party modules from the `about:third-party` page.

This policy only works on Windows through GPO (not policies.json).

**Compatibility:** Firefox 110 (Windows only, GPO only)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisableThirdPartyModuleBlocking = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableThirdPartyModuleBlocking
```
Value (string):
```
<enabled/> or <disabled/>
```
### DisplayBookmarksToolbar
Set the initial state of the bookmarks toolbar. A user can still change how it is displayed.

`always` means the bookmarks toolbar is always shown.

`never` means the bookmarks toolbar is not shown.

`newtab` means the bookmarks toolbar is only shown on the new tab page.

**Compatibility:** Firefox 109, Firefox ESR 102.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DisplayBookmarksToolbar = "always", "never", "newtab"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisplayBookmarksToolbar_Enum
```
Value (string):
```
<enabled/>
<data id="DisplayBookmarksToolbar" value="always | never | newtab"/>
```
#### macOS
```
<dict>
  <key>DisplayBookmarksToolbar</key>
  <string>always | never | newtab</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "DisplayBookmarksToolbar": "always" | "never" | "newtab"
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

`Fallback` determines whether or not Firefox will use your default DNS resolver if there is a problem with the secure DNS provider.

**Compatibility:** Firefox 63, Firefox ESR 68 (ExcludedDomains added in 75/68.7) (Fallback added in 124)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.trr.mode`, `network.trr.uri`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\ProviderURL = "URL_TO_ALTERNATE_PROVIDER"
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\ExcludedDomains\1 = "example.com"
Software\Policies\Mozilla\Firefox\DNSOverHTTPS\Fallback = 0x1 | 0x0
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
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_Fallback
```
Value (string):
```
<enabled/> or <disabled/>
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
    <key>Fallback</key>
    <true/> | <false/>
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
      "ExcludedDomains": ["example.com"],
      "Fallback": true | false,
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
### DownloadDirectory
Set and lock the download directory.

You can use ${home} for the native home directory.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.download.dir`, `browser.download.folderList`, `browser.download.useDownloadDir`

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

If `EmailTracking` is set to true, hidden email tracking pixels and scripts on websites are blocked. (Firefox 112)

If `SuspectedFingerprinting` is set to true, Firefox reduces the amount of information exposed to websites to protect against potential fingerprinting attempts. (Firefox 142, Firefox ESR 140.2)

`Exceptions` are origins for which tracking protection is not enabled.

`Category` can be either ```strict``` or ```standard```. If category is set, it overrides all other settings except `Exceptions` and the user cannot change the category. (Firefox 142, Firefox ESR 140.2)

**Compatibility:** Firefox 60, Firefox ESR 60 (Cryptomining and Fingerprinting added in 70/68.2, Exceptions added in 73/68.5. Category added in Firefox 142/140.2.)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.trackingprotection.enabled`, `privacy.trackingprotection.pbmode.enabled`, `privacy.trackingprotection.cryptomining.enabled`, `privacy.trackingprotection.fingerprinting.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Value = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Cryptomining = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Fingerprinting = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\EmailTracking = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\SuspectedFingerprinting = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Exceptions\1 = "https://example.com"
Software\Policies\Mozilla\Firefox\EnableTrackingProtection\Category = "strict" | "standard"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/A_TrackingProtection_Value
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/B_TrackingProtection_Cryptomining
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/C_TrackingProtection_Fingerprinting
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/F_TrackingProtection_EmailTracking
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/D_TrackingProtection_Exceptions
```
Value (string):
```
<enabled/>
<data id="TrackingProtection_Exceptions" value="1&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/E_TrackingProtection_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/G_TrackingProtection_Category
```
Value (string):
```
<data id="TrackingProtection_Category" value="strict | standard"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/H_TrackingProtection_SuspectedFingerprinting
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>EnableTrackingProtection</key>
  <dict>
    <key>Value</key>
    <true/> | <false/>
    <key>Locked</key>
    <true/> | <false/>
    <key>Cryptomining</key>
    <true/> | <false/>
    <key>Fingerprinting</key>
    <true/> | <false/>
    <key>EmailTracking</key>
    <true/> | <false/>
    <key>SuspectedFingerprinting</key>
    <true/> | <false/>
    <key>Exceptions</key>
    <key>Category</key>
    <string>strict | standard</string>
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
      "EmailTracking": true | false,
      "SuspectedFingerprinting": true | false,
      "Category": "strict" | "standard",
      "Exceptions": ["https://example.com"]
    }
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
    <key>Locked</key>
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
### ExemptDomainFileTypePairsFromFileTypeDownloadWarnings

Disable warnings based on file extension for specific file types on domains.

This policy is based on the [Chrome policy](https://chromeenterprise.google/policies/#ExemptDomainFileTypePairsFromFileTypeDownloadWarnings) of the same name.

Important: The documentation for the policy for both Edge and Chrome is incorrect. The ```domains``` value must be a domain, not a URL pattern. Also, we do not support using ```*``` to mean all domains.

**Compatibility:** Firefox 102\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\ExemptDomainFileTypePairsFromFileTypeDownloadWarnings (REG_MULTI_SZ) =
```
[
  {
     "file_extension": "jnlp",
     "domains": ["example.com"]
  }
]
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ExemptDomainFileTypePairsFromFileTypeDownloadWarnings
```
Value (string):
```
<enabled/>
<data id="JSON" value='
[
  {
     "file_extension": "jnlp",
     "domains": ["example.com"]
  }
]
'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ExemptDomainFileTypePairsFromFileTypeDownloadWarningsOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='[]'/>
```
#### macOS
```
<dict>
  <key>ExemptDomainFileTypePairsFromFileTypeDownloadWarnings</key>
  <array>
    <dict>
      <key>file_extension</key>
      <string>jnlp</string>
      <key>domains</key>
      <array>
        <string>example.com</string>
      </array>
    </dict>
  </array>
</dict>
```
#### policies.json
```
{
  "policies": {
    "ExemptDomainFileTypePairsFromFileTypeDownloadWarnings": [{
      "file_extension": "jnlp",
      "domains": ["example.com"]
    }]
  }
}
```
### Extensions
Control the installation, uninstallation and locking of extensions.

Note: The **[`ExtensionSettings`](#extensionsettings)** policy was added in Firefox 69. It provides additional functionality and is closer in compatibility to Chrome and Edge. It does not support native paths, though, so you'll have to use file:/// URLs. I'd recommend trying it before using this policy. Any future improvements will happen in that policy.

We will not, however, be removing this policy.

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
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/Extensions_Install
```
Value (string):
```
<enabled/>
<data id="Extensions" value="1&#xF000;https://addons.mozilla.org/firefox/downloads/somefile.xpi&#xF000;2&#xF000;//path/to/xpi"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/Extensions_Uninstall
```
Value (string):
```
<enabled/>
<data id="Extensions" value="1&#xF000;bad_addon_id@mozilla.org"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/Extensions_Locked
```
Value (string):
```
<enabled/>
<data id="Extensions" value="1&#xF000;addon_id@mozilla.org"/>
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

To obtain an extension ID, install the extension and go to about:support. You will see the ID in the Extensions section. I've also created an extension that makes it easy to find the ID of extensions on AMO. You can download it [here](https://github.com/mkaply/queryamoid/releases/tag/v0.1).
Or you can ask the Mozilla Addons API, see [docs](https://mozilla.github.io/addons-server/topics/api/addons.html#detail), which returns the ID as `guid`: https://addons.mozilla.org/api/v5/addons/addon/ublock-origin/

**Note:**
If the extension ID is a UUID ({12345678-1234-1234-1234-1234567890ab}), you must include the curly braces around the ID.

The configuration for each extension is another dictionary that can contain the fields documented below.

| Name | Description |
| --- | --- |
| `installation_mode` | Maps to a string indicating the installation mode for the extension. The valid strings are `allowed`,`blocked`,`force_installed`, and `normal_installed`.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`allowed` | Allows the extension to be installed by the user. This is the default behavior. There is no need for an install_url; it will automatically be allowed based on the ID.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`blocked`| Blocks installation of the extension and removes it from the device if already installed.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`force_installed`| The extension is automatically installed and can't be removed by the user. This option is not valid for the default configuration and requires an install_url.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`normal_installed`| The extension is automatically installed but can be disabled by the user. This option is not valid for the default configuration and requires an install_url.
| `install_url`| The URL from which Firefox can download a `force_installed` or `normal_installed` extension. Extensions are be automatically updated or re-installed when the XPI file's internal [version](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version) changes.<ul><li>If installing from the `addons.mozilla.org`, use `https://addons.mozilla.org/firefox/downloads/latest/ADDON_ID/latest.xpi` and substitue **ADDON_ID** with the extension's ID (for example `uBlock0@raymondhill.net` or `{446900e4-71c2-419f-a6a7-df9c091e268b}`).</li><li>If installing from the local file system, use a [```file:///``` URL](https://en.wikipedia.org/wiki/File_URI_scheme). You can mantually trigger an update or re-installation by changing the XPI's file name.</li><li>Languages packs are available from `https://releases.mozilla.org/pub/firefox/releases/VERSION/PLATFORM/xpi/LANGUAGE.xpi` (for example, `https://releases.mozilla.org/pub/firefox/releases/111.0.1/win64/xpi/en-US.xpi`).</li></ul>
| `install_sources` | A list of sources from which installing extensions is allowed using URL match patterns. **This is unnecessary if you are only allowing the installation of certain extensions by ID.** Each item in this list is an extension-style match pattern. Users will be able to easily install items from any URL that matches an item in this list. Both the location of the *.xpi file and the page where the download is started from (i.e.  the referrer) must be allowed by these patterns. This setting can be used only for the default configuration.
| `allowed_types` | This setting whitelists the allowed types of extension/apps that can be installed in Firefox. The value is a list of strings, each of which should be one of the following: "extension", "theme", "dictionary", "locale" This setting can be used only for the default configuration.
| `blocked_install_message` | This maps to a string specifying the error message to display to users if they're blocked from installing an extension. This setting allows you to append text to the generic error message displayed when the extension is blocked. This could be used to direct users to your help desk, explain why a particular extension is blocked, or something else. This setting can be used only for the default configuration.
| `restricted_domains` | An array of domains on which content scripts can't be run. This setting can be used only for the default configuration.
| `updates_disabled` | (Firefox 89, Firefox ESR 78.11) Boolean that indicates whether or not to disable automatic updates for an individual extension.
| `default_area` | (Firefox 113) String that indicates where to place the extension icon by default. Possible values are `navbar` and `menupanel`.
| `temporarily_allow_weak_signatures`| (Firefox 127) A boolean that indicates whether to allow installing extensions signed using deprecated signature algorithms.
| `private_browsing`| (Firefox 136, Firefox ESR 128.8) A boolean that indicates whether or not this extension should be enabled in private browsing.

**Compatibility:** Firefox 69, Firefox ESR 68.1 (As of Firefox 85, Firefox ESR 78.7, installing a theme makes it the default.)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\ExtensionSettings (REG_MULTI_SZ) =
```
{
  "*": {
    "blocked_install_message": "Custom error message.",
    "install_sources": ["https://yourwebsite.com/*"],
    "installation_mode": "blocked",
    "allowed_types": ["extension"]
  },
  "uBlock0@raymondhill.net": {
    "installation_mode": "force_installed",
    "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"  # using slug / short name
  },
  "adguardadblocker@adguard.com": {
    "installation_mode": "force_installed",
    "install_url": "https://addons.mozilla.org/firefox/downloads/latest/adguardadblocker@adguard.com/latest.xpi"  # using extension ID
  },
  "https-everywhere@eff.org": {
    "installation_mode": "allowed",
    "updates_disabled": false
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
{
  "*": {
    "blocked_install_message": "Custom error message.",
    "install_sources": ["https://yourwebsite.com/*"],
    "installation_mode": "blocked",
    "allowed_types": ["extension"]
  },
  "uBlock0@raymondhill.net": {
    "installation_mode": "force_installed",
    "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"
  },
  "adguardadblocker@adguard.com": {
    "installation_mode": "force_installed",
    "install_url": "https://addons.mozilla.org/firefox/downloads/latest/adguardadblocker@adguard.com/latest.xpi"
  },
  "https-everywhere@eff.org": {
    "installation_mode": "allowed",
    "updates_disabled": false
  }
}'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionSettingsOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='{}'/>
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
        <string>"https://yourwebsite.com/*"</string>
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
    <key>adguardadblocker@adguard.com</key>
    <dict>
      <key>installation_mode</key>
      <string>force_installed</string>
      <key>install_url</key>
      <string>https://addons.mozilla.org/firefox/downloads/latest/adguardadblocker@adguard.com/latest.xpi</string>
    </dict>
    <key>https-everywhere@eff.org</key>
    <dict>
      <key>installation_mode</key>
      <string>allowed</string>
      <key>updates_disabled</key>
      <true/> | <false/>
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
        "install_sources": ["https://yourwebsite.com/*"],
        "installation_mode": "blocked",
        "allowed_types": ["extension"]
      },
      "uBlock0@raymondhill.net": {
        "installation_mode": "force_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"
      },
      "adguardadblocker@adguard.com": {
        "installation_mode": "force_installed",
        "install_url": "https://addons.mozilla.org/firefox/downloads/latest/adguardadblocker@adguard.com/latest.xpi"
      },
      "https-everywhere@eff.org": {
        "installation_mode": "allowed",
        "updates_disabled": false
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
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionUpdate
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
### FirefoxHome
Customize the Firefox Home page.

**Compatibility:** Firefox 68, Firefox ESR 68 (SponsoredTopSites and SponsoredPocket were added in Firefox 95, Firefox ESR 91.4, Snippets was deprecated in Firefox 122, Stories and SponsoredStories were added in Firefox 141 to replace Pocket and SponsoredPocket.)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.newtabpage.activity-stream.showSearch`, `browser.newtabpage.activity-stream.feeds.topsites`, `browser.newtabpage.activity-stream.feeds.section.highlights`, `browser.newtabpage.activity-stream.feeds.section.topstories`, `browser.newtabpage.activity-stream.feeds.snippets`, `browser.newtabpage.activity-stream.showSponsoredTopSites`, `browser.newtabpage.activity-stream.showSponsored`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\FirefoxHome\Search = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\TopSites = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\SponsoredTopSites = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Highlights = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\Pocket = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxHome\SponsoredPocket = 0x1 | 0x0
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
<data id="FirefoxHome_Search" value="true | false"/>
<data id="FirefoxHome_TopSites" value="true | false"/>
<data id="FirefoxHome_SponsoredTopSites" value="true | false"/>
<data id="FirefoxHome_Highlights" value="true | false"/>
<data id="FirefoxHome_Pocket" value="true | false"/>
<data id="FirefoxHome_SponsoredPocket" value="true | false"/>
<data id="FirefoxHome_Snippets" value="true | false"/>
<data id="FirefoxHome_Locked" value="true | false"/>
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
    <key>SponsoredTopSites</key>
    <true/> | <false/>
    <key>Highlights</key>
    <true/> | <false/>
    <key>Pocket</key>
    <true/> | <false/>
    <key>Stories</key>
    <true/> | <false/>
    <key>SponsoredPocket</key>
    <true/> | <false/>
    <key>SponsoredStories</key>
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
      "SponsoredTopSites": true | false,
      "Highlights": true | false,
      "Pocket": true | false,
      "Stories": true | false,
      "SponsoredPocket": true | false,
      "SponsoredStories": true | false,
      "Snippets": true | false,
      "Locked": true | false
    }
  }
}
```
### FirefoxSuggest
Customize Firefox Suggest (US only).

**Compatibility:** Firefox 118, Firefox ESR 115.3.
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.urlbar.suggest.quicksuggest.nonsponsored`, `browser.urlbar.suggest.quicksuggest.sponsored`, `browser.urlbar.quicksuggest.dataCollection.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\FirefoxSuggest\WebSuggestions = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxSuggest\SponsoredSuggestions = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxSuggest\ImproveSuggest = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\FirefoxSuggest\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_WebSuggestions
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_SponsoredSuggestions
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_ImproveSuggest
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>FirefoxSuggest</key>
  <dict>
    <key>WebSuggestions</key>
    <true/> | <false/>
    <key>SponsoredSuggestions</key>
    <true/> | <false/>
    <key>ImproveSuggest</key>
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
    "FirefoxSuggest": {
      "WebSuggestions": true | false,
      "SponsoredSuggestions": true | false,
      "ImproveSuggest": true | false,
      "Locked": true | false
    }
  }
}
```
### GenerativeAI

Configure generative AI features.

`Chatbot` If false, AI chatbots are not available in the sidebar.

`LinkPreviews` If false, AI is not used to generate link previews (Firefox 144).

`TabGroups` If false,  AI is not used to suggest names and tabs for tab groups (Firefox 144).

`Locked` prevents the user from changing generative AI preferences.

**Compatibility:** Firefox 144, Firefox ESR 140.4\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.ml.chat.enabled`, `browser.ml.linkPreview.optin`, `browser.tabs.groups.smart.userEnabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\GenerativeAI\Chatbot = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\GenerativeAI\LinkPreviews = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\GenerativeAI\TabGroups = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\GenerativeAI\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_Chatbot
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_LinkPreviews
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_TabGroups
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>GenerativeAI</key>
  <dict>
    <key>Chatbot</key>
    <true/> | <false/>
    <key>LinkPreviews</key>
    <true/> | <false/>
    <key>TabGroups</key>
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
    "GenerativeAI": {
      "Chatbot": true | false,
      "LinkPreviews": true | false,
      "TabGroups": true | false,
      "Locked": true | false
    }
  }
}
```
### GoToIntranetSiteForSingleWordEntryInAddressBar
Whether to always go through the DNS server before sending a single word search string to a search engine.

If the site exists, it will navigate to the website. If the intranet responds with a 404, the page will show a 404. If the intranet does not respond, the browser will attempt a search.

The second result in the URL bar will be a search result to allow users to conduct a web search exactly as it was entered.

If instead you would like to enable the ability to have your domain appear as a valid URL and to disallow the browser from ever searching that term using the first result that matches it, add the pref `browser.fixup.domainwhitelist.YOUR_DOMAIN` (where `YOUR_DOMAIN` is the name of the domain you'd like to add), and set the pref to `true`. The URL bar will then suggest `YOUR_DOMAIN` when the user fully types `YOUR_DOMAIN`. If the user attempts to load that domain and it fails to load, it will show an "Unable to connect" error page.

You can also whitelist a domain suffix that is not part of the [Public Suffix List](https://publicsuffix.org/) by adding the pref `browser.fixup.domainsuffixwhitelist.YOUR_DOMAIN_SUFFIX` with a value of `true`.

Additionally, if you want users to see a "Did you mean to go to 'YOUR_DOMAIN'" prompt below the URL bar if they land on a search results page instead of an intranet domain that provides a response, set the pref `browser.urlbar.dnsResolveSingleWordsAfterSearch` to `1`. Enabling this will cause the browser to commit a DNS check after every single word search. If the browser receives a response from the intranet, a prompt will ask the user if they'd like to instead navigate to `YOUR_DOMAIN`. If the user presses the **yes** button, `browser.fixup.domainwhitelist.YOUR_DOMAIN` will be set to `true`.

**Compatibility:** Firefox 104, Firefox ESR 102.2\
**CCK2 Equivalent:** `N/A`\
**Preferences Affected:** `browser.fixup.dns_first_for_single_words`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\GoToIntranetSiteForSingleWordEntryInAddressBar = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/GoToIntranetSiteForSingleWordEntryInAddressBar
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>GoToIntranetSiteForSingleWordEntryInAddressBar</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "GoToIntranetSiteForSingleWordEntryInAddressBar": true | false
  }
}
```
### Handlers
Configure default application handlers. This policy is based on the internal format of `handlers.json`.

You can configure handlers based on a mime type (`mimeTypes`), a file's extension (`extensions`), or a protocol (`schemes`).

Within each handler type, you specify the given mimeType/extension/scheme as a key and use the following subkeys to describe how it is handled.

| Name | Description |
| --- | --- |
| `action`| Can be either `saveToDisk`, `useHelperApp`, `useSystemDefault`.
| `ask` | If `true`, the user is asked if what they want to do with the file. If `false`, the action is taken without user intervention.
| `handlers` | An array of handlers with the first one being the default. If you don't want to have a default handler, use an empty object for the first handler. Choose between path or uriTemplate.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name` | The display name of the handler (might not be used).
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`path`| The native path to the executable to be used.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`uriTemplate`| A url to a web based application handler. The URL must be https and contain a %s to be used for substitution.

**Compatibility:** Firefox 78, Firefox ESR 78\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\Handlers (REG_MULTI_SZ) =
```
{
  "mimeTypes": {
    "application/msword": {
      "action": "useSystemDefault",
      "ask": true | false
    }
  },
  "schemes": {
    "mailto": {
      "action": "useHelperApp",
      "ask": true | false,
      "handlers": [{
        "name": "Gmail",
        "uriTemplate": "https://mail.google.com/mail/?extsrc=mailto&url=%s"
      }]
    }
  },
  "extensions": {
    "pdf": {
      "action": "useHelperApp",
      "ask": true | false,
      "handlers": [{
        "name": "Adobe Acrobat",
        "path": "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
      }]
    }
  }
}
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Handlers
```
Value (string):
```
<enabled/>
<data id="Handlers" value='
{
  "mimeTypes": {
    "application/msword": {
      "action": "useSystemDefault",
      "ask": true | false
    }
  },
  "schemes": {
    "mailto": {
      "action": "useHelperApp",
      "ask": true | false,
      "handlers": [{
        "name": "Gmail",
        "uriTemplate": "https://mail.google.com/mail/?extsrc=mailto&amp;url=%s"
      }]
    }
  },
  "extensions": {
    "pdf": {
      "action": "useHelperApp",
      "ask": true | false,
      "handlers": [{
        "name": "Adobe Acrobat",
        "path": "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
      }]
    }
  }
}
'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HandlersOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='{}'/>
```
#### macOS
```
<dict>
  <key>Handlers</key>
  <dict>
    <key>mimeTypes</key>
    <dict>
      <key>application/msword</key>
      <dict>
        <key>action</key>
        <string>useSystemDefault</string>
        <key>ask</key>
        <true/> | <false/>
      </dict>
    </dict>
    <key>schemes</key>
    <dict>
      <key>mailto</key>
      <dict>
        <key>action</key>
        <string>useHelperApp</string>
        <key>ask</key>
        <true/> | <false/>
        <key>handlers</key>
        <array>
          <dict>
            <key>name</key>
            <string>Gmail</string>
            <key>uriTemplate</key>
            <string>https://mail.google.com/mail/?extsrc=mailto&url=%s</string>
          </dict>
        </array>
      </dict>
    </dict>
    <key>extensions</key>
    <dict>
      <key>pdf</key>
      <dict>
        <key>action</key>
        <string>useHelperApp</string>
        <key>ask</key>
        <true/> | <false/>
        <key>handlers</key>
        <array>
          <dict>
            <key>name</key>
            <string>Adobe Acrobat</string>
            <key>path</key>
            <string>/System/Applications/Preview.app</string>
          </dict>
        </array>
      </dict>
    </dict>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "Handlers": {
      "mimeTypes": {
        "application/msword": {
          "action": "useSystemDefault",
          "ask": false
        }
      },
      "schemes": {
        "mailto": {
          "action": "useHelperApp",
          "ask": true | false,
          "handlers": [{
            "name": "Gmail",
            "uriTemplate": "https://mail.google.com/mail/?extsrc=mailto&url=%s"
          }]
        }
      },
      "extensions": {
        "pdf": {
          "action": "useHelperApp",
          "ask": true | false,
          "handlers": [{
            "name": "Adobe Acrobat",
            "path": "/usr/bin/acroread"
          }]
        }
      }
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

`StartPage` is how Firefox starts.

| Value             | Description
|-------------------|-----------------------------------------------------------------------------
| `none`            | Start with a blank page (no homepage, no previous session).
| `homepage`        | Start with the homepage in `URL` policy.
| `previous-session`| Restore the previous session (all tabs and windows reopen).
| `homepage-locked` | Always force the homepage at startup, users cannot choose session restore. (Firefox 78)

**Compatibility:** Firefox 60, Firefox ESR 60 (StartPage was added in Firefox 60, Firefox ESR 60.4, homepage-locked added in Firefox 78)\
**CCK2 Equivalent:** `homePage`,`lockHomePage`\
**Preferences Affected:** `browser.startup.homepage`, `browser.startup.page`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Homepage\URL = "https://example.com"
Software\Policies\Mozilla\Firefox\Homepage\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Homepage\Additional\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Homepage\Additional\2 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Homepage\StartPage = "none" | "homepage" | "previous-session" | "homepage-locked"
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
    <string>none | homepage | previous-session | homepage-locked</string>
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
      "StartPage": "none" | "homepage" | "previous-session" | "homepage-locked"
    }
  }
}
```
### HttpAllowlist
Configure sites that will not be upgraded to HTTPS.

The sites are specified as a list of origins.

**Compatibility:** Firefox 127\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\HttpAllowlist\1 = "http://example.org"
Software\Policies\Mozilla\Firefox\HttpAllowlist\2 = "http://example.edu"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HttpAllowlist
```
Value (string):
```
<enabled/>
<data id="List" value="1&#xF000;http://example.org&#xF000;2&#xF000;http://example.edu"/>
```
#### macOS
```
<dict>
  <key>HttpAllowlist</key>
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
    "HttpAllowlist": ["http://example.org",
                       "http://example.edu"]
  }
}
```
### HttpsOnlyMode
Configure HTTPS-Only Mode.

| Value | Description
| --- | --- |
| allowed | HTTPS-Only Mode is off by default, but the user can turn it on.
| disallowed | HTTPS-Only Mode is off and the user can't turn it on.
| enabled | HTTPS-Only Mode is on by default, but the user can turn it off.
| force_enabled | HTTPS-Only Mode is on and the user can't turn it off.

**Compatibility:** Firefox 127\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `dom.security.https_only_mode`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\HttpsOnlyMode = "allowed", "disallowed", "enabled", "force_enabled"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HttpsOnlyMode
```
Value (string):
```
<enabled/>
<data id="HttpsOnlyMode" value="allowed | disallowed | enabled | force_enabled"/>
```
#### macOS
```
<dict>
  <key>HttpsOnlyMode</key>
  <string>allowed | disallowed | enabled | force_enabled</string>
</dict>
```
#### policies.json
```
{
  "policies": {
    "HttpsOnlyMode": "allowed" | "disallowed" | "enabled" | "force_enabled"
  }
}
```
### InstallAddonsPermission
Configure the default extension install policy as well as origins for extension installs are allowed. This policy does not override turning off all extension installs.

`Allow` is a list of origins where extension installs are allowed.

`Default` determines whether or not extension installs are allowed by default.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** `permissions.install`\
**Preferences Affected:** `xpinstall.enabled`, `browser.newtabpage.activity-stream.asrouter.userprefs.cfr.addons`, `browser.newtabpage.activity-stream.asrouter.userprefs.cfr.features`

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
### LegacySameSiteCookieBehaviorEnabled
Enable default legacy SameSite cookie behavior setting.

If this policy is set to true, it reverts all cookies to legacy SameSite behavior which means that cookies that don't explicitly specify a ```SameSite``` attribute are treated as if they were ```SameSite=None```.

**Compatibility:** Firefox 96\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.cookie.sameSite.laxByDefault`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\LegacySameSiteCookieBehaviorEnabled = = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LegacySameSiteCookieBehaviorEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>LegacySameSiteCookieBehaviorEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "LegacySameSiteCookieBehaviorEnabled": true | false
}
```
### LegacySameSiteCookieBehaviorEnabledForDomainList
Revert to legacy SameSite behavior for cookies on specified sites.

If this policy is set to true, cookies set for domains in this list will revert to legacy SameSite behavior which means that cookies that don't explicitly specify a ```SameSite``` attribute are treated as if they were ```SameSite=None```.

**Compatibility:** Firefox 96\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.cookie.sameSite.laxByDefault.disabledHosts`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\LegacySameSiteCookieBehaviorEnabledForDomainList\1 = "example.org"
Software\Policies\Mozilla\Firefox\LegacySameSiteCookieBehaviorEnabledForDomainList\2 = "example.edu"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LegacySameSiteCookieBehaviorEnabledForDomainList
```
Value (string):
```
<enabled/>
<data id="LegacySameSiteCookieBehaviorEnabledForDomainList" value="1&#xF000;example.org&#xF000;2&#xF000;example.edu"/>
```
#### macOS
```
<dict>
  <key>LegacySameSiteCookieBehaviorEnabledForDomainList</key>
  <array>
    <string>example.org</string>
    <string>example.edu</string>
  </array>
</dict>
```
#### policies.json
```
{
  "policies": {
    "LegacySameSiteCookieBehaviorEnabledForDomainList": ["example.org",
                                                         "example.edu"]
  }
}
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
### ManagedBookmarks
Configures a list of bookmarks managed by an administrator that cannot be changed by the user.

The bookmarks are only added as a button on the personal toolbar. They are not in the bookmarks folder.

The syntax of this policy is exactly the same as the [Chrome ManagedBookmarks policy](https://cloud.google.com/docs/chrome-enterprise/policies/?policy=ManagedBookmarks). The schema is:
```
{
 "items": {
  "id": "BookmarkType",
  "properties": {
   "children": {
    "items": {
     "$ref": "BookmarkType"
    },
    "type": "array"
   },
   "name": {
    "type": "string"
   },
   "toplevel_name": {
    "type": "string"
   },
   "url": {
    "type": "string"
   }
  },
  "type": "object"
 },
 "type": "array"
}
```
**Compatibility:** Firefox 83, Firefox ESR 78.5\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\ManagedBookmarks (REG_MULTI_SZ) =
```
[
  {
    "toplevel_name": "My managed bookmarks folder"
  },
  {
    "url": "example.com",
    "name": "Example"
  },
  {
    "name": "Mozilla links",
    "children": [
      {
        "url": "https://mozilla.org",
        "name": "Mozilla.org"
      },
      {
        "url": "https://support.mozilla.org/",
        "name": "SUMO"
      }
    ]
  }
]
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ManagedBookmarks
```
Value (string):
```
<enabled/>
<data id="JSON" value='
[
  {
    "toplevel_name": "My managed bookmarks folder"
  },
  {
    "url": "example.com",
    "name": "Example"
  },
  {
    "name": "Mozilla links",
    "children": [
      {
        "url": "https://mozilla.org",
        "name": "Mozilla.org"
      },
      {
        "url": "https://support.mozilla.org/",
        "name": "SUMO"
      }
    ]
  }
]'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ManagedBookmarksOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='[]'/>
```
#### macOS
```
<dict>
  <key>ManagedBookmarks</key>
  <array>
    <dict>
      <key>toplevel_name</key>
      <string>My managed bookmarks folder</string>
      <dict>
        <key>url</key>
        <string>example.com</string>
        <key>name</key>
        <string>Example</string>
      </dict>
      <dict>
      <key>name</key>
      <string>Mozilla links</string>
      <key>children</key>
      <array>
        <dict>
          <key>url</key>
          <string>https://mozilla.org</string>
          <key>name</key>
          <string>Mozilla</string>
        </dict>
        <dict>
          <key>url</key>
          <string>https://support.mozilla.org/</string>
          <key>name</key>
          <string>SUMO</string>
        </dict>
      </array>
    </dict>
  </array>
</dict>
```
#### policies.json
```
{
  "policies": {
    "ManagedBookmarks": [
      {
        "toplevel_name": "My managed bookmarks folder"
      },
      {
        "url": "example.com",
        "name": "Example"
      },
      {
        "name": "Mozilla links",
        "children": [
          {
            "url": "https://mozilla.org",
            "name": "Mozilla.org"
          },
          {
            "url": "https://support.mozilla.org/",
            "name": "SUMO"
          }
        ]
      }
    ]
  }
}
```
### ManualAppUpdateOnly

Switch to manual updates only.

If this policy is enabled:
 1. The user will never be prompted to install updates
 2. Firefox will not check for updates in the background, though it will check automatically when an update UI is displayed (such as the one in the About dialog). This check will be used to show "Update to version X" in the UI, but will not automatically download the update or prompt the user to update in any other way.
 3. The update UI will work as expected, unlike when using DisableAppUpdate.

This policy is primarily intended for advanced end users, not for enterprises, but it is available via GPO.

**Compatibility:** Firefox 87\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\ManualAppUpdateOnly = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ManualAppUpdateOnly
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>ManualAppUpdateOnly</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "ManualAppUpdateOnly": true | false
  }
}
```
### MicrosoftEntraSSO
Allow single sign-on for Microsoft Entra accounts on macOS.

If this policy is set to true, Firefox will use credentials stored in the Company Portal to sign in to Microsoft Entra accounts.

**Compatibility:** Firefox 132.0.1, Firefox ESR 128.5\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.http.microsoft-entra-sso.enabled`

#### macOS
```
<dict>
  <key>MicrosoftEntraSSO</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "MicrosoftEntraSSO": true | false
  }
}
```
### NetworkPrediction
Enable or disable network prediction (DNS prefetching).

**Compatibility:** Firefox 67, Firefox ESR 60.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.dns.disablePrefetch`, `network.dns.disablePrefetchFromHTTPS`

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
Override the first run page. If the value is an empty string (""), the first run page is not displayed.

Starting with Firefox 83, Firefox ESR 78.5, you can also specify multiple URLS separated by a vertical bar (|).

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
}
```
### OverridePostUpdatePage
Override the upgrade page. If the value is an empty string (""), no extra pages are displayed when Firefox is upgraded.

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
}
```
### PasswordManagerEnabled
Remove access to the password manager via preferences and blocks about:logins on Firefox 70.

**Compatibility:** Firefox 70, Firefox ESR 60.2\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `pref.privacy.disable_button.view_passwords`, `signon.rememberSignons`

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
### PasswordManagerExceptions
Prevent Firefox from saving passwords for specific sites.

The sites are specified as a list of origins.

**Compatibility:** Firefox 101\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PasswordManagerExceptions\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\PasswordManagerExceptions\2 = "https://example.edu"
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PasswordManagerExceptions
```
Value (string):
```
<enabled/>
<data id="List" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.edu"/>
```
#### macOS
```
<dict>
  <key>PasswordManagerExceptions</key>
  <array>
    <string>https://example.org</string>
    <string>https://example.edu</string>
  </array>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PasswordManagerExceptions": ["https://example.org",
                                  "https://example.edu"]
  }
}
```
### PDFjs
Disable or configure PDF.js, the built-in PDF viewer.

If `Enabled` is set to false, the built-in PDF viewer is disabled.

If `EnablePermissions` is set to true, the built-in PDF viewer will honor document permissions like preventing the copying of text.

Note: DisableBuiltinPDFViewer has not been deprecated. You can either continue to use it, or switch to using PDFjs->Enabled to disable the built-in PDF viewer. This new permission was added because we needed a place for PDFjs->EnabledPermissions.

**Compatibility:** Firefox 77, Firefox ESR 68.9\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `pdfjs.disabled`, `pdfjs.enablePermissions`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PDFjs\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\PDFjs\EnablePermissions = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PDFjs/PDFjs_Enabled
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PDFjs/PDFjs_EnablePermissions
```
Value (string):
```
<enabled/>or <disabled/>
```
#### macOS
```
<dict>
  <key>PDFjs</key>
  <dict>
    <key>Enabled</key>
    <true/> | <false/>
    <key>EnablePermissions</key>
    <true/> | <false/>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PDFjs": {
      "Enabled": true | false,
      "EnablePermissions": true | false
    }
  }
}
```
### Permissions
Set permissions associated with camera, microphone, location, notifications, autoplay, and virtual reality. Because these are origins, not domains, entries with unique ports must be specified separately. This explicitly means that it is not possible to add wildcards. See examples below.

`Allow` is a list of origins where the feature is allowed.

`Block` is a list of origins where the feature is not allowed.

`BlockNewRequests` determines whether or not new requests can be made for the feature.

`Locked` prevents the user from changing preferences for the feature.

`Default` specifies the default value for Autoplay. block-audio-video is not supported on Firefox ESR 68.

**Compatibility:** Firefox 62, Firefox ESR 60.2 (Autoplay added in Firefox 74, Firefox ESR 68.6, Autoplay Default/Locked added in Firefox 76, Firefox ESR 68.8, VirtualReality added in Firefox 80, Firefox ESR 78.2, ScreenShare added in Firefox 142, Firefox ESR 140.2)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `permissions.default.camera`, `permissions.default.microphone`, `permissions.default.geo`, `permissions.default.desktop-notification`, `media.autoplay.default`, `permissions.default.xr`, `permissions.default.screen`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Permissions\Camera\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Camera\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\Camera\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Camera\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Camera\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Microphone\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Microphone\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Location\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Location\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\Location\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Location\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Location\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Notifications\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Notifications\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Default = "allow-audio-video" | "block-audio" | "block-audio-video"
Software\Policies\Mozilla\Firefox\Permissions\Autoplay\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\VirtualReality\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\VirtualReality\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\VirtualReality\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\VirtualReality\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\VirtualReality\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\ScreenShare\Allow\1 = "https://example.org"
Software\Policies\Mozilla\Firefox\Permissions\ScreenShare\Allow\2 = "https://example.com"
Software\Policies\Mozilla\Firefox\Permissions\ScreenShare\Block\1 = "https://example.edu"
Software\Policies\Mozilla\Firefox\Permissions\ScreenShare\BlockNewRequests = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Permissions\ScreenShare\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_BlockNewRequests
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_BlockNewRequests
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
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
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
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
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
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
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_BlockNewRequests
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_Allow
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.org&#xF000;2&#xF000;https://example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_Block
```
Value (string):
```
<enabled/>
<data id="Permissions" value="1&#xF000;https://example.edu"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_BlockNewRequests
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_Locked
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
    <key>VirtualReality</key>
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
    <key>ScreenShare</key>
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
      },
      "VirtualReality": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "BlockNewRequests": true | false,
        "Locked": true | false
      },
      "ScreenShare": {
        "Allow": ["https://example.org"],
        "Block": ["https://example.edu"],
        "BlockNewRequests": true | false,
        "Locked": true | false
      }
    }
  }
}
```
### PictureInPicture

Enable or disable Picture-in-Picture as well as prevent the user from enabling or disabling it (Locked).

**Compatibility:** Firefox 78, Firefox ESR 78\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `media.videocontrols.picture-in-picture.video-toggle.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PictureInPicture\Enabled = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\PictureInPicture\Locked = 0x1 | 0x0

```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PictureInPicture/PictureInPicture_Enabled
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PictureInPicture/PictureInPicture_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>PictureInPicture</key>
  <dict>
    <key>Enabled</key>
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
    "PictureInPicture": {
      "Enabled": true | false,
      "Locked": true | false
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
### PostQuantumKeyAgreementEnabled
Enable post-quantum key agreement for TLS.

**Compatibility:** Firefox 127\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `security.tls.enable_kyber`, `network.http.http3.enable_kyber` (Firefox 128)

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PostQuantumKeyAgreementEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PostQuantumKeyAgreementEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>PostQuantumKeyAgreementEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PostQuantumKeyAgreementEnabled": true | false
  }
}
```
### Preferences
Set and lock preferences.

**NOTE** On Windows, in order to use this policy, you must clear all settings in the old **Preferences (Deprecated)** section in group policy.

Previously you could only set and lock a subset of preferences. Starting with Firefox 81 and Firefox ESR 78.3 you can set many more preferences. You can also set default preferences, user preferences and you can clear preferences.

**NOTE** There are too many preferences for us to provide documentation on them all. The source file [StaticPrefList.yaml](https://searchfox.org/mozilla-central/source/modules/libpref/init/StaticPrefList.yaml) contains information on many of them.

Preferences that start with the following prefixes are supported:
```
accessibility.
alerts.* (Firefox 122, Firefox ESR 115.7)
app.update.* (Firefox 86, Firefox ESR 78.8)
browser.
datareporting.policy.
dom.
extensions.
general.autoScroll (Firefox 83, Firefox ESR 78.5)
general.smoothScroll (Firefox 83, Firefox ESR 78.5)
geo.
gfx.
identity.fxaccounts.toolbar (Firefox 133)
intl.
keyword.enabled (Firefox 95, Firefox ESR 91.4)
layers.
layout.
mathml.disabled (Firefox 141, Firefox ESR 140.1)
media.
network.
pdfjs. (Firefox 84, Firefox ESR 78.6)
places.
pref.
print.
privacy.baselineFingerprintingProtection, privacy.baselineFingerprintingProtection.* (Firefox 141, Firefox ESR 140.1)
privacy.fingerprintingProtection, privacy.fingerprintingProtection.* (Firefox 141, Firefox ESR 140.1)
privacy.globalprivacycontrol.enabled (Firefox 127, Firefox ESR 128.0)
privacy.userContext.enabled (Firefox 126, Firefox ESR 115.11)
privacy.userContext.ui.enabled (Firefox 126, Firefox ESR 115.11)
signon. (Firefox 83, Firefox ESR 78.5)
spellchecker. (Firefox 84, Firefox ESR 78.6)
svg.context-properties.content.enabled (Firefox 141, Firefox ESR 140.1)
svg.disabled (Firefox 141, Firefox ESR 140.1)
toolkit.legacyUserProfileCustomizations.stylesheets (Firefox 95, Firefox ESR 91.4)
ui.
webgl.disabled (Firefox 141, Firefox ESR 140.1)
webgl.force-enabled (Firefox 141, Firefox ESR 140.1)
widget.
xpinstall.enabled (Firefox 141, Firefox ESR 140.1)
xpinstall.signatures.required (Firefox ESR 102.10, Firefox ESR only)
xpinstall.whitelist.required (Firefox 118, Firefox ESR 115.3)
```
as well as the following security preferences:

| Preference | Type | Default
| --- | --- | --- |
| security.csp.reporting.enabled | bool | true
| &nbsp;&nbsp;&nbsp;&nbsp;If set to false, disables CSP reporting. (Firefox 141, Firefox ESR 140.1)
| security.default_personal_cert | string | Ask Every Time
| &nbsp;&nbsp;&nbsp;&nbsp;If set to Select Automatically, Firefox automatically chooses the default personal certificate.
| security.disable_button.openCertManager | string | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If set to true and locked, the View Certificates button in preferences is disabled. (Firefox 121, Firefox ESR 115.6)
| security.disable_button.openDeviceManager | string | N/A
| &nbsp;&nbsp;&nbsp;&nbsp;If set to true and locked, the Security Devices button in preferences is disabled. (Firefox 121, Firefox ESR 115.6)
| security.insecure_connection_text.enabled | bool | false
| &nbsp;&nbsp;&nbsp;&nbsp;If set to true, adds the words "Not Secure" for insecure sites.
| security.insecure_connection_text.pbmode.enabled | bool | false
| &nbsp;&nbsp;&nbsp;&nbsp;If set to true, adds the words "Not Secure" for insecure sites in private browsing.
| security.mixed_content.block_active_content | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp;If set to true, mixed active content (HTTP subresources such as scripts, fetch requests, etc. on a HTTPS page) will be blocked.
| security.mixed_content.block_display_content | boolean | false
| &nbsp;&nbsp;&nbsp;&nbsp;If set to true, mixed passive/display content (HTTP subresources such as images, videos, etc. on a HTTPS page) will be blocked and ```security.mixed_content.upgrade_display_content``` will be ignored. (Firefox 127, Firefox ESR 128.0)
| security.mixed_content.upgrade_display_content | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp;If set to false, mixed passive/display content (HTTP subresources such as images, videos, etc. on a HTTPS page) will NOT be upgraded to HTTPS. (Firefox 127, Firefox ESR 128.0)
| security.osclientcerts.autoload | boolean | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, client certificates are loaded from the operating system certificate store.
| security.OCSP.enabled | integer | 1
| &nbsp;&nbsp;&nbsp;&nbsp;If 0, do not fetch OCSP. If 1, fetch OCSP for DV and EV certificates. If 2, fetch OCSP only for EV certificates.
| security.OCSP.require | boolean | false
| &nbsp;&nbsp;&nbsp;&nbsp; If true, if an OCSP request times out, the connection fails.
| security.osclientcerts.assume_rsa_pss_support | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp; If false, we don't assume an RSA key can do RSA-PSS. (Firefox 114, Firefox ESR 102.12)
| security.pki.certificate_transparency.disable_for_hosts  | |
| &nbsp;&nbsp;&nbsp;&nbsp; See [this page](https://searchfox.org/mozilla-central/rev/d1fbe983fb7720f0a4aca0e748817af11c1a374e/modules/libpref/init/StaticPrefList.yaml#16334) for more details.
| security.pki.certificate_transparency.disable_for_spki_hashes | |
| &nbsp;&nbsp;&nbsp;&nbsp; See [this page](https://searchfox.org/mozilla-central/rev/d1fbe983fb7720f0a4aca0e748817af11c1a374e/modules/libpref/init/StaticPrefList.yaml#16344) for more details.
| security.pki.certificate_transparency.mode | integer | 0
| &nbsp;&nbsp;&nbsp;&nbsp; Configures Certificate Transparency support mode (Firefox 133)
| security.ssl.enable_ocsp_stapling | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp; If false, OCSP stapling is not enabled.
| security.ssl.errorReporting.enabled | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, SSL errors cannot be sent to Mozilla.
| security.ssl.require_safe_negotiation | boolean | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, Firefox will only negotiate TLS connections with servers that indicate they support secure renegotiation. (Firefox 118, Firefox ESR 115.3)
| security.tls.enable_0rtt_data | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, TLS early data is turned off. (Firefox 93, Firefox 91.2, Firefox 78.15)
| security.tls.hello_downgrade_check | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, the TLS 1.3 downgrade check is disabled.
| security.tls.version.enable-deprecated | boolean | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, browser will accept TLS 1.0. and TLS 1.1. (Firefox 86, Firefox 78.8)
| security.warn_submit_secure_to_insecure | boolean | true
| &nbsp;&nbsp;&nbsp;&nbsp;If false, no warning is shown when submitting a form from https to http.
| security.webauthn.always_allow_direct_attestation | boolean | false
| &nbsp;&nbsp;&nbsp;&nbsp;If true, unnecessary (redundant) WebAuthn prompts are not shown.

Using the preference as the key, set the `Value` to the corresponding preference value.

`Status` can be "default", "locked", "user" or "clear"

* `"default"`: Read/Write: Settings appear as default even if factory default differs.
* `"locked"`: Read-Only: Settings appear as default even if factory default differs.
* `"user"`: Read/Write: Settings appear as changed if it differs from factory default.
* `"clear"`: Read/Write: `Value` has no effect. Resets to factory defaults on each startup.

`"user"` preferences persist across invocations of Firefox. It is the equivalent of a user setting the preference. They are most useful when a preference is needed very early in startup so it can't be set as default by policy. An example of this is ```toolkit.legacyUserProfileCustomizations.stylesheets```.

`"user"` preferences persist even if the policy is removed, so if you need to remove them, you should use the clear policy.

You can also set the `Type` starting in Firefox 123 and Firefox ESR 115.8. It can be `number`, `boolean` or `string`. This is especially useful if you are seeing 0 or 1 values being converted to booleans when set as user preferences.

See the examples below for more detail.

IMPORTANT: Make sure you're only setting a particular preference using this mechanism and not some other way.

Status
**Compatibility:** Firefox 81, Firefox ESR 78.3\
**CCK2 Equivalent:** `preferences`\
**Preferences Affected:** Many

#### Windows (GPO)
Software\Policies\Mozilla\Firefox\Preferences (REG_MULTI_SZ) =
```
{
  "accessibility.force_disabled": {
    "Value": 1,
    "Status": "default",
    "Type": "number"

  },
  "browser.cache.disk.parent_directory": {
    "Value": "SOME_NATIVE_PATH",
    "Status": "user"
  },
  "browser.tabs.warnOnClose": {
    "Value": false,
    "Status": "locked"
  }
}
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Preferences
```
Value (string):
```
<enabled/>
<data id="JSON" value='
{
  "accessibility.force_disabled": {
    "Value": 1,
    "Status": "default",
    "Type": "number"
  },
  "browser.cache.disk.parent_directory": {
    "Value": "SOME_NATIVE_PATH",
    "Status": "user"
  },
  "browser.tabs.warnOnClose": {
    "Value": false,
    "Status": "locked"
  }
}'/>
```
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PreferencesOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='{}'/>
```
#### macOS
```
<dict>
  <key>Preferences</key>
  <dict>
    <key>accessibility.force_disabled</key>
    <dict>
      <key>Value</key>
      <integer>1</integer>
      <key>Status</key>
      <string>default</string>
      <key>Type</key>
      <string>number</string>
    </dict>
    <key>browser.cache.disk.parent_directory</key>
    <dict>
      <key>Value</key>
      <string>SOME_NATIVE_PATH</string>
      <key>Status</key>
      <string>user</string>
    </dict>
    <key>browser.tabs.warnOnClose</key>
    <dict>
      <key>Value</key>
      <false/>
      <key>Status</key>
      <string>locked</string>
    </dict>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "Preferences": {
      "accessibility.force_disabled": {
        "Value": 1,
        "Status": "default"
        "Type": "number"
      },
      "browser.cache.disk.parent_directory": {
        "Value": "SOME_NATIVE_PATH",
        "Status": "user"
      },
      "browser.tabs.warnOnClose": {
        "Value": false,
        "Status": "locked"
      }
    }
  }
}
```
### PrimaryPassword
Require or prevent using a primary (formerly master) password.

If this value is true, a primary password is required. If this value is false, it works the same as if [`DisableMasterPasswordCreation`](#disablemasterpasswordcreation) was true and removes the primary password functionality.

If both DisableMasterPasswordCreation and PrimaryPassword are used, DisableMasterPasswordCreation takes precedent.

**Compatibility:** Firefox 79, Firefox ESR 78.1\
**CCK2 Equivalent:** `noMasterPassword`\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PrimaryPassword = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PrimaryPassword
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>PrimaryPassword</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PrimaryPassword": true | false
  }
}
```
### PrintingEnabled
Enable or disable printing.

**Compatibility:** Firefox 120, Firefox ESR 115.5\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `print.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PrintingEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PrintingEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>PrintingEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PrintingEnabled": true | false
  }
}
```
### PrivateBrowsingModeAvailability
Set availability of private browsing mode.

Possible values are `0` (Private Browsing mode is available), `1` (Private Browsing mode not available), and `2`(Private Browsing mode is forced).

This policy supersedes [`DisablePrivateBrowsing`](#disableprivatebrowsing)

Note: This policy missed Firefox ESR 128.2, but it will be in Firefox ESR 128.3.

**Compatibility:** Firefox 130, Firefox ESR 128.3\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\PrivateBrowsingModeAvailability = 0x0 | 0x1 | 0x2
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PrivateBrowsingModeAvailability
```
Value (string):
```
<enabled/>
<data id="PrivateBrowsingModeAvailability" value="0 | 1 | 2"/>
```
#### macOS
```
<dict>
  <key>PrivateBrowsingModeAvailability</key>
  <integer>0 | 1 | 2</integer>
</dict>
```
#### policies.json
```
{
  "policies": {
    "PrivateBrowsingModeAvailability": 0 | 1 | 2
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

Unless you lock this policy, changes the user already has in place will take effect.

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
**Preferences Affected:** `network.proxy.type`, `network.proxy.autoconfig_url`, `network.proxy.socks_remote_dns`, `signon.autologin.proxy`, `network.proxy.socks_version`, `network.proxy.no_proxies_on`, `network.proxy.share_proxy_settings`, `network.proxy.http`, `network.proxy.http_port`, `network.proxy.ftp`, `network.proxy.ftp_port`, `network.proxy.ssl`, `network.proxy.ssl_port`, `network.proxy.socks`, `network.proxy.socks_port`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\Proxy\Mode = "none" | "system" | "manual" | "autoDetect" | "autoConfig"
Software\Policies\Mozilla\Firefox\Proxy\Locked = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\Proxy\HTTPProxy = https://httpproxy.example.com
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
**Note**
These settings were moved to a category to make them easier to configure via Intune.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_Locked
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_ConnectionType
```
Value (string):
```
<enabled/>
<data id="Proxy_ConnectionType" value="none | system | manual | autoDetect | autoConfig"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_HTTPProxy
```
Value (string):
```
<enabled/>
<data id="Proxy_HTTPProxy" value="httpproxy.example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_UseHTTPProxyForAllProtocols
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_SSLProxy
```
Value (string):
```
<enabled/>
<data id="Proxy_SSLProxy" value="sslproxy.example.com"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_SOCKSProxy
```
Value (string):
```
<enabled/>
<data id="Proxy_SOCKSProxy" value="socksproxy.example.com"/>
<data id="Proxy_SOCKSVersion" value="4 | 5"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_AutoConfigURL
```
Value (string):
```
<enabled/>
<data id="Proxy_AutoConfigURL" value="URL_TO_AUTOCONFIG"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_Passthrough
```
Value (string):
```
<enabled/>
<data id="Proxy_Passthrough" value="&lt;local&gt;"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_AutoLogin
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_UseProxyForDNS
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI (Old way):
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Proxy
```
Value (string):
```
<enabled/>
<data id="ProxyLocked" value="true | false"/>
<data id="ConnectionType" value="none | system | manual | autoDetect | autoConfig"/>
<data id="HTTPProxy" value="httpproxy.example.com"/>
<data id="UseHTTPProxyForAllProtocols" value="true | false"/>
<data id="SSLProxy" value="sslproxy.example.com"/>
<data id="FTPProxy" value="ftpproxy.example.com"/>
<data id="SOCKSProxy" value="socksproxy.example.com"/>
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
      "Mode": "none" | "system" | "manual" | "autoDetect" | "autoConfig",
      "Locked": true | false,
      "HTTPProxy": "hostname",
      "UseHTTPProxyForAllProtocols": true | false,
      "SSLProxy": "hostname",
      "FTPProxy": "hostname",
      "SOCKSProxy": "hostname",
      "SOCKSVersion": 4 | 5,
      "Passthrough": "<local>",
      "AutoConfigURL": "URL_TO_AUTOCONFIG",
      "AutoLogin": true | false,
      "UseProxyForDNS": true | false
    }
  }
}
```
### RequestedLocales
Set the list of requested locales for the application in order of preference. It will cause the corresponding language pack to become active.

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
Clear data on shutdown.

Note: Starting with Firefox 136, FormData and History have been separated again.

`Cache`

`Cookies`

`Downloads` Download History (*Deprecated - part of History*)

`FormData` Form History

`History` Browsing History, Download History

`Sessions` Active Logins

`SiteSettings` Site Preferences

`OfflineApps` Offline Website Data (*Deprecated - part of Cookies*)

`Locked` prevents the user from changing these preferences.

**Compatibility:** Firefox 68, Firefox ESR 68 (Locked added in 74/68.6, History update in Firefox 128)\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown`, `privacy.clearOnShutdown.cache`, `privacy.clearOnShutdown.cookies`, `privacy.clearOnShutdown.downloads`, `privacy.clearOnShutdown.formdata`, `privacy.clearOnShutdown.history`, `privacy.clearOnShutdown.sessions`, `privacy.clearOnShutdown.siteSettings`, `privacy.clearOnShutdown.offlineApps`, `privacy.clearOnShutdown_v2.historyFormDataAndDownloads` (Firefox 128), `privacy.clearOnShutdown_v2.cookiesAndStorage` (Firefox 128), `privacy.clearOnShutdown_v2.cache` (Firefox 128), `privacy.clearOnShutdown_v2.siteSettings` (Firefox 128), `privacy.clearOnShutdown_v2.formdata` (Firefox 128)

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Cache = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Cookies = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\FormData = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\History = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Sessions = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\SiteSettings = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\SanitizeOnShutdown\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/A_SanitizeOnShutdown_Cache
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/B_SanitizeOnShutdown_Cookies
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/E_SanitizeOnShutdown_FormData
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/E_SanitizeOnShutdown_History
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/F_SanitizeOnShutdown_Sessions
```
Value (string):
```
<enabled/> or <disabled/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/G_SanitizeOnShutdown_SiteSettings
```
Value (string):
```
<enabled/> or <disabled/>
```
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
    <key>FormData</key>
    <true/> | <false/>
    <key>History</key>
    <true/> | <false/>
    <key>Sessions</key>
    <true/> | <false/>
    <key>SiteSettings</key>
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
      "FormData": true | false,
      "History": true | false,
      "Sessions": true | false,
      "SiteSettings": true | false,
      "Locked": true | false
    }
  }
}
```
### SanitizeOnShutdown (All)
Clear all data on shutdown, including Browsing & Download History, Cookies, Active Logins, Cache, Form History, Site Preferences and Offline Website Data.

**Compatibility:** Firefox 60, Firefox ESR 60\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `privacy.sanitize.sanitizeOnShutdown`, `privacy.clearOnShutdown.cache`, `privacy.clearOnShutdown.cookies`, `privacy.clearOnShutdown.downloads`, `privacy.clearOnShutdown.formdata`, `privacy.clearOnShutdown.history`, `privacy.clearOnShutdown.sessions`, `privacy.clearOnShutdown.siteSettings`, `privacy.clearOnShutdown.offlineApps`
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
<data id="SearchBar" value="unified | separate"/>
```
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

### SearchEngines

As of Firefox 139, this policy is available in all versions of Firefox.

### SearchEngines | Add

Add new search engines. Although there are only five engines available in the ADMX template, there is no limit. To add more in the ADMX template, you can duplicate the XML.

`Name` is the name of the search engine. (Required)

`URLTemplate` is the search URL with {searchTerms} to substitute for the search term. (Required)

`Method` is either GET or POST

`IconURL` is a URL for the icon to use.

`Alias` is a keyword to use for the engine.

`Description` is a description of the search engine.

`PostData` is the POST data as name value pairs separated by &.

`SuggestURLTemplate` is a search suggestions URL with {searchTerms} to substitute for the search term.

`Encoding` is the query charset for the engine. It defaults to UTF-8.

**Compatibility:** Firefox 139, Firefox ESR 60 (POST support in Firefox ESR 68, Encoding support in Firefox 91)\
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
### SearchEngines | Default

Set the default search engine.

**Compatibility:** Firefox 139, Firefox ESR 60\
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

**Compatibility:** Firefox 139, Firefox ESR 60\
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

Hide built-in search engines.

**Compatibility:** Firefox 139, Firefox ESR 60.2\
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
### SearchSuggestEnabled

Enable search suggestions.

**Compatibility:** Firefox 68, Firefox ESR 68\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.urlbar.suggest.searches`, `browser.search.suggest.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SearchSuggestEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchSuggestEnabled
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

Add or delete PKCS #11 modules.

**Compatibility:** Firefox 114, Firefox ESR 112.12\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SecurityDevices\Add\NAME_OF_DEVICE_TO_ADD = PATH_TO_LIBRARY_FOR_DEVICE
Software\Policies\Mozilla\Firefox\SecurityDevices\Remove\1 = NAME_OF_DEVICE_TO_REMOVE
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SecurityDevices/SecurityDevices_Add
```
Value (string):
```
<enabled/>
<data id="SecurityDevices" value="NAME_OF_DEVICE_TO_ADD&#xF000;PATH_TO_LIBRARY_FOR_DEVICE"/>
```
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SecurityDevices/SecurityDevices_Delete
```
Value (string):
```
<enabled/>
<data id="SecurityDevices" value="1&#xF000;NAME_OF_DEVICE_TO_REMOVE"/>
```
#### macOS
```
<dict>
  <key>SecurityDevices</key>
  <dict>
    <key>Add<key>
    <dict>
      <key>NAME_OF_DEVICE_TO_ADD</key>
      <string>PATH_TO_LIBRARY_FOR_DEVICE</string>
    </dict>
    <key>Delete</add>
    <array>
      <string>NAME_OF_DEVICE_TO_DELETE</string>
    </array>
  </dict>
</dict>
```
#### policies.json
```
{
  "policies": {
    "SecurityDevices": {
      "Add": {
        "NAME_OF_DEVICE_TO_ADD": "PATH_TO_LIBRARY_FOR_DEVICE"
      },
      "Delete": ["NAME_OF_DEVICE_TO_DELETE"]
    }
  }
}
```
### SecurityDevices (Deprecated)

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
### ShowHomeButton
Show the home button on the toolbar.

Future versions of Firefox will not show the home button by default.

**Compatibility:** Firefox 88, Firefox ESR 78.10\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\ShowHomeButton = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/Homepage_ShowHomeButton
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>ShowHomeButton</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "ShowHomeButton": true | false
  }
}
```
### SkipTermsOfUse
If true, don't display the Firefox [Terms of Use](https://www.mozilla.org/about/legal/terms/firefox/) and [Privacy Notice](https://www.mozilla.org/privacy/firefox/) upon startup. You represent that you accept and have the authority to accept the Terms of Use on behalf of all individuals to whom you provide access to this browser.

**Compatibility:** Firefox 138, Firefox ESR 140\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** N/A

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\SkipTermsOfUse = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SkipTermsOfUse
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>SkipTermsOfUse</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "SkipTermsOfUse": true | false
  }
}
```
### SSLVersionMax

Set and lock the maximum version of TLS. (Firefox defaults to a maximum of TLS 1.3.)

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

Set and lock the minimum version of TLS. (Firefox defaults to a minimum of TLS 1.2.)

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
### StartDownloadsInTempDirectory
Force downloads to start off in a local, temporary location rather than the default download directory.

**Compatibility:** Firefox 102\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.download.start_downloads_in_tmp_dir`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\StartDownloadsInTempDirectory = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/StartDownloadsInTempDirectory
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>StartDownloadsInTempDirectory</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "StartDownloadsInTempDirectory": true | false
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
<data id="SupportMenuAccessKey" value="S"/>
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
### TranslateEnabled
Enable or disable webpage translation.

Note: Web page translation is done completely on the client, so there is no data or privacy risk.

If you only want to disable the popup, you can set the pref `browser.translations.automaticallyPopup` to false using the [Preferences](#preferences) policy.

**Compatibility:** Firefox 126\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.translations.enable`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\TranslateEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/TranslateEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>TranslateEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "TranslateEnabled": true | false
  }
}
```
### UserMessaging

Prevent Firefox from messaging the user in certain situations.

`WhatsNew` Remove the "What's New" icon and menuitem. (*Deprecated*)

`ExtensionRecommendations` If false, don't recommend extensions while the user is visiting web pages.

`FeatureRecommendations` If false, don't recommend browser features.

`UrlbarInterventions` If false, don't offer Firefox specific suggestions in the URL bar.

`SkipOnboarding` If true, don't show onboarding messages on the new tab page.

`MoreFromMozilla` If false, don't show the "More from Mozilla" section in Preferences. (Firefox 98)

`FirefoxLabs` If false, don't show the "Firefox Labs" section in Preferences. (Firefox 130.0.1)

Note: Firefox Labs is now controlled by Nimbus, our testing platform, so disabling telemetry also disables Firefox Labs.

`Locked` prevents the user from changing user messaging preferences.

**Compatibility:** Firefox 75, Firefox ESR 68.7\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.newtabpage.activity-stream.asrouter.userprefs.cfr.addons`, `browser.newtabpage.activity-stream.asrouter.userprefs.cfr.features`, `browser.aboutwelcome.enabled`, `browser.preferences.moreFromMozilla`, `browser.preferences.experimental`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\UserMessaging\ExtensionRecommendations = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\FeatureRecommendations = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\UrlbarInterventions = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\SkipOnboarding = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\MoreFromMozilla = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\FirefoxLabs = 0x1 | 0x0
Software\Policies\Mozilla\Firefox\UserMessaging\Locked = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_ExtensionRecommendations
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_FeatureRecommendations
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_UrlbarInterventions
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_SkipOnboarding
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_MoreFromMozilla
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_FirefoxLabs
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_Locked
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
    <key>ExtensionRecommendations</key>
    <true/> | <false/>
    <key>FeatureRecommendations</key>
    <true/> | <false/>
    <key>UrlbarInterventions</key>
    <true/> | <false/>
    <key>SkipOnboarding</key>
    <true/> | <false/>
    <key>MoreFromMozilla</key>
    <true/> | <false/>
    <key>FirefoxLabs</key>
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
    "UserMessaging": {
      "ExtensionRecommendations": true | false,
      "FeatureRecommendations": true | false,
      "UrlbarInterventions": true | false,
      "SkipOnboarding": true | false,
      "MoreFromMozilla": true | false,
      "FirefoxLabs": true | false,
      "Locked": true | false
    }
  }
}
```
### UseSystemPrintDialog
Use the system print dialog instead of the print preview window.

**Compatibility:** Firefox 102\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `print.prefer_system_dialog`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\UseSystemPrintDialog = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/UseSystemPrintDialog
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>UseSystemPrintDialog</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "UseSystemPrintDialog": true | false
  }
}
```
### VisualSearchEnabled
Enable or disable visual search.

**Compatibility:** Firefox 144\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `browser.search.visualSearch.featureGate`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\VisualSearchEnabled = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/VisualSearchEnabled
```
Value (string):
```
<enabled/> or <disabled/>
```
#### macOS
```
<dict>
  <key>VisualSearchEnabled</key>
  <true/> | <false/>
</dict>
```
#### policies.json
```
{
  "policies": {
    "VisualSearchEnabled": true | false
  }
}
```
### WebsiteFilter
Block websites from being visited. The parameters take an array of Match Patterns, as documented in https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Match_patterns.
The arrays are limited to 1000 entries each.

If you want to block all URLs, you can use `<all_urls>` or `*://*/*`. You can't have just a `*` on the right side.

For specific protocols, use `https://*/*` or `http://*/*`.

As of Firefox 83 and Firefox ESR 78.5, file URLs are supported.

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
<enabled/> <data id="WebsiteFilter" value="1&#xF000;&#60;all_urls&#62;"/>
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
If you are using custom ADMX and ADML administrative templates in Intune, you can use this OMA-URI instead
to workaround the limit on the length of strings. Put all of your JSON on one line.

OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/WebsiteFilterOneLine
```
Value (string):
```
<enabled/>
<data id="JSONOneLine" value='{"Block": ["<all_urls>"],"Exceptions": ["http://example.org/*"]}'/>
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
### WindowsSSO
Allow Windows single sign-on for Microsoft, work, and school accounts.

If this policy is set to true, Firefox will use credentials stored in Windows to sign in to Microsoft, work, and school accounts.

**Compatibility:** Firefox 91\
**CCK2 Equivalent:** N/A\
**Preferences Affected:** `network.http.windows-sso.enabled`

#### Windows (GPO)
```
Software\Policies\Mozilla\Firefox\WindowsSSO = 0x1 | 0x0
```
#### Windows (Intune)
OMA-URI:
```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/WindowsSSO
```
Value (string):
```
<enabled/> or <disabled/>
```
#### policies.json
```
{
  "policies": {
    "WindowsSSO": true | false
  }
}
```
