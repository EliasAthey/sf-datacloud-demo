from dotenv import load_dotenv
import jaydebeapi as jdbc
import os

load_dotenv()
sf_user = os.getenv('SF_USERNAME')
sf_pw = os.getenv('SF_PASSWORD')
dc_key = os.getenv('DATA_CLOUD_API_KEY')
dc_secret = os.getenv('DATA_CLOUD_API_SECRET')

# Data Cloud API Connected App properties - username/pw flow
properties = {
    'user': sf_user,
    'password':sf_pw,
    'clientId': dc_key,
    'clientSecret': dc_secret
}

# Connect to Data Cloud via JDBC Driver
conn = jdbc.connect("com.salesforce.cdp.queryservice.QueryServiceDriver",
             "jdbc:queryService-jdbc:https://login.salesforce.com",
             properties,
             "Salesforce-CDP-jdbc-1.19.1.jar")

# Setup cursor, execute query of Individual object
curs = conn.cursor()
curs.execute('SELECT * FROM ssot__Individual__dlm')
data = curs.fetchall()
print(data)

print('done')