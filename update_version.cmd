xml ed -P --inplace --update "/policyDefinitions/@revision" -v "%1" windows/firefox.admx
xml ed -P --inplace --update "/policyDefinitions/resources/@minRequiredRevision" -v "%1" windows/firefox.admx
xml ed -P --inplace --update "/policyDefinitionResources/@revision" -v "%1" windows/de-DE/firefox.adml
xml ed -P --inplace --update "/policyDefinitionResources/@revision" -v "%1" windows/en-US/firefox.adml
xml ed -P --inplace --update "/policyDefinitionResources/@revision" -v "%1" windows/ru-RU/firefox.adml
xml ed -P --inplace --update "/policyDefinitionResources/@revision" -v "%1" windows/fr-FR/firefox.adml
