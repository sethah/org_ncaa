
YEAR_MAP = {10440: 2010, 10260: 2009, 10740: 2011, 11220: 2012, 11540: 2013, 12020: 2014}

ALIASES = {'Cal St. Northridge': 'CSUN',
           'UNC Wilmington': 'UNCW',
           'SIU Edwardsville': 'SIUE'}
REVERSE_ALIAS = {v: k for k, v in ALIASES.iteritems()}

def stats_link(game_id, link_type='box'):
    """Construct box stats and play-by-play stats links from stats.ncaa.org game id"""
    assert link_type in {'box', 'pbp'}, "invalid link type: %s" % link_type
    if link_type == 'box':
        link = 'http://stats.ncaa.org/game/box_score/%s' % game_id
    elif link_type == 'pbp':
        link = 'http://stats.ncaa.org/game/play_by_play/%s' % game_id

    return link

def all_years():
    """All current available years for stats.ncaa.org"""
    return [v for k, v in YEAR_MAP.iteritems()]

def convert_ncaa_year_code(val):
    """Swap between the stats.ncaa.org year code and the actual year."""
    code_to_year = YEAR_MAP
    year_to_code = {v: k for k, v in code_to_year.iteritems()}
    if val in code_to_year:
        return code_to_year[val]
    elif val in year_to_code:
        return year_to_code[val]
    else:
        return None