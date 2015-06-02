# bindex

**bindex** (probably a temporary name) is a tool for managing indexes
by name into a set of BuildLists stored by content key.

A BuildList contains an indented list of names and hashes.  The names are
typically file names.  If the hash is present it is the SHA1 or SHA256
hash of the contents of the file.  The list of names and hashes is has
a header which contains an RSA public key, a title, and a time stamp.
If the BuildList has been signed, the RSA-SHA1 digital signature will
appear at the bottom of the serialized BuildList.

Stored by content key a BuildList is not easy to find.  A BuildList index, 
a **bindex**, enables BuildLists to be retrieved by the signer's RSA
public key and in chronological or reverse chronological order.

## On-line Documentation

More information on the **bindex** project can be found [here](https://jddixon.github.io/bindex)
