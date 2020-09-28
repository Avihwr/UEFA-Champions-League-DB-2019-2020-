from django.db import models

# Create your models here.


MANAGER_CHOICES = [('Hans-Dieter Flick', 'Hans-Dieter Flick',),
                   ('Thomas Tuchel',
                    'Thomas Tuchel',),
                   ('Pep Guardiola',
                    'Pep Guardiola',),
                   ('Jürgen Klopp',
                    'Jürgen Klopp',),
                   ('Ronald Koeman',
                    'Ronald Koeman',),
                   ('Frank Lampard',
                    'Frank Lampard',),
                   ('Zinédine Zidane',
                    'Zinédine Zidane',),
                   ('Diego Simeone',
                    'Diego Simeone',),
                   ('José Mourinho',
                    'José Mourinho',),
                   ('Antonio Conte',
                    'Antonio Conte',),
                   ('Andrea Pirlo',
                    'Andrea Pirlo',),
                   ('Gennaro Gattuso',
                    'Gennaro Gattuso',),
                   ('Lucien Favre',
                    'Lucien Favre',),
                   ('Julian Nagelsmann',
                    'Julian Nagelsmann',),
                   ('Jorge Jesus',
                    'Jorge Jesus',),
                   ('Gian Piero Gasperini',
                    'Gian Piero Gasperini',),
                   ('Rudi Garcia',
                    'Rudi Garcia',),
                   ('Peter Bosz',
                    'Peter Bosz',),
                   ('Javi Gracia',
                    'Javi Gracia',),
                   ('Erik ten Hag',
                    'Erik ten Hag',),
                   ('Christophe Galtier',
                    'Christophe Galtier',),
                   ('Sergey Semak',
                    'Sergey Semak',),
                   ('Luís Castro',
                    'Luís Castro',),
                   ('Jesse Marsch',
                    'Jesse Marsch',),
                   ('Philippe Clement',
                    'Philippe Clement',),
                   ('Hannes Wolf',
                    'Hannes Wolf',),
                   ('Pedro Martins',
                    'Pedro Martins',),
                   ('Zoran Mamic',
                    'Zoran Mamic',),
                   ('Marko Nikolic',
                    'Marko Nikolic',),
                   ('Fatih Terim',
                    'Fatih Terim',),
                   ('Dejan Stanković',
                    'Dejan Stanković',),
                   ('Jindrich Trpisovsky',
                    'Jindrich Trpisovsky',)]

TEAM_CHOICES = [
    ('Bayern Munich', 'Bayern Munich'),
    ('Paris Saint-Germain', 'Paris Saint-Germain'),
    ('Manchester City', 'Manchester City'),
    ('Liverpool FC', 'Liverpool FC'),
    ('FC Barcelona', 'FC Barcelona'),
    ('Chelsea FC', 'Chelsea FC'),
    ('Real Madrid', 'Real Madrid'),
    ('Atlético Madrid', 'Atlético Madrid'),
    ('Tottenham Hotspur', 'Tottenham Hotspur'),
    ('Inter Milan', 'Inter Milan'),
    ('Juventus FC', 'Juventus FC'),
    ('SSC Napoli', 'SSC Napoli'),
    ('Borussia Dortmund', 'Borussia Dortmund'),
    ('RB Leipzi', 'RB Leipzi'),
    ('SL Benfica', 'SL Benfica'),
    ('Atalanta BC', 'Atalanta BC'),
    ('Olympique Lyon', 'Olympique Lyon'),
    ('Bayer 04 Leverkusen', 'Bayer 04 Leverkusen'),
    ('Valencia CF', 'Valencia CF'),
    ('Ajax Amsterdam', 'Ajax Amsterdam'),
    ('LOSC Lille', 'LOSC Lille'),
    ('Zenit St. Petersburg', 'Zenit St. Petersburg'),
    ('Shakhtar Donetsk', 'Shakhtar Donetsk'),
    ('Red Bull Salzburg', 'Red Bull Salzburg'),
    ('Club Brugge KV', 'Club Brugge KV'),
    ('KRC Genk', 'KRC Genk'),
    ('Olympiacos Piraeus', 'Olympiacos Piraeus'),
    ('GNK Dinamo Zagreb', 'GNK Dinamo Zagreb'),
    ('Lokomotiv Moscow', 'Lokomotiv Moscow'),
    ('Galatasaray SK', 'Galatasaray SK'),
    ('Red Star Belgrade', 'Red Star Belgrade'),
    ('SK Slavia Prague', 'SK Slavia Prague'),
]

