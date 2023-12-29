import os

class Film:
    type = 'movie'

    def __init__(self, title, storage_address, rating, year):
        self.film_data(title, storage_address, rating, year)
        self.get_film()

    def film_data(self, title, storage_address, rating=7.7, year=1999):
        self.title = title
        self.storage_address = storage_address
        self.rating = rating
        self.year = year

    def get_film(self):
        print('title :', self.title, self.storage_address, 'year :', self.year, 'rating :', self.rating)

film1 = Film('Being John Malkovich', 'https://mu.rezka.app/films/1-fantasy/6798-byt-dzhonom-malkovichem-1999.html', 8,1999)
film2 = Film('Sleepy Hollow', 'https://kinogo.uk/3692-sonnaja-loschina-1999.html', 7.3, 1999)
film3 = Film('Office Space', 'https://the-hdrezka.com/22384-ofisnoe-prostranstvo.html', 7.7, 1999)
film_info = []
film_title_info = []
film1_res = []
film2_res = []
film3_res = []
film_title_dir = []
film1_res.append('{}, {}, {}, {}'.format(film1.title, film1.storage_address, film1.rating, film1.year))
film2_res.append('{}, {}, {}, {}'.format(film2.title, film2.storage_address, film2.rating, film2.year))
film3_res.append('{}, {}, {}, {}'.format(film3.title, film3.storage_address, film3.rating, film3.year))
film_info.extend(list((film1_res, film2_res, film3_res)))
film_title_info.extend(list((film1.title, film2.title, film3.title)))


class FilmDir(Film):
    def __init__(self, title, storage_address, rating, year):
        super().__init__(title, storage_address, rating, year)
        self.save_data(film_title_info)
        self.upload_file(film_title_info)
        self.get_film_address(film_title_info)


    def save_data(self, num):
        for data in num:
            film_title_dir = os.path.join('film_storage', data[0], data)
            os.makedirs(film_title_dir, exist_ok=True)
            for row in film_info:
                if row[0][0] == data[0]:
                    file_path = 'film.json'
                    file_json_path = os.path.join(film_title_dir, file_path)
                    if not os.path.exists(file_json_path):
                        with open(file_json_path, 'a', encoding='utf-8') as film_obj:
                            film_obj.write(''.join(row[0]))
                    else:
                        with open(file_json_path, 'r', encoding='utf-8') as film_obj:
                            film_obj.read()

    def upload_file(self, res):
        for data in res:
            film_title_dir = os.path.join('film_storage', data[0], data)
            if data[0] == res[0][0]:
                file_path = f'{data}.txt'
                file_json_path = os.path.join(film_title_dir, file_path)
                if not os.path.exists(file_json_path):
                    with open(file_json_path, 'a', encoding='utf-8') as film_obj:
                        film_obj.write(''.join(data))
                else:
                    with open(file_json_path, 'r', encoding='utf-8') as film_obj:
                        film_obj.read()

    def get_film_address(self, res):
        for data in res:
            film_title_dir = os.path.join('film_storage', data[0], data)
        print('Завдання 8: ', film_title_dir)

film1 = FilmDir('Being John Malkovich', 'https://mu.rezka.app/films/1-fantasy/6798-byt-dzhonom-malkovichem-1999.html', 8,1999)
film2 = FilmDir('Sleepy Hollow', 'https://kinogo.uk/3692-sonnaja-loschina-1999.html', 7.3, 1999)
film3 = FilmDir('Office Space', 'https://the-hdrezka.com/22384-ofisnoe-prostranstvo.html', 7.7, 1999)

