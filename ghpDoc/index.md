<h1 class="libTop">bindex</h1>

**bindex** (probably a temporary name) is a tool for managing indexes
by name into a set of BuildLists stored by content key.

A
[BuildList](https://jddixon.github.io/xlattice/buildList)
contains an indented list of names and hashes.  The names are
typically file names.  If a hash is present, it is the SHA1 or SHA256
hash of the contents of the file named.  If there is no hash, the name
is that of a directory.  Any files in that directory will appear in the
lines below, indented by one additional space.

The BuildList begins with
a header which contains an RSA public key, a title, and a timestamp.
If the BuildList has been signed, the RSA-SHA1 digital signature will
appear at the bottom of the serialized BuildList.  The signatory
guarantees that only one BuildList exists this title and timestamp.

A example of a BuildList (abbreviated and reformatted for clarity):

    -----BEGIN RSA PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoM2sBgX0ChP2JriXkOxS
    e2FjHYVzBGkNvgf0vIAa7FFYZi2pWmxBAVXgl3tTiB3quqqud/MbKqdejM6gkKBK
    v8f7hlcBQLD6BLIZ/RRfhIElc+WlDVfKSnBTB4va5qTQAgvuq5i8+oMj7G8WEy5d
    7cYucWyUJMtHvT4pCDtBWeeqQ62tByWjv34Ud/+A9Mjf0leiWxM3tiToVsqIKb4s
    zPjEShF9rvcNa9XEy1dKpcDz9Szbm2SlxOgM83fDDGtOq4SSCSqndtxrOvXXPB57
    H1mJV/FmerbXRPm5ERJVNIxtLk7Gr2Ce45FVlWyJGMhpfVlKkkk+bRQ02OFfazJI
    GQIDAQAB
    -----END RSA PUBLIC KEY-----
    bindex v0.0.13
    2016-06-20 20:16:30
    # START CONTENT #
    bindex
     .copyright 304c14d702dff7c6c2c39729ff62aed7203b3427
     .dvcz
      builds ae0bb04143d8d45e9614924ca5c3c7c6d81138f9
      lastBuildList ec90d6124a9c0241430d51a13a3e4232ff3d5b52
      projCfg c6fc5c724af42ea24278c5be68b08155eb3ed0a9
      projCfg.local a9f0457240a0b968bb179fdd0157b6bc9be4055a
      version 786533f21663fffa461b6a5c4756ff5a3e2a54aa
     .gitignore 5f1a04317952b671c5828218c6efe88c2594f8fb
     CHANGES 45e4e99874cce47a511ac6316d6989c7a7b3ca69
     LICENSE.md ef87ef0aafe2bb3dc3b3ab29651c52e8add097b4
     MANIFEST.in 35fa674699802cec92495df6b90f6ea06d81340b
     README.md 8a50e9ea19bfcc5392ae9ee22d9eaf4b95f52985
     TODO 0e3a7a9f760c70bb2712e6bd94cf3088592861fe
     bindex
      __init__.py a4cf66fe489593b90eb892e4fdb945232be0e3c8
     bkp2U 645fc4ac0ec5511b371c0a5487f79329aea64b8c
     countem e5dabc321ac196911709c07f3ad0dfb5719905d4
     dist
      ...
     ghpDoc
      css
       LICENSE.html5-boilerplate.md ded771b3245b190da0e81c76de5a80d41392c0a6
       ghp.css 1d6ebe8a6cf8f61f4645a793cb087dfae2420f33
       main.css 018ed80b8a6e6607bc7c08595fa5a7fa56853885
       normalize.css cba40c7ce3d558d00ff79d7505ac3d348015ec9c
      img
       GitHub-Mark-32px.png fabe53eb72f9b6d3d47cd95aff31ffc45c2fdbf8
       chunk.jpg de2b27e41f1547fc14b13399f5906b4303b49657
       chunk2.jpg d0593d312dbb8ea837c17b28cb639726e29ea93b
       cluster-with-clients.jpg c167d04c0c6b5736ef9fe4cdc3fcce1956fdea78
       simple-cluster.jpg 6b223ddd25937c1ef75ef328f36fc3436f10bd62
       xl-registration.jpg 15cbf951f9db173a45428b32dcec87aca83bbdf0
       xlattice-2014.jpg f185aaad06db71acd9454f31054c62c56d36f37f
      index.md 52bbf099e3b4c96eefdecce7ce20f69262339619
     installit d54edb06fa07010fe69bfb544ef8ed3b00c2baa4
     setup.py d242b5be53837de1d746a5ab293ae5ca8393d3ba
     styleit 00c200cee064f03044b071fc6bd73d4650a41615
     test.all bff9c58665104f46b8c0477cf8729029fab8aea4
    # END CONTENT #

    H5l1YnoUNqGvIjUXVwQWEvITVK6dySFTw1MW0hBONf6IY4RPOL868DsDPSpeYKPmW
    OLkjHgxHGvRfEK8v0D7F228E6ra0CrFmq1BpScXPYix2WKo1y9vuisxBTJjYR1AA8
    VmicSDMmu9vlHVCLdMxm9i0Ta9/6FLO3cGZACw1ETSmNpih75Pg5jHjGru/vBl5Uq
    tj4PYBq7yeoMBB3G3v5LPvtUjgIi3p08Zzs+I/zWDhih7WLQ7AUT0vKi9oVMhTeJR
    iaL9aJqEsJBhg9cAGA+J6HiwJUP1xUZGjKRft65rmxT0ZunGLZSgLXKo0IYNih9O6
    To8Ec2UqiZbGaeRLg==

The example is the BuildList for the bindex project at the stated
time on 20 June 2016.  Content begins immediately after the timestamp.
Project files are stored in the directory `bindex`, named in the first
content line.  The first file listed is `.copyright'.  Its conent key,
beginning with hex `304c14` immediately follows the name.  File and
directory names are sorted alphabetically.  The list of files and
content kyes is followed by a digital signature (reformatted for
readability).

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

Rough specification.

