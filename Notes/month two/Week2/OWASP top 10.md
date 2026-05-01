# What is OWASP?

The Open Web Application Security Project, or OWASP, is an international non-profit organization dedicated to web application security. One of OWASP’s core principles is that all of their materials be freely available and easily accessible on their website, making it possible for anyone to improve their own web application security. 

# OWASP Top 10

## 1. Broken Access Control

- Access control refers a system that controls access to information or functionality. 
- Broken access controls allow attackers to bypass authorization and perform tasks as though they were privileged users such as administrators. 
> For example a web application could allow a user to change which account they are logged in as simply by changing part of a URL, without any other verification.
- Access controls can be secured by ensuring that a web application uses authorization tokens* and sets tight controls on them.
- Many services issue authorization tokens when users log in.

## 2. Cryptographic Failures

- The risk of data exposure can be minimized by encrypting all sensitive data, authenticating all transmissions, and disabling the caching* of any sensitive information. 
- Additionally, web application developers should take care to ensure that they are not unnecessarily storing any sensitive data.
> *Caching is the practice of temporarily storing data for re-use. For example, web browsers will often cache webpages so that if a user revisits those pages within a fixed time span, the browser does not have to fetch the pages from the web.

## 3. Injection

- Injection attacks happen when untrusted data is sent to a code interpreter through a form input or some other data submission to a web application. 
> For example, an attacker could enter SQL database code into a form that expects a plaintext username. If that form input is not properly secured, this would result in that SQL code being executed. This is known as an **SQL injection attack**.
- The Injection category also includes cross-site scripting (XSS) attacks, previously their own category in the 2017 report. Mitigation strategies for cross-site scripting include escaping untrusted HTTP requests, as well as using modern web development frameworks like ReactJS and Ruby on Rails, which provide some built-in cross-site scripting protection.
- Injection attacks can be prevented by validating and/or sanitizing user-submitted data. 
- **Validation** means rejecting suspicious-looking data
- **Sanitization** refers to cleaning up the suspicious-looking parts of the data.

## 4. Insecure Design

- Emdedded in the architecture of an application. 
It focuses on the design of an application, not its implementation. 
> An example of bad design can be an option to give a clue about the password like "what's your mom's name?"
- The use of threat modeling prior to an application's deployment can help mitigate these types of vulnerabilities.

## 5. Security Misconfiguration

- **Security misconfiguration** is the most common vulnerability on the list, and is often the result of using default configurations or displaying excessively verbose errors. 
- This can be mitigated by removing any unused features in the code and ensuring that error messages are more general.

### The Security Misconfiguration category includes: 
- *The XML External Entities (XEE) attack* — This is an attack against a web application that parses XML* input. This input can reference an external entity (this refers to storage unit like hard drive). An XML parser can be duped into sending data to an unauthorized external entity, which can pass sensitive data directly to an attacker. The best ways to prevent XEE attacks are to have web applications accept a less complex type of data, such as JSON, or at the very least to patch XML parsers and disable the use of external entities in an XML application.

> *XML or Extensible Markup Language is a markup language intended to be both human-readable and machine-readable. Due to its complexity and security vulnerabilities, it is now being phased out of use in many web applications.

## 6. Vulnerable and Outdated Components

-  Some attackers look for vulnerabilities in components which they can then use to orchestrate attacks. 
- Some of the more popular components are used on hundreds of thousands of websites; an attacker finding a security hole in one of these components could leave hundreds of thousands of sites vulnerable to exploit.

- Component developers often offer security patches and updates to plug up known vulnerabilities, but web application developers do not always have the patched or most-recent versions of components running on their applications. 
- To minimize the risk of running components with known vulnerabilities, developers should remove unused components from their projects, as well as ensure that they are receiving components from a trusted source that are up to date.

## 7. Identification and Authentication Failures

- Vulnerabilities in authentication (login) systems can give attackers access to user accounts and even the ability to compromise an entire system using an admin account. 
- Ways to mitigate this:
    - Using 2FA
    - Delaying repeated login attempts
    
## 8. Software and Data Integrity Failures

- Includes insecure deserialization exploits, accepting all updates f an external source
- Ways of mitigation
    - use digital signatures to verify updates, 
    - check their software supply chains, and ensure that 
    - continuous integration/continuous deployment (CI/CD) pipelines have strong access control and are configured correctly.

## 9. Security Logging and Monitoring Failures

- Many web applications are not taking enough steps to detect data breaches. 
- The average discovery time for a breach is around 200 days after it has happened. 
- OWASP recommends that web developers should implement logging and monitoring as well as incident response plans to ensure that they are made aware of attacks on their applications.

## 10. Server-Side Request Forgery

- Server-Side Request Forgery (SSRF) is an attack in which someone sends a URL request to a server that causes the server to fetch an unexpected resource, even if that resource is otherwise protected. 
- An attacker might, for example, send a request for www.example.com/super-secret-data/, even though web users are not supposed to be able to navigate to that location, and get access to super secret data from the server's response.
- Ways of mitigation
    - Validate all URLs coming from clients