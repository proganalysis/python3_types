from test_fena.test_common import test_cmd

def test_teams():
    test_cmd("team add _team team_test", "team add fena.team team_test")
    test_cmd("team add _team team test", "team add fena.team team test")
    test_cmd("team empty _team",         "team empty fena.team")
    test_cmd("team _team + @a",          "team join fena.team @a")
    test_cmd("team _team + target",      "team join fena.team target")
    test_cmd("team leave @a",            "team leave @a")
    test_cmd("team leave target",        "team leave target")
    test_cmd("team remove _team",        "team remove fena.team")

    test_cmd("team _team friendlyfire = true",               "team option fena.team friendlyfire true")
    test_cmd("team _team color = green",                     "team option fena.team color green")
    test_cmd("team _team seeFriendlyInvisibles = false",     "team option fena.team seeFriendlyInvisibles false")
    test_cmd("team _team nametagVisibility = hideForOwnTeam", "team option fena.team nametagVisibility hideForOwnTeam")
    test_cmd("team _team deathMessageVisibility = never",    "team option fena.team deathMessageVisibility never")
    test_cmd("team _team collisionRule = pushOwnTeam",       "team option fena.team collisionRule pushOwnTeam")

    test_cmd(r'team _team prefix = {"text":"PREFIX","color":"blue"}', r'team option fena.team prefix {"text":"PREFIX","color":"blue"}')
    test_cmd(r'team _team suffix = {"text":"SUFFIX","color":"red"}', r'team option fena.team suffix {"text":"SUFFIX","color":"red"}')
