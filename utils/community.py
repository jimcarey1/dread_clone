from subdread.models import SubDread

def is_community_setup(subdread:SubDread):
    if (subdread.posts.count() >= 3) and (subdread.rules.count() >= 1) and (subdread.flairs.count() >= 1):
        return True
    return False