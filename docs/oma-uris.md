# Firefox ADMX OMA-URIs for Intune

Auto-generated from `windows/firefox.admx` (revision `7.12`). Do not edit by hand.

Entries are keyed by the JSON policy name (as used in `policies.json`), with the GPMC display path shown in parentheses. Policies marked "(Deprecated)" in the ADML are omitted. Numbered families (e.g. `Bookmark01`-`Bookmark50`) are collapsed into a single entry with an `NN` placeholder in the URI.

Value templates are best-effort. For policies whose value is a JSON blob (e.g. `ExtensionSettings`, `ManagedBookmarks`, `Bookmarks`, `Containers`, `Handlers`, `Preferences`, `WebsiteFilter`, `AutoLaunchProtocolsFromOrigins`, `ExemptDomainFileTypePairsFromFileTypeDownloadWarnings`) see the [policy documentation](https://firefox-admin-docs.mozilla.org/) for the value shape.

## AIControls.Default.Locked (AI Controls > Default > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~Default/Default_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.Default.Value (AI Controls > Default > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~Default/Default_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AIControls.LinkPreviewKeyPoints.Locked (AI Controls > Key Points in Link Previews > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~LinkPreviewKeyPoints/LinkPreviewKeyPoints_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.LinkPreviewKeyPoints.Value (AI Controls > Key Points in Link Previews > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~LinkPreviewKeyPoints/LinkPreviewKeyPoints_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AIControls.PDFAltText.Locked (AI Controls > PDF Image Alt Text > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~PDFAltText/PDFAltText_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.PDFAltText.Value (AI Controls > PDF Image Alt Text > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~PDFAltText/PDFAltText_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AIControls.SidebarChatbot.Locked (AI Controls > Chatbot in Sidebar > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~SidebarChatbot/SidebarChatbot_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.SidebarChatbot.Value (AI Controls > Chatbot in Sidebar > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~SidebarChatbot/SidebarChatbot_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AIControls.SmartTabGroups.Locked (AI Controls > Tab Group Suggestions > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~SmartTabGroups/SmartTabGroups_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.SmartTabGroups.Value (AI Controls > Tab Group Suggestions > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~SmartTabGroups/SmartTabGroups_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AIControls.SmartWindow.Locked (AI Controls > Smart Window > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~SmartWindow/SmartWindow_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.SmartWindow.Value (AI Controls > Smart Window > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~SmartWindow/SmartWindow_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AIControls.Translations.Locked (AI Controls > Translations > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~Translations/Translations_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## AIControls.Translations.Value (AI Controls > Translations > Value)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~AIControls~Translations/Translations_Value
```

**Value:**

```
<enabled/>
<data id="AIControls_Value" value="available | blocked"/>
```

## AllowedDomainsForApps (Define domains allowed to access Google Workspace)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AllowedDomainsForApps
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## AllowFileSelectionDialogs (Allow File Selection Dialogs)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AllowFileSelectionDialogs
```

**Value:**

```
<enabled/> or <disabled/>
```

## AppAutoUpdate (Application Autoupdate)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppAutoUpdate
```

**Value:**

```
<enabled/> or <disabled/>
```

## AppUpdatePin (Pin updates to a specific version)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppUpdatePin
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## AppUpdateURL (Custom Update URL)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AppUpdateURL
```

**Value:**

```
<enabled/>
<data id="AppUpdateURL" value="STRING"/>
```

## Authentication.AllowNonFQDN (Authentication > Allow Non FQDN)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_AllowNonFQDN
```

**Value:**

```
<enabled/>
<data id="Authentication_AllowNonFQDN_NTLM" value="true | false"/>
<data id="Authentication_AllowNonFQDN_SPNEGO" value="true | false"/>
```

## Authentication.AllowProxies (Authentication > Allow Proxies)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_AllowProxies
```

**Value:**

```
<enabled/>
<data id="Authentication_AllowProxies_NTLM" value="true | false"/>
<data id="Authentication_AllowProxies_SPNEGO" value="true | false"/>
```

## Authentication.Delegated (Authentication > Delegated)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_Delegated
```

**Value:**

```
<enabled/>
<data id="Authentication" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Authentication.Locked (Authentication > Do not allow authentication preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Authentication.NTLM (Authentication > NTLM)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_NTLM
```

**Value:**

```
<enabled/>
<data id="Authentication" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Authentication.PrivateBrowsing (Authentication > Allow authentication in private browsing)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_PrivateBrowsing
```

**Value:**

```
<enabled/> or <disabled/>
```

## Authentication.SPNEGO (Authentication > SPNEGO)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Authentication/Authentication_SPNEGO
```

**Value:**

```
<enabled/>
<data id="Authentication" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## AutofillAddressEnabled (Enable autofill for addresses)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutofillAddressEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## AutofillCreditCardEnabled (Enable autofill for payment methods)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutofillCreditCardEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## AutoLaunchProtocolsFromOrigins (Auto Launch Protocols From Origins (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutoLaunchProtocolsFromOriginsOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## AutoLaunchProtocolsFromOrigins (Auto Launch Protocols From Origins)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/AutoLaunchProtocolsFromOrigins
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## BackgroundAppUpdate (Background updater)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BackgroundAppUpdate
```

**Value:**

```
<enabled/> or <disabled/>
```

## BlockAboutAddons (Block Add-ons Manager)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutAddons
```

**Value:**

```
<enabled/> or <disabled/>
```

## BlockAboutConfig (Block about:config)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutConfig
```

**Value:**

```
<enabled/> or <disabled/>
```

## BlockAboutProfiles (Block about:profiles)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutProfiles
```

**Value:**

```
<enabled/> or <disabled/>
```

## BlockAboutSupport (Block Troubleshooting Information)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/BlockAboutSupport
```

**Value:**

```
<enabled/> or <disabled/>
```

## Bookmarks (Bookmarks > Bookmarks (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Bookmarks/A_BookmarksOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## Bookmarks (Bookmarks > Bookmarks (JSON))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Bookmarks/A_Bookmarks
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## Bookmarks[N] (Bookmarks > Bookmark 01 - Bookmark 50)

Replace `NN` with the numeric suffix from `Bookmark01` through `Bookmark50` (50 slots).

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Bookmarks/BookmarkNN
```

**Value:**

```
<enabled/>
<data id="BookmarkTitle" value="STRING"/>
<data id="BookmarkURL" value="STRING"/>
<data id="BookmarkFolder" value="STRING"/>
<data id="BookmarkFavicon" value="STRING"/>
<data id="BookmarkPlacement" value="toolbar | menu"/>
```

## BrowserDataBackup.AllowBackup (Browser Data Backup > Allow Backup)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~BrowserDataBackup/BrowserDataBackup_AllowBackup
```

**Value:**

```
<enabled/> or <disabled/>
```

## BrowserDataBackup.AllowRestore (Browser Data Backup > Allow Restore)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~BrowserDataBackup/BrowserDataBackup_AllowRestore
```

**Value:**

```
<enabled/> or <disabled/>
```

## CaptivePortal (Captive Portal)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/CaptivePortal
```

**Value:**

```
<enabled/> or <disabled/>
```

## Certificates.ImportEnterpriseRoots (Certificates > Import Enterprise Roots)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Certificates/Certificates_ImportEnterpriseRoots
```

**Value:**

```
<enabled/> or <disabled/>
```

## Containers (Containers (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ContainersOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## Containers (Containers)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Containers
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## ContentAnalysis.AgentName (Content Analysis (DLP) > Agent Name)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_AgentName
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## ContentAnalysis.AgentTimeout (Content Analysis (DLP) > Agent Timeout)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_AgentTimeout
```

**Value:**

```
<enabled/>
<data id="Number" value="0"/>
```

## ContentAnalysis.AllowUrlRegexList (Content Analysis (DLP) > Allow Url Regex List)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_AllowUrlRegexList
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## ContentAnalysis.BypassForSameTabOperations (Content Analysis (DLP) > Bypass For Same Tab Operations)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_BypassForSameTabOperations
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.ClientSignature (Content Analysis (DLP) > Client Signature)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_ClientSignature
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## ContentAnalysis.DefaultResult (Content Analysis (DLP) > Default Result)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_DefaultResult
```

**Value:**

```
<enabled/>
<data id="ContentAnalysis_DefaultResult" value="0 | 1 | 2"/>
```

## ContentAnalysis.DenyUrlRegexList (Content Analysis (DLP) > Deny Url Regex List)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_DenyUrlRegexList
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## ContentAnalysis.Enabled (Content Analysis (DLP) > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.Clipboard.Enabled (Content Analysis (DLP) > Interception Points > Clipboard > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~InterceptionPoints_Clipboard/ContentAnalysis_InterceptionPoints_Clipboard
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.Clipboard.PlainTextOnly (Content Analysis (DLP) > Interception Points > Clipboard > Plain Text Only)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~InterceptionPoints_Clipboard/ContentAnalysis_InterceptionPoints_Clipboard_PlainTextOnly
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.Download.Enabled (Content Analysis (DLP) > Interception Points > Download)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints/ContentAnalysis_InterceptionPoints_Download
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.DragAndDrop.Enabled (Content Analysis (DLP) > Interception Points > Drag And Drop > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~InterceptionPoints_DragAndDrop/ContentAnalysis_InterceptionPoints_DragAndDrop
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.DragAndDrop.PlainTextEnabled (Content Analysis (DLP) > Interception Points > Drag And Drop > Plain Text Only)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints~InterceptionPoints_DragAndDrop/ContentAnalysis_InterceptionPoints_DragAndDrop_PlainTextOnly
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.FileUpload.Enabled (Content Analysis (DLP) > Interception Points > File Upload)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints/ContentAnalysis_InterceptionPoints_FileUpload
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.InterceptionPoints.Print.Enabled (Content Analysis (DLP) > Interception Points > Print)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis~InterceptionPoints/ContentAnalysis_InterceptionPoints_Print
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.IsPerUser (Content Analysis (DLP) > Is Per User)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_IsPerUser
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.PipePathName (Content Analysis (DLP) > Pipe Path Name)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_PipePathName
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## ContentAnalysis.ShowBlockedResult (Content Analysis (DLP) > Show Blocked Result)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_ShowBlockedResult
```

**Value:**

```
<enabled/> or <disabled/>
```

## ContentAnalysis.TimeoutResult (Content Analysis (DLP) > Timeout Result)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ContentAnalysis/ContentAnalysis_TimeoutResult
```

**Value:**

```
<enabled/>
<data id="ContentAnalysis_TimeoutResult" value="0 | 1 | 2"/>
```

## Cookies.Allow (Cookies > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Cookies.AllowSession (Cookies > Allowed Sites (Session Only))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_AllowSession
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Cookies.Behavior (Cookies > Cookie Behavior)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Behavior
```

**Value:**

```
<enabled/>
<data id="Cookies_Behavior" value="accept | reject-foreign | reject | limit-foreign | reject-tracker | reject-tracker-and-partition-foreign"/>
```

## Cookies.BehaviorPrivateBrowsing (Cookies > Cookie Behavior in private browsing)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_BehaviorPrivateBrowsing
```

**Value:**

```
<enabled/>
<data id="Cookies_BehaviorPrivateBrowsing" value="accept | reject-foreign | reject | limit-foreign | reject-tracker | reject-tracker-and-partition-foreign"/>
```

## Cookies.Block (Cookies > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Cookies.ExpireAtSessionEnd (Cookies > Keep cookies until Firefox is closed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_ExpireAtSessionEnd
```

**Value:**

```
<enabled/> or <disabled/>
```

## Cookies.Locked (Cookies > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Cookies/Cookies_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## CustomizeFirefoxHome (Customize Firefox Home (Moved to category))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/CustomizeFirefoxHome
```

**Value:**

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

## DefaultDownloadDirectory (Default Download Directory)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DefaultDownloadDirectory
```

**Value:**

```
<enabled/>
<data id="Preferences_String" value="STRING"/>
```

## DefaultSerialGuardSetting (Control use of the Web Serial API)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DefaultSerialGuardSetting
```

**Value:**

```
<enabled/>
<data id="DefaultSerialGuardSetting" value="2 | 3"/>
```

## DisableAppUpdate (Disable Update)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableAppUpdate
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableBuiltinPDFViewer (Disable Built-in PDF Viewer (PDF.js))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableBuiltinPDFViewer
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_AES_128_GCM_SHA256 (Disabled Ciphers > TLS_AES_128_GCM_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_AES_128_GCM_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_AES_256_GCM_SHA384 (Disabled Ciphers > TLS_AES_256_GCM_SHA384)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_AES_256_GCM_SHA384
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_CHACHA20_POLY1305_SHA256 (Disabled Ciphers > TLS_CHACHA20_POLY1305_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_CHACHA20_POLY1305_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_DHE_RSA_WITH_AES_128_CBC_SHA (Disabled Ciphers > TLS_DHE_RSA_WITH_AES_128_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_DHE_RSA_WITH_AES_128_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_DHE_RSA_WITH_AES_256_CBC_SHA (Disabled Ciphers > TLS_DHE_RSA_WITH_AES_256_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_DHE_RSA_WITH_AES_256_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA (Disabled Ciphers > TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (Disabled Ciphers > TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA (Disabled Ciphers > TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 (Disabled Ciphers > TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 (Disabled Ciphers > TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (Disabled Ciphers > TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (Disabled Ciphers > TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (Disabled Ciphers > TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (Disabled Ciphers > TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (Disabled Ciphers > TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_RSA_WITH_3DES_EDE_CBC_SHA (Disabled Ciphers > TLS_RSA_WITH_3DES_EDE_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_3DES_EDE_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_RSA_WITH_AES_128_CBC_SHA (Disabled Ciphers > TLS_RSA_WITH_AES_128_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_AES_128_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_RSA_WITH_AES_128_GCM_SHA256 (Disabled Ciphers > TLS_RSA_WITH_AES_128_GCM_SHA256)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_AES_128_GCM_SHA256
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_RSA_WITH_AES_256_CBC_SHA (Disabled Ciphers > TLS_RSA_WITH_AES_256_CBC_SHA)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_AES_256_CBC_SHA
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisabledCiphers.TLS_RSA_WITH_AES_256_GCM_SHA384 (Disabled Ciphers > TLS_RSA_WITH_AES_256_GCM_SHA384)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DisabledCiphers/DisabledCiphers_TLS_RSA_WITH_AES_256_GCM_SHA384
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableDefaultBrowserAgent (Disable the default browser agent)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableDefaultBrowserAgent
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableDeveloperTools (Disable Developer Tools)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableDeveloperTools
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableEncryptedClientHello (Disable Encrypted Client Hello)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableEncryptedClientHello
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableFeedbackCommands (Disable Feedback Commands)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFeedbackCommands
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableFirefoxAccounts (Disable Firefox Accounts)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFirefoxAccounts
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableFirefoxScreenshots (Disable Firefox Screenshots)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFirefoxScreenshots
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableFirefoxStudies (Disable Firefox Studies)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFirefoxStudies
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableForgetButton (Disable Forget Button)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableForgetButton
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableFormHistory (Disable Form History)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableFormHistory
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableMasterPasswordCreation (Disable Master Password Creation)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableMasterPasswordCreation
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisablePasswordReveal (Do not allow passwords to be revealed in saved logins)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisablePasswordReveal
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisablePrivateBrowsing (Disable Private Browsing)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisablePrivateBrowsing
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableProfileImport (Disable Profile Import)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableProfileImport
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableProfileRefresh (Disable Profile Refresh)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableProfileRefresh
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableRemoteImprovements (Disable Remote Improvements)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableRemoteImprovements
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableSafeMode (Disable Safe Mode)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableSafeMode
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableSecurityBypass.InvalidCertificate (Prevent overriding certificate errors)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/P_DisableSecurityBypass_InvalidCertificate
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableSecurityBypass.SafeBrowsing (Prevent overriding safe browsing errors)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/P_DisableSecurityBypass_SafeBrowsing
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableSetDesktopBackground (Disable Set Desktop Background)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableSetDesktopBackground
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableSystemAddonUpdate (Disable System Addon Updates)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableSystemAddonUpdate
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableTelemetry (Disable Telemetry)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableTelemetry
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisableThirdPartyModuleBlocking (Disable Third Party Module Blocking)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisableThirdPartyModuleBlocking
```

**Value:**

```
<enabled/> or <disabled/>
```

## DisplayBookmarksToolbar (Display Bookmarks Toolbar)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisplayBookmarksToolbar_Enum
```

**Value:**

```
<enabled/>
<data id="DisplayBookmarksToolbar" value="always | never | newtab"/>
```

## DisplayMenuBar (Display Menu Bar)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DisplayMenuBar_Enum
```

**Value:**

```
<enabled/>
<data id="DisplayMenuBar" value="always | never | default-on | default-off"/>
```

## DNSOverHTTPS.Enabled (DNS Over HTTPS > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## DNSOverHTTPS.ExcludedDomains (DNS Over HTTPS > Excluded Domains)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_ExcludedDomains
```

**Value:**

```
<enabled/>
<data id="List" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## DNSOverHTTPS.Fallback (DNS Over HTTPS > Fallback)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_Fallback
```

**Value:**

```
<enabled/> or <disabled/>
```

## DNSOverHTTPS.Locked (DNS Over HTTPS > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## DNSOverHTTPS.ProviderURL (DNS Over HTTPS > Provider URL)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~DNSOverHTTPS/DNSOverHTTPS_ProviderURL
```

**Value:**

```
<enabled/>
<data id="String" value="STRING"/>
```

## DontCheckDefaultBrowser (Don't Check Default Browser)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DontCheckDefaultBrowser
```

**Value:**

```
<enabled/> or <disabled/>
```

## DownloadDirectory (Download Directory)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/DownloadDirectory
```

**Value:**

```
<enabled/>
<data id="Preferences_String" value="STRING"/>
```

## EnableTrackingProtection.BaselineExceptions (Tracking Protection > Baseline Exceptions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/I_TrackingProtection_BaselineExceptions
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.Category (Tracking Protection > Tracking Protection Mode)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/G_TrackingProtection_Category
```

**Value:**

```
<enabled/>
<data id="TrackingProtection_Category" value="strict | standard"/>
```

## EnableTrackingProtection.ConvenienceExceptions (Tracking Protection > Convenience Exceptions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/J_TrackingProtection_ConvenienceExceptions
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.Cryptomining (Tracking Protection > Cryptomining)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/B_TrackingProtection_Cryptomining
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.EmailTracking (Tracking Protection > Email Tracking)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/F_TrackingProtection_EmailTracking
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.Exceptions (Tracking Protection > Exceptions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/D_TrackingProtection_Exceptions
```

**Value:**

```
<enabled/>
<data id="TrackingProtection_Exceptions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## EnableTrackingProtection.Fingerprinting (Tracking Protection > Fingerprinting)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/C_TrackingProtection_Fingerprinting
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.Locked (Tracking Protection > Do not allow tracking protection preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/E_TrackingProtection_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.SuspectedFingerprinting (Tracking Protection > Suspected Fingerprinting)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/H_TrackingProtection_SuspectedFingerprinting
```

**Value:**

```
<enabled/> or <disabled/>
```

## EnableTrackingProtection.Value (Tracking Protection > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~TrackingProtection/A_TrackingProtection_Value
```

**Value:**

```
<enabled/> or <disabled/>
```

## EncryptedMediaExtensions.Enabled (Encrypted Media Extensions > Enable Encrypted Media Extensions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~EncryptedMediaExtensions/EncryptedMediaExtensions_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## EncryptedMediaExtensions.Locked (Encrypted Media Extensions > Lock Encrypted Media Extensions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~EncryptedMediaExtensions/EncryptedMediaExtensions_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## ExemptDomainFileTypePairsFromFileTypeDownloadWarnings (Disable warnings based on file extension for specific file types on domains (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ExemptDomainFileTypePairsFromFileTypeDownloadWarningsOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## ExemptDomainFileTypePairsFromFileTypeDownloadWarnings (Disable warnings based on file extension for specific file types on domains)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ExemptDomainFileTypePairsFromFileTypeDownloadWarnings
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## Extensions.Install (Extensions > Extensions to Install)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/Extensions_Install
```

**Value:**

```
<enabled/>
<data id="Extensions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Extensions.Locked (Extensions > Prevent extensions from being disabled or removed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/Extensions_Locked
```

**Value:**

```
<enabled/>
<data id="Extensions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Extensions.Uninstall (Extensions > Extensions to Uninstall)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/Extensions_Uninstall
```

**Value:**

```
<enabled/>
<data id="Extensions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## ExtensionSettings (Extensions > Extension Management)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionSettings
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## ExtensionSettings (Extensions > Extension Management (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionSettingsOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## ExtensionUpdate (Extensions > Extension Update)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Extensions/ExtensionUpdate
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.Highlights (Firefox Home > Recent Activity)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_Highlights
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.Locked (Firefox Home > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.Search (Firefox Home > Search)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_Search
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.SponsoredStories (Firefox Home > Sponsored Stories)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_SponsoredStories
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.SponsoredTopSites (Firefox Home > Sponsored Shortcuts)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_SponsoredTopSites
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.Stories (Firefox Home > Stories)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_Stories
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.TopSites (Firefox Home > Shortcuts)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_TopSites
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxHome.Weather (Firefox Home > Weather)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxHome/FirefoxHome_Weather
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxSuggest.ImproveSuggest (Firefox Suggest (US only) > Improve the Firefox Suggest experience)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_ImproveSuggest
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxSuggest.Locked (Firefox Suggest (US only) > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxSuggest.SponsoredSuggestions (Firefox Suggest (US only) > Suggestions from sponsors)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_SponsoredSuggestions
```

**Value:**

```
<enabled/> or <disabled/>
```

## FirefoxSuggest.WebSuggestions (Firefox Suggest (US only) > Suggestions from the web)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~FirefoxSuggest/FirefoxSuggest_WebSuggestions
```

**Value:**

```
<enabled/> or <disabled/>
```

## FlashPlugin.Allow (Flash > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## FlashPlugin.Block (Flash > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## FlashPlugin.Default (Flash > Activate Flash on websites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Default
```

**Value:**

```
<enabled/> or <disabled/>
```

## FlashPlugin.Locked (Flash > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Flash/FlashPlugin_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## GenerativeAI.Chatbot (Generative AI > Chatbot)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_Chatbot
```

**Value:**

```
<enabled/> or <disabled/>
```

## GenerativeAI.Enabled (Generative AI > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## GenerativeAI.LinkPreviews (Generative AI > Link Previews)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_LinkPreviews
```

**Value:**

```
<enabled/> or <disabled/>
```

## GenerativeAI.Locked (Generative AI > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## GenerativeAI.TabGroups (Generative AI > Tab Groups)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~GenerativeAI/GenerativeAI_TabGroups
```

**Value:**

```
<enabled/> or <disabled/>
```

## GoToIntranetSiteForSingleWordEntryInAddressBar (Force direct intranet site navigation on single word entries in the address bar)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/GoToIntranetSiteForSingleWordEntryInAddressBar
```

**Value:**

```
<enabled/> or <disabled/>
```

## Handlers (Handlers (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HandlersOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## Handlers (Handlers)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Handlers
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## HardwareAcceleration (Hardware Acceleration)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HardwareAcceleration
```

**Value:**

```
<enabled/> or <disabled/>
```

## Homepage (Home page > URL for Home page)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/HomepageURL
```

**Value:**

```
<enabled/>
<data id="HomepageURL" value="STRING"/>
<data id="HomepageLocked" value="true | false"/>
```

## Homepage.Additional (Home page > Additional Homepages)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/HomepageAdditional
```

**Value:**

```
<enabled/>
<data id="HomepageAdditional" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Homepage.StartPage (Home page > Start Page)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/HomepageStartPage
```

**Value:**

```
<enabled/>
<data id="StartPage" value="none | homepage | previous-session | homepage-locked"/>
```

## HttpAllowlist (HTTP Allowlist)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HttpAllowlist
```

**Value:**

```
<enabled/>
<data id="List" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## HttpsOnlyMode (HTTPS-Only Mode)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/HttpsOnlyMode
```

**Value:**

```
<enabled/>
<data id="HttpsOnlyMode" value="allowed | disallowed | enabled | force_enabled"/>
```

## InstallAddonsPermission.Allow (Addons > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Addons/InstallAddonsPermission_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## InstallAddonsPermission.Default (Addons > Allow add-on installs from websites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Addons/InstallAddonsPermission_Default
```

**Value:**

```
<enabled/> or <disabled/>
```

## IPProtectionAvailable (IP Protection (VPN) Availability)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/IPProtectionAvailable
```

**Value:**

```
<enabled/> or <disabled/>
```

## LegacyProfiles (Legacy Profiles)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LegacyProfiles
```

**Value:**

```
<enabled/> or <disabled/>
```

## LegacySameSiteCookieBehaviorEnabled (Revert to legacy SameSite behavior)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LegacySameSiteCookieBehaviorEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## LegacySameSiteCookieBehaviorEnabledForDomainList (Revert to legacy SameSite behavior on specific domains)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LegacySameSiteCookieBehaviorEnabledForDomainList
```

**Value:**

```
<enabled/>
<data id="LegacySameSiteCookieBehaviorEnabledForDomainList" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## LocalFileLinks (Local File Links)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/LocalFileLinks
```

**Value:**

```
<enabled/>
<data id="LocalFileLinks" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## LocalNetworkAccess.BlockTrackers (Local Network Access > Block Trackers)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~LocalNetworkAccess/LocalNetworkAccess_BlockTrackers
```

**Value:**

```
<enabled/> or <disabled/>
```

## LocalNetworkAccess.Enabled (Local Network Access > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~LocalNetworkAccess/LocalNetworkAccess_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## LocalNetworkAccess.EnablePrompting (Local Network Access > Enable Prompting)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~LocalNetworkAccess/LocalNetworkAccess_EnablePrompting
```

**Value:**

```
<enabled/> or <disabled/>
```

## LocalNetworkAccess.Locked (Local Network Access > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~LocalNetworkAccess/LocalNetworkAccess_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## LocalNetworkAccess.SkipDomains (Local Network Access > Skip Domains)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~LocalNetworkAccess/LocalNetworkAccess_SkipDomains
```

**Value:**

```
<enabled/>
<data id="LocalNetworkAccess_SkipDomains" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## ManagedBookmarks (Managed Bookmarks (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ManagedBookmarksOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## ManagedBookmarks (Managed Bookmarks)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ManagedBookmarks
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## ManualAppUpdateOnly (Manual Update Only)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/ManualAppUpdateOnly
```

**Value:**

```
<enabled/> or <disabled/>
```

## NetworkPrediction (Network Prediction)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/NetworkPrediction
```

**Value:**

```
<enabled/> or <disabled/>
```

## NewTabPage (New Tab Page)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/NewTabPage
```

**Value:**

```
<enabled/> or <disabled/>
```

## NoDefaultBookmarks (No Default Bookmarks)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/NoDefaultBookmarks
```

**Value:**

```
<enabled/> or <disabled/>
```

## OfferToSaveLogins (Offer to save logins)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OfferToSaveLogins
```

**Value:**

```
<enabled/> or <disabled/>
```

## OfferToSaveLoginsDefault (Offer to save logins (default))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OfferToSaveLoginsDefault
```

**Value:**

```
<enabled/> or <disabled/>
```

## OverrideFirstRunPage (Override the first run page)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OverrideFirstRunPage
```

**Value:**

```
<enabled/>
<data id="OverridePage" value="STRING"/>
```

## OverridePostUpdatePage (Override the upgrade page)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/OverridePostUpdatePage
```

**Value:**

```
<enabled/>
<data id="OverridePage" value="STRING"/>
```

## PasswordManagerEnabled (Password Manager)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PasswordManagerEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## PasswordManagerExceptions (Password Manager Exceptions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PasswordManagerExceptions
```

**Value:**

```
<enabled/>
<data id="List" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## PDFjs.Enabled (PDF.js > Enable PDF.js)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PDFjs/PDFjs_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## PDFjs.EnablePermissions (PDF.js > Enable Permissions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PDFjs/PDFjs_EnablePermissions
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Autoplay.Allow (Permissions > Autoplay > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Autoplay.Block (Permissions > Autoplay > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Autoplay.Default (Permissions > Autoplay > Default autoplay level)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Default
```

**Value:**

```
<enabled/>
<data id="Autoplay_Default" value="allow-audio-video | block-audio | block-audio-video"/>
```

## Permissions.Autoplay.Locked (Permissions > Autoplay > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Autoplay/Autoplay_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Camera.Allow (Permissions > Camera > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Camera.Block (Permissions > Camera > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Camera.BlockNewRequests (Permissions > Camera > Block new requests asking to access the camera)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_BlockNewRequests
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Camera.Locked (Permissions > Camera > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Camera/Camera_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Location.Allow (Permissions > Location > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Location.Block (Permissions > Location > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Location.BlockNewRequests (Permissions > Location > Block new requests asking to access location)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_BlockNewRequests
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Location.Locked (Permissions > Location > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Location/Location_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Microphone.Allow (Permissions > Microphone > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Microphone.Block (Permissions > Microphone > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Microphone.BlockNewRequests (Permissions > Microphone > Block new requests asking to access the microphone)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_BlockNewRequests
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Microphone.Locked (Permissions > Microphone > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Microphone/Microphone_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Notifications.Allow (Permissions > Notifications > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Notifications.Block (Permissions > Notifications > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.Notifications.BlockNewRequests (Permissions > Notifications > Block new requests asking to send notifications)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_BlockNewRequests
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.Notifications.Locked (Permissions > Notifications > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~Notifications/Notifications_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.ScreenShare.Allow (Permissions > Screen Sharing > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.ScreenShare.Block (Permissions > Screen Sharing > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.ScreenShare.BlockNewRequests (Permissions > Screen Sharing > Block new screen sharing requests)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_BlockNewRequests
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.ScreenShare.Locked (Permissions > Screen Sharing > Do not allow screen sharing preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~ScreenShare/ScreenShare_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.VirtualReality.Allow (Permissions > Virtual Reality > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.VirtualReality.Block (Permissions > Virtual Reality > Blocked Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_Block
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Permissions.VirtualReality.BlockNewRequests (Permissions > Virtual Reality > Block new requests asking to access virtual reality devices)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_BlockNewRequests
```

**Value:**

```
<enabled/> or <disabled/>
```

## Permissions.VirtualReality.Locked (Permissions > Virtual Reality > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Permissions~VirtualReality/VirtualReality_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## PictureInPicture.Enabled (Picture-in-Picture > Enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PictureInPicture/PictureInPicture_Enabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## PictureInPicture.Locked (Picture-in-Picture > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~PictureInPicture/PictureInPicture_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## PopupBlocking.Allow (Popups > Allowed Sites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Popups/PopupBlocking_Allow
```

**Value:**

```
<enabled/>
<data id="Permissions" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## PopupBlocking.Default (Popups > Block pop-ups from websites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Popups/PopupBlocking_Default
```

**Value:**

```
<enabled/> or <disabled/>
```

## PopupBlocking.Locked (Popups > Do not allow preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Popups/PopupBlocking_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## PostQuantumKeyAgreementEnabled (Enable post-quantum key agreement)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PostQuantumKeyAgreementEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## Preferences (Preferences (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PreferencesOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## Preferences (Preferences)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/Preferences
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## PrimaryPassword (Primary (Master) Password)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PrimaryPassword
```

**Value:**

```
<enabled/> or <disabled/>
```

## PrintingEnabled (Printing)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PrintingEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## PrivateBrowsingModeAvailability (Private Browsing Mode Availability)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PrivateBrowsingModeAvailability
```

**Value:**

```
<enabled/>
<data id="PrivateBrowsingModeAvailability" value="0 | 1 | 2"/>
```

## PromptForDownloadLocation (Prompt for download location)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/PromptForDownloadLocation
```

**Value:**

```
<enabled/> or <disabled/>
```

## Proxy (Proxy Settings > SOCKS Host)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_SOCKSProxy
```

**Value:**

```
<enabled/>
<data id="Proxy_SOCKSProxy" value="STRING"/>
<data id="Proxy_SOCKSVersion" value="4 | 5"/>
```

## Proxy.AutoConfigURL (Proxy Settings > Automatic proxy configuration URL)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_AutoConfigURL
```

**Value:**

```
<enabled/>
<data id="Proxy_AutoConfigURL" value="STRING"/>
```

## Proxy.AutoLogin (Proxy Settings > Do not prompt for authentication if password is saved)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_AutoLogin
```

**Value:**

```
<enabled/> or <disabled/>
```

## Proxy.HTTPProxy (Proxy Settings > HTTP Proxy)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_HTTPProxy
```

**Value:**

```
<enabled/>
<data id="Proxy_HTTPProxy" value="STRING"/>
```

## Proxy.Locked (Proxy Settings > Do not allow proxy settings to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## Proxy.Mode (Proxy Settings > Connection Type)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_ConnectionType
```

**Value:**

```
<enabled/>
<data id="Proxy_ConnectionType" value="none | system | manual | autoDetect | autoConfig"/>
```

## Proxy.Passthrough (Proxy Settings > Proxy Passthrough)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_Passthrough
```

**Value:**

```
<enabled/>
<data id="Proxy_Passthrough" value="STRING"/>
```

## Proxy.SSLProxy (Proxy Settings > HTTPS Proxy)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_SSLProxy
```

**Value:**

```
<enabled/>
<data id="Proxy_SSLProxy" value="STRING"/>
```

## Proxy.UseHTTPProxyForAllProtocols (Proxy Settings > Use HTTP proxy for HTTPS)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_UseHTTPProxyForAllProtocols
```

**Value:**

```
<enabled/> or <disabled/>
```

## Proxy.UseProxyForDNS (Proxy Settings > Proxy DNS when using SOCKS)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~ProxySettings/Proxy_UseProxyForDNS
```

**Value:**

```
<enabled/> or <disabled/>
```

## RequestedLocales (Requested locale)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/RequestedLocales
```

**Value:**

```
<enabled/>
<data id="RequestedLocales" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## RequestedLocales (Requested locale (string))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/RequestedLocalesString
```

**Value:**

```
<enabled/>
<data id="Preferences_String" value="STRING"/>
```

## SanitizeOnShutdown.Cache (Clear data when browser is closed > Cache)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/A_SanitizeOnShutdown_Cache
```

**Value:**

```
<enabled/> or <disabled/>
```

## SanitizeOnShutdown.Cookies (Clear data when browser is closed > Cookies)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/B_SanitizeOnShutdown_Cookies
```

**Value:**

```
<enabled/> or <disabled/>
```

## SanitizeOnShutdown.FormData (Clear data when browser is closed > Form Data)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/D_SanitizeOnShutdown_FormData
```

**Value:**

```
<enabled/> or <disabled/>
```

## SanitizeOnShutdown.History (Clear data when browser is closed > History)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/E_SanitizeOnShutdown_History
```

**Value:**

```
<enabled/> or <disabled/>
```

## SanitizeOnShutdown.Locked (Clear data when browser is closed > Locked)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/I_SanitizeOnShutdown_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## SanitizeOnShutdown.Sessions (Clear data when browser is closed > Active Logins)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/F_SanitizeOnShutdown_Sessions
```

**Value:**

```
<enabled/> or <disabled/>
```

## SanitizeOnShutdown.SiteSettings (Clear data when browser is closed > Site Preferences)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SanitizeOnShutdown/G_SanitizeOnShutdown_SiteSettings
```

**Value:**

```
<enabled/> or <disabled/>
```

## SearchBar (Search bar location)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SearchBar
```

**Value:**

```
<enabled/>
<data id="SearchBar" value="unified | separate"/>
```

## SearchEngines.Add[N] (Search > Search Engine One - Search Engine Five)

Replace `NN` with the numeric suffix from `SearchEngines_1` through `SearchEngines_5` (5 slots).

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_NN
```

**Value:**

```
<enabled/>
<data id="SearchEngine_Name" value="STRING"/>
<data id="SearchEngine_URLTemplate" value="STRING"/>
<data id="SearchEngine_Method" value="GET | POST"/>
<data id="SearchEngine_IconURL" value="STRING"/>
<data id="SearchEngine_Alias" value="STRING"/>
<data id="SearchEngine_Description" value="STRING"/>
<data id="SearchEngine_SuggestURLTemplate" value="STRING"/>
<data id="SearchEngine_PostData" value="STRING"/>
<data id="SearchEngine_Encoding" value="STRING"/>
```

## SearchEngines.Default (Search > Default Search Engine)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_Default
```

**Value:**

```
<enabled/>
<data id="SearchEngines_Default" value="STRING"/>
```

## SearchEngines.PreventInstalls (Search > Prevent Search Engine Installs)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_PreventInstalls
```

**Value:**

```
<enabled/> or <disabled/>
```

## SearchEngines.Remove (Search > Remove Search Engines)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchEngines_Remove
```

**Value:**

```
<enabled/>
<data id="SearchEngines_Remove" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## SearchSuggestEnabled (Search > Search Suggestions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Search/SearchSuggestEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## SecurityDevices (Security Devices)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SecurityDevices
```

**Value:**

```
<enabled/>
<data id="SecurityDevices" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## SecurityDevices.Add (Security Devices > Add)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SecurityDevices/SecurityDevices_Add
```

**Value:**

```
<enabled/>
<data id="SecurityDevices" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## SecurityDevices.Delete (Security Devices > Delete)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~SecurityDevices/SecurityDevices_Delete
```

**Value:**

```
<enabled/>
<data id="SecurityDevices" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## ShowHomeButton (Home page > Show Home button on toolbar)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Homepage/Homepage_ShowHomeButton
```

**Value:**

```
<enabled/> or <disabled/>
```

## SkipTermsOfUse (Skip Terms of Use)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SkipTermsOfUse
```

**Value:**

```
<enabled/> or <disabled/>
```

## Software.Policies.Mozilla.Certificates (Certificates > Install Certificates)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~Certificates/Certificates_Install
```

**Value:**

```
<enabled/>
<data id="Certificates_Install" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Software.Policies.Mozilla.WebsiteFilter.Block (Blocked websites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/B_WebsiteFilter_Block
```

**Value:**

```
<enabled/>
<data id="WebsiteFilter" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## Software.Policies.Mozilla.WebsiteFilter.Exceptions (Exceptions to blocked websites)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/B_WebsiteFilter_Exceptions
```

**Value:**

```
<enabled/>
<data id="WebsiteFilter" value="1&#xF000;value1&#xF000;2&#xF000;value2"/>
```

## SSLVersionMax (Maximum SSL version enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SSLVersionMax
```

**Value:**

```
<enabled/>
<data id="SSLVersion" value="tls1 | tls1.1 | tls1.2 | tls1.3"/>
```

## SSLVersionMin (Minimum SSL version enabled)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SSLVersionMin
```

**Value:**

```
<enabled/>
<data id="SSLVersion" value="tls1 | tls1.1 | tls1.2 | tls1.3"/>
```

## StartDownloadsInTempDirectory (Start Downloads in Temporary Directory)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/StartDownloadsInTempDirectory
```

**Value:**

```
<enabled/> or <disabled/>
```

## SupportMenu (Support Menu)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/SupportMenu
```

**Value:**

```
<enabled/>
<data id="SupportMenuTitle" value="STRING"/>
<data id="SupportMenuURL" value="STRING"/>
<data id="SupportMenuAccessKey" value="STRING"/>
```

## TranslateEnabled (Enable webpage translation)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/TranslateEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.ExtensionRecommendations (User Messaging > Extension Recommendations)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_ExtensionRecommendations
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.FeatureRecommendations (User Messaging > Feature Recommendations)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_FeatureRecommendations
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.FirefoxLabs (User Messaging > Firefox Labs)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_FirefoxLabs
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.Locked (User Messaging > Do not allow user messaging preferences to be changed)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_Locked
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.MoreFromMozilla (User Messaging > More from Mozilla)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_MoreFromMozilla
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.SkipOnboarding (User Messaging > Skip Onboarding)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_SkipOnboarding
```

**Value:**

```
<enabled/> or <disabled/>
```

## UserMessaging.UrlbarInterventions (User Messaging > Urlbar Interventions)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox~UserMessaging/UserMessaging_UrlbarInterventions
```

**Value:**

```
<enabled/> or <disabled/>
```

## UseSystemPrintDialog (Use System Print Dialog)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/UseSystemPrintDialog
```

**Value:**

```
<enabled/> or <disabled/>
```

## VisualSearchEnabled (Visual Search)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/VisualSearchEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```

## WebsiteFilter (Website Filter (JSON on one line))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/WebsiteFilterOneLine
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## WebsiteFilter (Website Filter (JSON))

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/WebsiteFilter
```

**Value:**

```
<enabled/>
<data id="JSON" value='... JSON - see policy docs for schema ...'/>
```

## WindowsSSO (Windows SSO)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/WindowsSSO
```

**Value:**

```
<enabled/> or <disabled/>
```

## XSLTEnabled (Enable XSLT)

**OMA-URI:**

```
./Device/Vendor/MSFT/Policy/Config/Firefox~Policy~firefox/XSLTEnabled
```

**Value:**

```
<enabled/> or <disabled/>
```
