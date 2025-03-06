class ZaporanaHodnota(Exception):
    pass

class NedostatecnyZustatek(Exception):
    pass


class Osoba:
    def __init__(self, jmeno, rc):
        self.jmeno = jmeno
        self.rc = rc


class BankovniUcet:
    def __init__(self, vlastnik):
        self.__vlastnik = vlastnik
        self.__zustatek = 0
    
    @property
    def vlastnik(self):
        return self.__vlastnik

    @property
    def zustatek(self):
        return self.__zustatek
    
    def vloz(self, suma):
        if suma <= 0:
            raise ZaporanaHodnota("Vkladame zapornou hodnotu")
        self.__zustatek += suma
    
    def vyber(self, suma):
        if self.__zustatek < suma:
            raise NedostatecnyZustatek("Nemuzeme vybrat vic nez mame na ucte")
        self.__zustatek -= suma
    
    def __str__(self):
        return f"Ucet(vlastnik={self.vlastnik.jmeno}, zustatek={self.zustatek})"


if __name__ == "__main__":
    try:
        ja = Osoba("Vladimir Kobzev", "123456/7890")
        muj_ucet = BankovniUcet(ja)
        print(muj_ucet)
    except NedostatecnyZustatek as e:
        print(str(e))