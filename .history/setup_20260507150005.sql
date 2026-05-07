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

SELECT COUNT(*) FROM aggregated_insurance;

SELECT * FROM aggregated_insurance LIMIT 10;

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

SELECT COUNT(*) FROM map_user;

SELECT * FROM map_user LIMIT 10;

CREATE TABLE IF NOT EXISTS map_map (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

SELECT COUNT(*) FROM map_map;

SELECT * FROM map_map LIMIT 10; 

CREATE TABLE IF NOT EXISTS map_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

SELECT COUNT(*) FROM map_insurance;

SELECT * FROM map_insurance LIMIT 10;

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

SELECT COUNT(*) FROM top_user;

SELECT * FROM top_user LIMIT 10;

CREATE TABLE IF NOT EXISTS top_map (
    state VARCHAR(100),
    year INT,
    quarter INT,
    entity_name VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

SELECT COUNT(*) FROM top_map;

SELECT * FROM top_map LIMIT 10;

CREATE TABLE IF NOT EXISTS top_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_name VARCHAR(100),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);