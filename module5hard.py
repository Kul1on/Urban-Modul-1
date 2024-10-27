import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_password(password)  # Храним хэш пароля
        self.age = age

    def _hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Вход выполнен: {nickname}")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Выполняем автоматический вход
        print(f"Регистрация выполнена: {nickname}")

    def log_out(self):
        print(f"Пользователь {self.current_user} вышел")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует и не будет добавлено повторно.")

    def get_videos(self, keyword):
        keyword_lower = keyword.lower()
        return [video.title for video in self.videos if keyword_lower in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено.")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        print(f"Воспроизведение видео: {video.title}")
        for sec in range(video.time_now + 1, video.duration + 1):
            print(sec, end=" ")
            time.sleep(1)  # Задержка для эмуляции просмотра
        print("Конец видео")
        video.time_now = 0  # Сброс таймера просмотра видео

    def __str__(self):
        return f"UrTube: {len(self.users)} пользователей, {len(self.videos)} видео"
