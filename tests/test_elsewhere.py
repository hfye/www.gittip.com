from __future__ import unicode_literals
from gittip.elsewhere.twitter import TwitterAccount
from gittip.testing import Harness

# I ended up using TwitterAccount to test even though this is generic
# functionality, because the base class is too abstract.


class TestAccountElsewhere(Harness):

    def test_opt_in_can_change_username(self):
        account = TwitterAccount("alice", {})
        expected = "bob"
        actual = account.opt_in("bob")[0].username
        assert actual == expected, actual

    def test_opt_in_doesnt_have_to_change_username(self):
        self.make_participant("bob")
        account = TwitterAccount("alice", {})
        expected = account.participant # A random one.
        actual = account.opt_in("bob")[0].username
        assert actual == expected, actual
