# pip install great_expectations==0.18.11 (Install this version)
from great_expectations.data_context import DataContext
from great_expectations.core.batch import BatchRequest

context = DataContext()

# Define batch request (proper object)
batch_request = BatchRequest(
    datasource_name="my_pandas_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="user_signup.csv"
)

# Try the connection to data
try:
    validator = context.get_validator(batch_request=batch_request)

    # Add simple expectation
    result = validator.expect_column_values_to_not_be_null('email')

    # Check and print result
    if result.success:
        print("Validation passed: All emails are not null")
    else:
        print("Validation failed: Some emails are missing!")

except Exception as e:
    print("Error during the validation")
    print(str(e))