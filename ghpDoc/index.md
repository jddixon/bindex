<h1 class="libTop">bindex</h1>

**bindex** (probably a temporary name) is a tool for managing indexes
by name into a set of BuildLists stored by content key.

A [BuildList](https://jddixon.github.io/buildList)
contains an indented list of names and hashes.  The names are
typically file names.  If a hash is present, it is the SHA1 or SHA256
hash of the contents of the file named.  If there is no hash, the name
is that of a directory.  Any files in that directory will appear in the
lines below, indented by one additional space.

The BuildList begins with a
a header which contains an RSA public key, a title, and a timestamp.
If the BuildList has been signed, the RSA-SHA1 digital signature will
appear at the bottom of the serialized BuildList.  The signatory
guarantees that only one BuildList exists this title and timestamp.

The BuildList can be seen as an index from a **content key** to a file name.
A user can use the content key to verify the integrity of the file: the
user hashes the file; if the result differs from the hash in the build list,
the user can safely conclude that the file is corrupt.

In the XLattice system (
[Java version](https://jddixon.github.io/xlattice_java),
[Go version](https://jddixon.github.io/xlattice_go),
[Python3 version](https://jddixon.github.io/xlattice_py)),
files are typically stored by content key rather than by name, and
BuildLists are used to map file names into content keys.

BuildLists can be stored either by name in the (POSIX or Windows) file
system or by content key.  In either case a BuildList index, a **Bindex**,
is used to handle the mapping.

Most commonly a user will want to retrieve the most recent BuildList, the
one with the most recent timestamp.  To do this, the user will
supply the RSA public key of the signatory and the title of the BuildList.
The system will use this to find the content key of the most recent
BuildList.  It will then return either that content key or the file itself.

## Project Status

Rough specification

