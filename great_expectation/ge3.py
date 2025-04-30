from great_expectations.data_context import DataContext
from great_expectations.core.batch import BatchRequest

context = DataContext()

# Define batch request (proper object)
batch_request = BatchRequest(
    datasource_name="my_pandas_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="product_catalog.csv"
)

try:
    validator = context.get_validator(
        batch_request = batch_request,
        expectation_suite_name="product_catalog_suite"
    )

    result = validator.expect_column_values_to_not_be_null('stock_qty')

    # Save suite
    validator.save_expectation_suite()

    # Check and print result
    if result.success:
        print("Validation 3 passed!")
    else:
        print("Validation 3 failed!")
    
except Exception as e:
    print("Error during validation")
    print(str(e))