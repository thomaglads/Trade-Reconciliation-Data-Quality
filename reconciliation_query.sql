-- This query reconciles trades between the front-office and back-office systems.
-- It identifies breaks such as missing trades or mismatched economic values.

SELECT
    COALESCE(fo.trade_id, bo.TransactionReference) AS trade_id,
    CASE
        WHEN fo.trade_id IS NULL THEN 'Missing in Front Office'
        WHEN bo.TransactionReference IS NULL THEN 'Missing in Back Office'
        WHEN fo.quantity != bo.Units THEN 'Quantity Mismatch'
        WHEN fo.price != bo.ExecutionPrice THEN 'Price Mismatch'
        WHEN fo.settlement_date != bo.ExpectedSettlement THEN 'Settlement Date Mismatch'
        ELSE 'Unknown Break'
    END AS break_reason,
    fo.ticker AS fo_ticker,
    bo.SecurityID AS bo_ticker,
    fo.quantity AS fo_quantity,
    bo.Units AS bo_quantity,
    fo.price AS fo_price,
    bo.ExecutionPrice AS bo_price,
    fo.settlement_date AS fo_settlement_date,
    bo.ExpectedSettlement AS bo_settlement_date
FROM
    front_office fo
FULL OUTER JOIN
    back_office bo ON fo.trade_id = bo.TransactionReference
WHERE
    fo.trade_id IS NULL
    OR bo.TransactionReference IS NULL
    OR fo.quantity != bo.Units
    OR fo.price != bo.ExecutionPrice
    OR fo.settlement_date != bo.ExpectedSettlement;
