class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __eq__(self, other):
        if self.nickname == other.nickname and self.password == other.password:
            return True


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        list_user = []
        for user_ in self.users:
            list_user.append(user_.nickname)

        if nickname not in list_user:
            user_ = User(nickname, password, age)
            user_.nickname = nickname
            user_.password = hash(password)
            user_.age = int(age)
            self.users.append(user_)
            self.current_user = len(self.users) - 1
        else:
            print(f'Пользователь {nickname} уже существует')
            self.current_user = list_user.index(nickname)

    def get_current_user(self):
        return self.users[self.current_user].nickname

    def log_in(self, nickname, password):
        counter = 0
        for user_ in self.users:
            if nickname == user_.nickname and hash(password) == user_.password:
                self.current_user = counter
                break

            counter += 1

    def log_out(self):
        self.current_user = None

    def add(self, *other):
        list_title = []  # creating a list of films
        # If this is not the first call
        for videos_ in self.videos:
            list_title.append(videos_.title)
        # add film in UrTube
        for item in other:
            if item.title not in list_title:
                self.videos.append(item)
                list_title.append(item.title)

    def get_videos(self, str_):
        list_title = []
        for video_ in self.videos:
            if str_.lower() in video_.title.lower():
                list_title.append(video_.title)

        return list_title

    def watch_video(self, title):
        from time import sleep
        for video_ in self.videos:
            if video_.title == title:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                    return

                if video_.adult_mode:
                    if self.users[self.current_user].age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return

                durat = video_.duration
                start_video = video_.time_now

                for _ in range(durat + 1):
                    print(start_video, end=' ')
                    sleep(1)
                    start_video += 1

                print('"Конец видео"')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.get_current_user())

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
