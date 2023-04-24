============================
gh_loc
============================

Some miscellaneous attempts at aggregating statistics on
repositories in the pcdshub organization.  (or any organization I guess)

Currently extremely hacky, with little done in the way of generalizability.


Some notes:
* Uses the codetabs api to gather LOC information on each repository.
    * This could in theory be performed on our own local storage by cloning and counting
        each repository, but why do that when we can have someone else do it
    * A key limitation of this is a limit of one request / 5s, stymying attempts
        to run this asynchronously

* Currently PLC code is recognized as XML code, which is technically true but
    potentially confusing.

* 