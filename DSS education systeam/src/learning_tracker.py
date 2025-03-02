class LearningTracker:
    def __init__(self):
        self.progress = {}

    def track_progress(self, user_id, progress):
        self.progress[user_id] = progress

    def get_progress(self, user_id):
        return self.progress.get(user_id, "No progress recorded")
