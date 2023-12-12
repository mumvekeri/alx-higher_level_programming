-- A script that lists all the tables of a database in your MySQL server.
-- Check for argument presence
IF @@parameter_count < 1 THEN
  SELECT 'Please provide a database name as an argument.';
ELSE
  SELECT TABLE_NAME
  FROM information_schema.tables
  WHERE TABLE_SCHEMA = @`{1}`;
END IF;
