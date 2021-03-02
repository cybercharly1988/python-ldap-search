# python-ldap-search

## Summary
 a very simple Python script to do a simple LDAP search on that LDAP server.

 ## Usage

 ### Pre-requisites
 * install libraries ldap3 and ssl

## Getting Started
**Example**

```python
from ldap3 import Server, Connection, SUBTREE
import ssl
server = ldap3.Server('ldap.testcompany.net', use_ssl=True)
connection = ldap3.Connection(server, authentication=ldap3.SASL, sasl_mechanism='GSSAPI')
connection.bind()

print(connection.extend.standard.who_am_i())

onnection.search(
    'ou=users,dc=testcompany,dc=net',
    '(uid=juan)',
    attributes=ldap3.ALL_ATTRIBUTES)

    print(connection)

    print(connection.response)
```


**Outputs**
| Name | Description |
|------|-------------|
| uid | If we found a coincidence in the ldap for the user, we will have the information UID for the that user |

### Notable
* Nothing to mention yet

## Owners
| Name | Email |
|------|-------|
| Juan Carlos Perez Hernandez | jc.przhdz@gmail.com

# CHANGELOG
***
### Version 1.0.0
***Added***
* Added the python code to create a simple query in ldap
* Added the README