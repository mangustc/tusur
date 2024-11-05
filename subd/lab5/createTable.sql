DROP TABLE Employee CASCADE;
DROP TABLE Email CASCADE;

CREATE TABLE Email (
	email_id SERIAL PRIMARY KEY,
	email_str text NOT NULL,
	email_created_at DATE NOT NULL,
	UNIQUE(email_str)
);

CREATE TABLE Employee (
	empolyee_id SERIAL PRIMARY KEY,
	employee_last_name text,
	employee_first_name text,
	employee_username text NOT NULL,
	email_id int,
	CONSTRAINT fk_email FOREIGN KEY (email_id) REFERENCES Email(email_id),
	UNIQUE(employee_username)
);
