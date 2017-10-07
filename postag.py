from konlpy.tag import *

class PosTag:

    def hannanum(self, items):
        hannanum = Hannanum()
        for item in items:
            item.context = hannanum.pos(item.context_backup)
            
    def twitter(self, items):
        twitter = Twitter()
        for item in items:
            item.context = twitter.pos(item.context_backup)