PLAYER_CHOICES = [
    ('Robert Lewandowski', 'Robert Lewandowski'),
    ('Erling Braut Haaland',
     'Erling Braut Haaland'),
    ('Serge Gnabry',
     'Serge Gnabry'),
    ('Rahim Sterling',
     'Rahim Sterling'),
    ('Memphis Depay',
     'Memphis Depay'),
    ('Harry Kane',
     'Harry Kane'),
    ('Dries Mertens',
     'Dries Mertens'),
    ('Gabriel Jesus',
     'Gabriel Jesus'),
    ('Josip Ilicic',
     'Josip Ilicic'),
    ('Kylian Mbappe',
     'Kylian Mbappe'),
    ('Icardi',
     'Icardi'),
    ('Karim Benzema',
     'Karim Benzema'),
    ('Luis Suárez',
     'Luis Suárez'),
    ('Heung-Min Son',
     'Heung-Min Son'),
    ('Lautaro Martínez',
     'Lautaro Martínez'),
    ('Rodrygo',
     'Rodrygo'),
    ('Mislav Orsic',
     'Mislav Orsic'),
    ('Mohamed Salah',
     'Mohamed Salah'),
    ('Emil Forsberg',
     'Emil Forsberg'),
    ('Thomas Müller',
     'Thomas Müller'),
    ('Cristiano Ronaldo',
     'Cristiano Ronaldo'),
    ('M. Sabitzer',
     'M. Sabitzer'),
    ('Timo Werner',
     'Timo Werner'),
    ('Achraf Hakimi',
     'Achraf Hakimi'),
    ('Quincy Promes',
     'Quincy Promes'),
    ('Pasalic',
     'Pasalic'),
    ('Tammy Abraham',
     'Tammy Abraham'),
    ('Angel Di María',
     'Angel Di María'),
    ('Neymar Jr.',
     'Neymar Jr.'),
    ('Arkadiusz Milik',
     'Arkadiusz Milik'),
    ('Paulo Dybala',
     'Paulo Dybala'),
    ('Dani Olmo',
     'Dani Olmo'),
    ('Oxlade-Chamberlain',
     'Oxlade-Chamberlain'),
    ('Tolisso',
     'Tolisso'),
    ('Perisic',
     'Perisic'),
    ('João Félix',
     'João Félix'),
    ('Hwang Hee-Chan',
     'Hwang Hee-Chan'),
    ('Pizzi',
     'Pizzi'),
    ('Coutinho',
     'Coutinho'),
    ('Kingsley Coman',
     'Kingsley Coman'),
    ('Lionel Messi',
     'Lionel Messi'),
    ('Álvaro Morata',
     'Álvaro Morata'),
    ('Mbwana Aly Samatta',
     'Mbwana Aly Samatta'),
    ('El-Arabi',
     'El-Arabi'),
    ('Rúben Afonso Borges Semedo',
     'Rúben Afonso Borges Semedo'),
    ('Tomas Soucek',
     'Tomas Soucek'),
    ('Higuaín', 'Higuaín'),
    ('Joshua Kimmich',
     'Joshua Kimmich'),
    ('Takumi Minamino',
     'Takumi Minamino'),
    ('Sergio Ramos',
     'Sergio Ramos'),
    ('Manuel Neuer',
     'Manuel Neuer'),
    ('David Silva',
     'David Silva'),
    ('Andreas Ulmer',
     'Andreas Ulmer'),
    ('Girgio Chiellini',
     'Girgio Chiellini'),
    ('Dani Parejo',
     'Dani Parejo'),
    ('Taison',
     'Taison'),
    ('Hulk',
     'Hulk'),
    ('Lars Bender',
     'Lars Bender'),
    ('Guilherme',
     'Guilherme'),
    ('Ruud Vormer',
     'Ruud Vormer'),
    ('José Fonte',
     'José Fonte'),
    ('Stevan Stojanovic',
     'Stevan Stojanovic'),
    ('Fernando Muslera',
     'Fernando Muslera'),
]

