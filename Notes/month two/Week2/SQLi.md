Most SQL injection vulnerabilities occur within the WHERE clause of a SELECT query.
 -- is a comment indicator in SQL. This means that the rest of the query is interpreted as a comment

 # Portswigger 1

 `https://0a8b003d03e3d4c384331d6d00bd00df.web-security-academy.net/filter?category=Accessories%27+OR+1=1--` what this query does is it return all category including both realeased and unreleased products.

 eg SQL injection: `'+OR+1=1--`
| Part     | Purpose                     |
| -------- | --------------------------- |
| `'`      | Closes the original string  |
| `OR 1=1` | Makes condition always true |
| `--`     | Comments out the rest       |
| `+`      | Represents spaces in a URL  |

An attacker can log in as any user without the need for a password. They can do this using the SQL comment sequence -- to remove the password check from the WHERE clause of the query. For example, submitting the username administrator'-- and a blank password results in the following query:
    `SELECT * FROM users WHERE username = 'administrator'--' AND password = ''`
This query returns the user whose username is administrator and successfully logs the attacker in as that user. 


# SQL Injection UNION Attack

- You can use the UNION keyword to retrieve data from other tables within the database. This is commonly known as a SQL injection UNION attack.
- The UNION keyword enables you to execute one or more additional SELECT queries and append the results to the original query. For example:
    `SELECT a, b FROM table1 UNION SELECT c, d FROM table2`
This SQL query returns a single result set with two columns, containing values from columns a and b in table1 and columns c and d in table2. 
To carry out a SQL injection UNION attack, make sure that your attack meets these two requirements. This normally involves finding out:
    - How many columns are being returned from the original query.
    - Which columns returned from the original query are of a suitable data type to hold the results from the injected query.

- To determine the number of columns we can use `ORDER BY` command
- Another way is: `'+UNION+SELECT+NULL,NULL--`

# SQL Injection Cheet Sheet

## String concatenation
You can concatenate together multiple strings to make a single string.
    `Oracle 	'foo'||'bar' `
    `Microsoft 	'foo'+'bar' `
    `PostgreSQL 	'foo'||'bar' `
    `MySQL 	'foo' 'bar' [Note the space between the two strings] `
    `CONCAT('foo','bar') `

## Substring
You can extract part of a string, from a specified offset with a specified length. Note that the offset index is 1-based. Each of the following expressions will return the string ba.
    Oracle 	SUBSTR('foobar', 4, 2)
    Microsoft 	SUBSTRING('foobar', 4, 2)
    PostgreSQL 	SUBSTRING('foobar', 4, 2)
    MySQL 	SUBSTRING('foobar', 4, 2) 

## Comments
You can use comments to truncate a query and remove the portion of the original query that follows your input.
    Oracle 	--comment
    Microsoft 	--comment
                /*comment*/
    PostgreSQL 	--comment
                /*comment*/
    MySQL 	#comment
            -- comment [Note the space after the double dash]
            /*comment*/