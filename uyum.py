class UnluUyumuSorgula():
    def __init__(self, kelime):
        self.UIUnluUyumuSorgulanabilirMi = self.UyumIncelenimiSorgula(kelime)
		
        self.UIBuyukUnluUyumuKontrolu = self.BuyukUnluUyumuKontrolu(kelime)
        self.UIBuyukUnluUyumuKalinlikItibariyleKontrolu = self.BuyukUnluUyumuKalinlikItibariyleKontrolu(kelime)
        self.UIBuyukUnluUyumuIncelikItibariyleKontrolu = self.BuyukUnluUyumuIncelikItibariyleKontrolu(kelime)

        #self.UIKucukUnluUyumuKontrolu oluştursak iyiydi, iç simetri olurdu ama böyle bir fonksiyon yaratmadık."
        self.UIKucukUnluUyumuDuzlukItibariyleKontrolu = self.KucukUnluUyumuDuzlukItibariyleKontrolu(kelime)
        self.UIKucukUnluUyumuYuvarlaklikItibariyleKontrolu1= self.KucukUnluUyumuYuvarlaklikItibariyleKontrolu1(kelime)
        self.UIKucukUnluUyumuYuvarlaklikItibariyleKontrolu2 = self.KucukUnluUyumuYuvarlaklikItibariyleKontrolu2(kelime)

        print(f"incelenen kelime = {kelime}")
        print(f"ünlü uyumu sorgulanabilir mi = {self.UIUnluUyumuSorgulanabilirMi}\n")
        
        print(f"büyük ünlü uyumuna uygun mu = {self.UIBuyukUnluUyumuKontrolu}")
        print(f"büyük ünlü uyumuna (kalınlık itibariyele) uygun mu = {self.UIBuyukUnluUyumuKalinlikItibariyleKontrolu}")
        print(f"büyük ünlü uyumuna (incelik itibariyele) uygun mu = {self.UIBuyukUnluUyumuIncelikItibariyleKontrolu}\n")

        print(f"küçük ünlü uyumuna (düzlük itibariyle) uygun mu = {self.UIKucukUnluUyumuDuzlukItibariyleKontrolu}")
        print(f"küçük ünlü uyumuna (yuvarlaklık no:1 itibariyle) uygun mu = {self.UIKucukUnluUyumuYuvarlaklikItibariyleKontrolu1}")
        print(f"küçük ünlü uyumuna (yuvarlaklık no:2 itibariyle) uygun mu = {self.UIKucukUnluUyumuYuvarlaklikItibariyleKontrolu2}")
        
    def UyumIncelenimiSorgula(self, kelime):
        # uyum incelenim sorgula
        sesli= "a","e","ı","i","u","ü","o","ö"
        sayac = 0
        for harf in kelime:
            if harf in sesli:
                sayac += 1
        if sayac >1:
            return "E"
        else:
            return "H"

    def BuyukUnluUyumuKalinlikItibariyleKontrolu(self, kelime):
        # buyuk unlu uyumu kanlik kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        kalin_unluler = ku = "a", "ı", "u", "o"
        ince_unluler = iu = "e", "i", "ü", "ö"

        kelimenin_seslileri = ks = []

        deney_tupu_ince = dti = 0
        deney_tupu_kalin = dtk = 0

        for harf in kelime:
            if harf in s:
                ks += harf
        if len(ks) >= 2:
            for nesne in ks:
                if nesne in iu:
                    dti += 1
                elif nesne in ku:
                    dtk += 1

            if dti > 0:
                return "H"
            if dti <= 0:
                return "E"
        elif len(ks) <= 1:
            return "n"

    def BuyukUnluUyumuIncelikItibariyleKontrolu(self, kelime):
        # buyuk unlu uyumu incelik kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        kalin_unluler = ku = "a", "ı", "u", "o"
        ince_unluler = iu = "e", "i", "ü", "ö"

        kelimenin_seslileri = ks = []

        deney_tupu_ince = dti = 0
        deney_tupu_kalin = dtk = 0

        for harf in kelime:
            if harf in s:
                ks += harf
        if len(ks) >= 2:
            for nesne in ks:
                if nesne in iu:
                    dti += 1
                elif nesne in ku:
                    dtk += 1

            if dtk > 0:
                return "H"
            if dtk <= 0:
                return "E"
        elif len(ks) <= 1:
            return "n"

    def BuyukUnluUyumuKontrolu(self, kelime):
        # buyuk unlu uyumu kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        kalin_unluler = ku = "a", "ı", "u", "o"
        ince_unluler = iu = "e", "i", "ü", "ö"

        kelimenin_seslileri = ks = []

        deney_tupu_ince = dti = 0
        deney_tupu_kalin = dtk = 0

        for harf in kelime:
            if harf in s:
                ks += harf
        if len(ks) >= 2:
            for nesne in ks:
                if nesne in iu:
                    dti += 1
                elif nesne in ku:
                    dtk += 1

            if dtk >= 1:
                if dti >= 1:
                    return "H"

            if dtk >= 1:
                if dti == 0:
                    return "E"
            if dti >= 1:
                if dtk == 0:
                    return "E"
        elif len(ks) <= 1:
            return "n"

    def KucukUnluUyumuDuzlukItibariyleKontrolu(self, kelime):
        # kucuk unlu uyumu -duzden- kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        duz = "a", "e", "ı", "i"

        kelimenin_sesliler = ks = []
        duzlu = []
        diger = []

        for harf in kelime:
            if harf in s:
                ks += [harf]

        for sesli in ks:
            if sesli in duz:
                duzlu += [sesli]
            else:
                diger += [sesli]
        if len(ks) >= 2:
            if len(duzlu) >= 1:
                if len(diger) ==0:
                    return "E"
            if len(duzlu) ==0:
                    return "H"
            if len(duzlu) >= 1:
                if len(diger) >= 1:
                    return "H"
        elif len(ks) <= 1:
            return "n"

    def KucukUnluUyumuYuvarlaklikItibariyleKontrolu1(self, kelime):
        # kucuk unlu uyumu -yuvarlakdan 1- kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        duz_unluler = "a", "e", "ı", "i"
        yuvarlak_unluler = "o", "ö", "u", "ü"
        dar_yuvarlak_unluler = "u", "ü"

        kelimenin_sesliler = ks = []
        ilk_sesli = ils = []
        ikinci_sesli = iks = []

        for harf in kelime:
            if harf in s:
                ks += [harf]

        ils += [ks[0]]
        if len(ks)>1:
            iks += [ks[1]]

        if len(ks) >= 2:
            if ils[0] in duz_unluler:
                return "H"
            elif ils[0] in yuvarlak_unluler:
                if iks[0] in dar_yuvarlak_unluler:
                    return "E"
                elif iks[0] not in dar_yuvarlak_unluler:
                    return "H"
        elif len(ks) == 1:
            return "n"

    def KucukUnluUyumuYuvarlaklikItibariyleKontrolu2(self, kelime):
        # kucuk unlu uyumu -yuvarlakdan 2- kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        duz_unluler = "a", "e", "ı", "i"
        yuvarlak_unluler = "o", "ö", "u", "ü"
        duz_genis_unluler = "a", "e"

        kelimenin_sesliler = ks = []
        ilk_sesli = ils = []
        ikinci_sesli = iks = []

        for harf in kelime:
            if harf in s:
                ks += [harf]

        ils += [ks[0]]
        if len(ks)>1:
            iks += [ks[1]]

        if len(ks) >= 2:
            if ils[0] in duz_unluler:
                return "H"
            elif ils[0] in yuvarlak_unluler:
                if iks[0] in duz_genis_unluler:
                    return "E"
                elif iks[0] not in duz_genis_unluler:
                    return "H"
        elif len(ks) == 1:
            return "n"

ornek = UnluUyumuSorgula("hakkı")
