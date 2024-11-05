DROP FUNCTION create_email CASCADE;
DROP FUNCTION get_email_from_username CASCADE;
DROP FUNCTION insert_email CASCADE;

CREATE OR REPLACE FUNCTION get_email_from_username(username text)
RETURNS text
AS $BODY$
BEGIN
	RETURN username || '@empl.tusur.ru';
END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION insert_email(username text)
RETURNS int
AS $BODY$
DECLARE
	email text := get_email_from_username(username);
BEGIN
	WITH new_email AS (
	    INSERT INTO Email (email_str, email_created_at)
	    VALUES (email, NOW())
	    RETURNING email_id
	)
	UPDATE Employee
	SET email_id = (SELECT email_id FROM new_email)
	WHERE employee_username = username;
	RETURN 1;
END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_email()
RETURNS trigger
AS $create_email$
DECLARE
	inttest int := 0;
BEGIN
	inttest := insert_email(NEW.employee_username);
	RETURN NEW;
END;
$create_email$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER create_email_trigger AFTER INSERT ON Employee
	FOR EACH ROW EXECUTE PROCEDURE create_email();
