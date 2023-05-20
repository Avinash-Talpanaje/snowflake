# Getting started Snowflake with Python connector on VSCode.

1. Create snowflake account (30 Days free trial) at https://www.snowflake.com. Get your snowflake account identifier.
2. Create a role for your usage and assign 'Usage' privilage to Warehouse and Database.
3. Create a workspace in VSCode.
4. Create requirements.txt and add snowflake connector dependency. Click on "Create Environment" button to create a Virtual Environment. This step will create a python virtual environment. You can choose your provider.
5. Create 3 environment variables, namely "SNOWFLAKE_USER", "SNOWFLAKE_PASSWORD", "SNOWFLAKE_ACCOUNT". Put your username, password that you created for your account and your snowflake account (org id.account). Replace dot(".") with a hiphen ("-")
eg., XXXXOXX.XY00000 will become XXXXOXX-XY00000
6. Replace your warehouse, database and schema according to your account settings.
7. Replace sql_query with your desired query.
8. Press ctrl+F5 to run your program. If successfull, data will be printed on the console. If there is any error it will logged in the "snowflake_connector.log" file.