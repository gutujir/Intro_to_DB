-- Full description of books table without DESCRIBE or EXPLAIN
SELECT * 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'alx_book_store' 
AND TABLE_NAME = 'books';