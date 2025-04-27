from great_expectations.data_context import DataContext

# Initialize Great Expectations Context
context = DataContext()

# Add Pandas datasource manually
context.add_datasource(
    name="my_pandas_datasource",
    class_name="Datasource",
    execution_engine={"class_name": "PandasExecutionEngine"},
    data_connectors={
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "D:/repos/scraping_data_from_web/great_expectation/",
            "default_regex": {
                "pattern": "(.*)",
                "group_names": ["data_asset_name"],
            },
        }
    }
)

print("✅ Datasource 'my_pandas_datasource' created successfully!")
