import sys
import os

# Add gx/plugins/ to Python path
sys.path.append(os.path.join(os.getcwd(), "gx", "plugins"))

from great_expectations.data_context import DataContext
from great_expectations.core.batch import BatchRequest

context = DataContext()

# Define batch request (proper object)
batch_request = BatchRequest(
    datasource_name="my_pandas_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="sales_transactions.csv"
)

try:
    validator = context.get_validator(
        batch_request=batch_request,
        expectation_suite_name="sales_transactions_suite"
    )

    # Instead of calling custom expect directly,
    # add expectation manually into suite
    validator.expect_column_values_to_be_greater_than(
        column="amount_usd",
        value=0
    )

    validator.save_expectation_suite()

    print("✅ Saved expectations into 'sales_transactions_suite'!")

except Exception as e:
    print("💥 Error during the validation")
    print(str(e))
