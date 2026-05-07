
USE phonepe;

-- Check data
SELECT COUNT(*) FROM aggregated_transaction;

-- Top states
SELECT state, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- Transaction types
SELECT transaction_type, SUM(transaction_count) AS total_transactions
FROM aggregated_transaction
GROUP BY transaction_type
ORDER BY total_transactions DESC;

-- Year analysis
SELECT year, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY year
ORDER BY year;

-- Quarter analysis
SELECT quarter, SUM(transaction_amount) AS total_amount
FROM aggregated_transaction
GROUP BY quarter
ORDER BY quarter;

-- State + year
SELECT state, year, SUM(transaction_amount) AS total
FROM aggregated_transaction
GROUP BY state, year
ORDER BY total DESC;