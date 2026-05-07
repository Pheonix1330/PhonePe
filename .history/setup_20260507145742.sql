CREATE DATABASE IF NOT EXISTS phonepe;

USE phonepe;

-- =========================================================
-- AGGREGATED TABLES
-- =========================================================

CREATE TABLE IF NOT EXISTS aggregated_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

SELECT COUNT(*) FROM aggregated_transaction;

SELECT * FROM aggregated_transaction LIMIT 10;

CREATE TABLE IF NOT EXISTS aggregated_user (
    state VARCHAR(100),
    year INT,
    quarter INT,
    brand VARCHAR(100),
    registered_users BIGINT,
    app_opens DOUBLE
);

SELECT COUNT(*) FROM aggregated_user;
SELECT * FROM aggregated_user LIMIT 10;
CREATE TABLE IF NOT EXISTS aggregated_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_type VARCHAR(100),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

-- =========================================================
-- MAP TABLES
-- =========================================================

CREATE TABLE IF NOT EXISTS map_user (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    registered_users BIGINT,
    app_opens BIGINT
);

CREATE TABLE IF NOT EXISTS map_map (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS map_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

-- =========================================================
-- TOP TABLES
-- =========================================================

CREATE TABLE IF NOT EXISTS top_user (
    state VARCHAR(100),
    year INT,
    quarter INT,
    pincode VARCHAR(20),
    registered_users BIGINT
);

CREATE TABLE IF NOT EXISTS top_map (
    state VARCHAR(100),
    year INT,
    quarter INT,
    entity_name VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

CREATE TABLE IF NOT EXISTS top_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_name VARCHAR(100),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);