IMG_CHOICES = [
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lew/large/19319.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lew/large/19319.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/e/erl/large/46369.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/e/erl/large/46369.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/20737.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/20737.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ste/large/21357.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ste/large/21357.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/d/dep/large/21564.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/d/dep/large/21564.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kan/large/20771.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kan/large/20771.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mer/large/19804.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mer/large/19804.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/g/gab/large/37013.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/g/gab/large/37013.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/jos/large/20952.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/jos/large/20952.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kyl/large/33539.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kyl/large/33539.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/i/ica/large/20961.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/i/ica/large/20961.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/b/ben/large/15784.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/b/ben/large/15784.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lui/large/18478.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lui/large/18478.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/son/large/20434.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/son/large/20434.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lau/large/34156.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/l/lau/large/34156.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/r/rod/large/40471.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/r/rod/large/40471.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/sal/large/21766.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/sal/large/21766.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/f/for/large/26182.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/f/for/large/26182.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mul/large/18302.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mul/large/18302.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/c/cri/large/14558.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/c/cri/large/14558.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/m_s/large/23713.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/m_s/large/23713.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tim/large/22911.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tim/large/22911.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/a/ach/large/35147.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/a/ach/large/35147.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/q/qui/large/24989.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/q/qui/large/24989.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/pas/large/25027.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/pas/large/25027.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tam/large/34877.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tam/large/34877.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/d/di_/large/17825.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/d/di_/large/17825.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/n/ney/large/19355.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/n/ney/large/19355.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/a/ark/large/20418.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/a/ark/large/20418.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/pau/large/20958.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/pau/large/20958.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/o/oxl/large/19560.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/o/oxl/large/19560.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tol/large/22940.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tol/large/22940.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/per/large/22661.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/per/large/22661.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/joa/large/44227.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/joa/large/44227.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/piz/large/19387.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/p/piz/large/19387.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/c/cou/large/19546.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/c/cou/large/19546.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kin/large/20182.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/k/kin/large/20182.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mes/large/15167.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mes/large/15167.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mor/large/22240.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/mor/large/22240.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/silueta-generica-large.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/e/el_/100/20283.jpg',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/e/el_/100/20283.jpg'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/sem/large/32696.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/sem/large/32696.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tom/large/39609.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/t/tom/large/39609.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/h/hig/large/16907.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/h/hig/large/16907.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/jos/large/31252.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/j/jos/large/31252.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/min/large/36039.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/m/min/large/36039.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/14962.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/14962.png'),
    ('//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/14962.png',
     '//as01.epimg.net/img/comunes/fotos/fichas/deportistas/s/ser/large/14962.png'),
]


class Stadium(models.Model):
    Stadium = models.CharField(max_length=100)

    def __str__(self):
        return self.Stadium


class Captain(models.Model):
    Captain = models.CharField(max_length=100)

    def __str__(self):
        return self.Captain


class Group(models.Model):
    Groups = models.CharField(max_length=100)

    def __str__(self):
        return self.Groups


class TeamGroups(models.Model):
    TeamGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    Team1 = models.CharField(max_length=100)
    Team2 = models.CharField(max_length=100)
    Team3 = models.CharField(max_length=100)
    Team4 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.TeamGroup)


class Manager(models.Model):
    Manager_name = models.CharField(max_length=100, choices=MANAGER_CHOICES)
    Manager_team = models.CharField(max_length=100, choices=TEAM_CHOICES)
    Manager_age = models.PositiveIntegerField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.Manager_name


class AllTeams(models.Model):
    teams = models.CharField(max_length=100, choices=TEAM_CHOICES)

    def __str__(self):
        return str(self.teams)


class Club(models.Model):
    Club_Manager = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name="manager", null=True)
    Club_Name = models.OneToOneField(AllTeams, on_delete=models.CASCADE, null=True)
    Club_Captain = models.OneToOneField(Captain, on_delete=models.CASCADE, null=True)
    Relation = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    Goals = models.PositiveIntegerField(null=True)
    Stadium = models.OneToOneField(Stadium, on_delete=models.CASCADE, null=True)
    Market_Value = models.FloatField(max_length=50, null=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return str(self.Club_Name)


class Player(models.Model):
    Name = models.CharField(max_length=100, choices=PLAYER_CHOICES, null=True)
    Club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    Age = models.PositiveIntegerField(null=True)
    Goals = models.PositiveIntegerField(null=True)
    Overall = models.PositiveIntegerField(null=True)
    Market_Value = models.FloatField(max_length=50, null=True)
    imgsrc = models.CharField(max_length=200, null=True, choices=IMG_CHOICES)
    is_Captain = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Name)

    class Meta:
        ordering = ['-Overall']
