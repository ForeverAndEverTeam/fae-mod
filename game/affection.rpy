#Affection chart singleton
init python:
    def slerp(x, a, b):
        if a > b:
            return slerp(x, b, a)
        if x < a:
            return a
        elif x > b:
            return b
        return x

    class Affection:
        def __init__(self, friendship = 0.5, romance = 0.0, romance_unlocked = False):
            self.friendship = friendship #The friendship score: 0.0 = hatred, 1.0 = best friends
            self.romance = romance #The romance score: 0.0 = aromantic, 1.0 = passionate lovers
            self.romance_unlocked = romance_unlocked #If romantic interactions are unlocked
            self.linked_list = None #A linked list that duplicates the scores, i.e. to store in persistent
        
        def tuple(self):
            """Return the affection scores as a tuple (friendship, romance)"""
            return (self.friendship, self.romance)
        
        def __tuple__(self):
            return self.tuple()
        
        def sync_list(self):
            """Sync the affection data with the linked list"""
            if not self.linked_list:
                return
            self.linked_list[0] = self.friendship
            self.linked_list[1] = self.romance
            self.linked_list[2] = self.romance_unlocked
        
        def link_list(self, l):
            """Link a list to duplicate the affection data in a more "fundumental" way"""
            self.linked_list = l
            self.sync_list()

        def set(self, friendship = None, romance = None):
            """Set the affection scores to given number of points.
            If you want to keep the same value of one score, set its argument to None.
            NOTE: If romance_unlocked == False, this function won't affect its score."""
            if friendship is not None:
                self.friendship = slerp(friendship, 0.0, 1.0)
            if romance is not None and self.romance_unlocked:
                self.romance = slerp(romance, 0.0, 1.0)
            self.sync_list()
        
        def increase(self, friendship = 0.0, romance = 0.0):
            """Increase the affection scores by given number of points.
            If you want to keep the same value of one score, set the increase to 0.0"""
            friendship += self.friendship
            romance += self.romance
            self.set(friendship, romance)
    #Initialize the Affecton object
    if not persistent.affection_data:
        persistent.affection_data = [0.5, 0.0, False]
    affection = Affection(*persistent.affection_data)
    affection.link_list(persistent.affection_data)