from great_expectations.expectations.expectation import ColumnMapExpectation
from great_expectations.expectations.metrics import ColumnMapMetricProvider, column_condition_partial
from great_expectations.execution_engine import PandasExecutionEngine   # <-- this line is important!

# First, define the Metric
class ColumnValuesGreaterThanCustom(ColumnMapMetricProvider):
    condition_metric_name = "column_values.greater_than_custom"

    @column_condition_partial(engine=PandasExecutionEngine)   # <-- fix this
    def _pandas(cls, column, value, **kwargs):
        return column > value

# Second, define the Expectation
class ExpectColumnValuesToBeGreaterThanCustom(ColumnMapExpectation):
    """Expect column values to be greater than a given threshold."""

    metric_dependencies = ("column_values.greater_than_custom",)
    success_keys = ("value",)

    default_kwarg_values = {
        "value": 0,
        "mostly": 1.0,
    }

    map_metric = "column_values.greater_than_custom"

    def validate_configuration(self, configuration):
        super().validate_configuration(configuration)
        if "value" not in configuration.kwargs:
            raise ValueError("value parameter must be provided")
        return True
