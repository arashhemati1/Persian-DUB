from locust import HttpUser, task

class DubbingUser(HttpUser):
    @task
    def submit_video(self):
        self.client.post("/asr", files={"file": open("sample.mp4", "rb")})
