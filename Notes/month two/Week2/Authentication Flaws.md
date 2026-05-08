# What are Authentication Flaws?

Aunthentication Vulnerabilities arise from insecure implementation of the authentication mechanisms in an application.

## Insecure Authentication mechanisms

 - weak password requirements
 - Improper restriction of authentication attempts: Application permits bruteforse
 - Verbose error message
 - Vulnerable transmission of credentials
 - Insecure forgot password functionality: it might give too clarified clue info about the user
 - Defects in multistage login mechanism: insecure implementation of the MFA function. 
 - Insecure storage of credentials

 ## How to Prevent authentication vulnerabilities
 
 - Wherever possible, implement multi-factor authentication.
 - Change all default credentials.
 - Always use an encrypted channel / connection (HTTPS) when sending user credentials.
 - Only POST requests should be used to transmit credentials to the server.
 - Stored credentials should be hashed and salted using cryptographically secure algorithms.
 - Use identical, generic error messages on the login form when the user enters incorrect credentials.
 - Implement an effective password policy that is compliant with NIST 800-63-b’s guidelines.
 - Use a simple password checker to provide real time feedback on the strength of the password. For example: zxcvbn JavaScript library.
 - Implement robust brute force protection on all authentication pages.
 - Audit any verification or validation logic thoroughly to eliminate flaws.

 # portswigger's labs on Authentication
 ## 2FA Simple bypass