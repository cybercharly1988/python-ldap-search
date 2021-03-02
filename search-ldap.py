#!/usr/bin/env python3
#Author: Juan Carlos Perez Hernandez

from ldap3 import Server, Connection, SUBTREE
import ssl
server = ldap3.Server('ldap.testcompany.net', use_ssl=True)
connection = ldap3.Connection(server, authentication=ldap3.SASL, sasl_mechanism='GSSAPI')
connection.bind()

print(connection.extend.standard.who_am_i())

onnection.search(
    'ou=users,dc=testcompany,dc=net',
    '(uid=usertosearch)',
    attributes=ldap3.ALL_ATTRIBUTES)

    print(connection)

    print(connection.response)