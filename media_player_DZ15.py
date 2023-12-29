import requests

class Player:
    def player_data(self, player_name, video_search, access, duration = 480):
        self.player_name = player_name
        self.video_search = video_search
        self.access = access
        self.duration = duration

    def get_player(self):
        print(self.player_name, self.video_search, self.access, self.duration)

    def play(self, url):
        domain = url.split('/')[2]
        try:
            req = requests.get(url)
            print(domain, req.status_code)
        except Exception as e:
            print(domain, e)

    def duration(self, data):
        if 479 < data < 1080:
            print('це середня якicть')
        else:
            print('це низька якicть')

megogo = Player()
megogo.player_data("megogo", True, "paid", 720)
megogo.get_player()

youtube = Player()
youtube.player_data("youtube", True, "for free", 480)
youtube.get_player()

film_player = Player()
film_player.play('https://megogo.net/ru/view/2113971-odin-doma.html')
# url_list = [
#     "https://megogo.net/ru/view/2113971-odin-doma.html,"
#     "https://kinokrad.cc/469991-motstandaren.html",
#     "https://rezka.ag/films/comedy/65153-otlichnyy-gamburger-2-2023.html",
#     "https://kinogo.inc/films/21601-zakroyte-glaza.html


