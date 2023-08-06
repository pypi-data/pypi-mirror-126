# memoorje crypto

This repository contains implementations of our cryptographic helpers and container formats.
Implementations should share a similar interface and must be kept in sync.

HUGE WARNING: This code has not been reviewed yet. If you care about your data DON’T use it.

# TypeScript implementation

The TypeScript implementation of memoorje crypto is based on the
[Web Cryptography API](https://w3c.github.io/webcrypto/).

Build with: `npm run build`. \
Test with: `npm run test`.

# Python implementation

The python implementation of memoorje crypto is based on [PyCryptodome](https://pypi.org/project/pycryptodome/).

Test with: `tox`.
