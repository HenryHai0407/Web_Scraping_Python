CREATE PROCEDURE usp_LoadSalesInBatches
    @BatchSize INT = 10,
    @TargetDate DATE = NULL  -- Optional: specify which date to process
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @ProcessedRows INT;

    -- Default to today's date if not provided
    IF @TargetDate IS NULL
        SET @TargetDate = CAST(GETDATE() AS DATE);

    -- Create or prepare target table
    IF OBJECT_ID('dbo.sales_results') IS NULL
    BEGIN
        CREATE TABLE dbo.sales_results (
            product_id INT,
            product_name NVARCHAR(255),
            order_id INT,
            quantity INT,
            list_price DECIMAL(10, 2),
            discount DECIMAL(4, 2),
            order_date DATE,
            sales DECIMAL(12, 2)
        );
    END
    ELSE
    BEGIN
        -- Remove only old data, not today's target date
        DELETE FROM dbo.sales_results
        WHERE order_date < @TargetDate;
    END

    -- Loop processing
    WHILE 1 = 1
    BEGIN
        -- Insert batch where not already inserted
        WITH Batch AS (
            SELECT TOP (@BatchSize)
                o.product_id,
                p.product_name,
                o.order_id,
                o.quantity,
                o.list_price,
                o.discount,
                o.order_date,
                (o.quantity * o.list_price) * (1 - o.discount) AS sales
            FROM [K13_HoangHai_Practice].[dbo].[order_items] o
            JOIN [K13_HoangHai_Practice].[dbo].[products] p
                ON o.product_id = p.product_id
            WHERE CAST(o.order_date AS DATE) = @TargetDate
              AND NOT EXISTS (
                  SELECT 1
                  FROM dbo.sales_results r
                  WHERE r.order_id = o.order_id
                    AND r.product_id = o.product_id
              )
            ORDER BY o.order_id
        )
        INSERT INTO dbo.sales_results (product_id, product_name, order_id, quantity, list_price, discount, order_date, sales)
        SELECT * FROM Batch;

        SET @ProcessedRows = @@ROWCOUNT;

        -- Exit loop if no more rows
        IF @ProcessedRows = 0
            BREAK;
    END

    PRINT CONCAT('Sales data for ', CONVERT(VARCHAR, @TargetDate), ' processed successfully.');
END
