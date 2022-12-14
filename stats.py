class Stats():
    """tracking statics"""

    def __init__(self):
        """initialisation statics"""
        self.reset_stats()
        self.run_game = True
    def reset_stats(self):
        """statistics changing in time game"""
        self.guns_left = 2
        self.score = 0
        
