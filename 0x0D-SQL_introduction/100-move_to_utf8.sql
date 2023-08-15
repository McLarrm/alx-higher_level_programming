-- Script: Convert to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Task: Convert database hbtn_0c_0, table first_table, and field name to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- SQL Query: Select database
USE hbtn_0c_0
-- SQL Query: Convert table first_table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
