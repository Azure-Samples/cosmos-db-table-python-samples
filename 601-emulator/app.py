# <imports>
from azure.data.tables import TableServiceClient, UpdateMode
# </imports>

# <client>
service = TableServiceClient.from_connection_string(
    conn_str="DefaultEndpointsProtocol=http;AccountName=localhost;AccountKey=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==;TableEndpoint=http://localhost:8902/;"
)
# </client>

# <resources>
client = service.create_table_if_not_exists(
    table_name="cosmicworksproducts"
)
# </resources>

# <upsert>
item = {
    "PartitionKey": "68719518371",
    "RowKey": "Surfboards",
    "name": "Kiama classic surfboard"
}

client.upsert_entity(
    entity=item,
    mode=UpdateMode.REPLACE
)
# </upsert>
