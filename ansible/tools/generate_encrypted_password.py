#!/usr/bin/env python3

# from https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module

from passlib.hash import sha512_crypt
import getpass

print(">> Enter the password to be encrypted below.")
print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))

