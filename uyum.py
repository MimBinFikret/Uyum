class uyum_sorgula():
    def __init__(self, str_kelime):
        self.u_i_s_d= uyum_sorgula.u_i_s(str_kelime) #bu "_d" kısaltması ...değeri manasına geliyor.
		
        self.buuk_d   = uyum_sorgula.buuk(str_kelime)
        self.buukk_d  = uyum_sorgula.buukk(str_kelime)
        self.buuik_d  = uyum_sorgula.buuik(str_kelime)
		
        #self.kuuk_d= kuuk(kelime) "yani küçük ünlü uyumu kontrolu: ama böyle bir fonksiyon yaratmadık."
        self.kuudk_d  = uyum_sorgula.kuudk(str_kelime)
        self.kuuy1k_d = uyum_sorgula.kuuy1k(str_kelime)
        self.kuuy2k_d = uyum_sorgula.kuuy2k(str_kelime)

        print("incelenen kelime                                              =  "+str_kelime   + "\n")
        
        print("ünlü uyumu sorgulanabilir mi                                  =  "+self.u_i_s_d + "\n")
        
        print("büyük ünlü uyumuna uygun mu                                   =  "+self.buuk_d)
        print("büyük ünlü uyumuna (kalınlık itibariyele) uygun mu            =  "+self.buukk_d)
        print("büyük ünlü uyumuna (incelik  itibariyele) uygun mu            =  "+self.buuik_d + "\n")

        print("küçük ünlü uyumuna (düzlük itibariyle) uygun mu               =  "+self.kuudk_d)
        print("küçük ünlü uyumuna (yuvarlaklık no:1 itibariyle) uygun mu     =  "+self.kuuy1k_d)
        print("küçük ünlü uyumuna (yuvarlaklık no:2 itibariyle) uygun mu     =  "+self.kuuy2k_d)
        

    def u_i_s(kelimeu):
        # uyum incelenim sorgula
        sesli= "a","e","ı","i","u","ü","o","ö"
        sayac = 0
        for harf in kelimeu:
            if harf in sesli:
                sayac += 1
        if sayac >1:
            return "E"
        else:
            return "H"

    def buukk(kelime):
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

    def buuik(kelime):
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

    def buuk(kelime):
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

    def kuudk(kelime):
        # kucuk unlu uyumu -duzden- kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        duz = "a", "e", "ı", "i"

        kelimeninsesliler = ks = []
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

    def kuuy1k(kelime):
        # kucuk unlu uyumu -yuvarlakdan 1- kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        duz_unluler          = "a", "e", "ı", "i"
        yuvarlak_unluler     = "o", "ö", "u", "ü"
        dar_yuvarlak_unluler = "u", "ü"

        kelimeninsesliler  = ks  = []
        ilk_sesli          = ils = []
        ikinci_sesli       = iks = []

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

    def kuuy2k(kelime):
        # kucuk unlu uyumu -yuvarlakdan 2- kontrolu
        sesliler = s = "a", "ı", "u", "o", "e", "i", "ü", "ö"
        duz_unluler          = "a", "e", "ı", "i"
        yuvarlak_unluler     = "o", "ö", "u", "ü"
        duz_genis_unluler    = "a", "e"

        kelimeninsesliler  = ks  = []
        ilk_sesli          = ils = []
        ikinci_sesli       = iks = []

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

ornek = uyum_sorgula("hakkı")
