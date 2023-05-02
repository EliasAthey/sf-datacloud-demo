# sf-datacloud-demo
Demo of programmatic integration with Salesforce Data Cloud

# Connect to SF Data Cloud
1. [Install latest SF Data Cloud JDBC Driver](https://github.com/forcedotcom/Salesforce-CDP-jdbc/releases)
   1. Put the jar file in the project folder.
2. [Create key pair and certificates](https://github.com/forcedotcom/Salesforce-CDP-jdbc#create-a-private-public-key-pair-and-a-digital-x509-certificate)
3. [Create Connected App](https://github.com/forcedotcom/Salesforce-CDP-jdbc#connected-app-setup)
4. [Authorize user for connected app via the User Agent Flow](https://github.com/forcedotcom/Salesforce-CDP-jdbc#app-authorization)
   1. Authorization URL template:
   <ORG_URL>/services/oauth2/authorize?response_type=code&client_id=<CLIENT_ID>&scope=<REQUIRED_SCOPES>&redirect_uri=<CALLBACK_URL>
   2. Formatted CDP Scopes for URL:
   full%20cdp_calculated_insight_api%20cdp_identityresolution_api%20cdp_ingest_api%20cdp_profile_api%20api%20cdp_query_api%20refresh_token%20offline_access%20cdp_segment_api


# Use Cursor object to send queries
Sample query of Individual data model object:
```
curs = conn.cursor()
curs.execute('SELECT * FROM ssot__Individual__dlm')
data = curs.fetchall()
```
