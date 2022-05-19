from tkinter import*
from random import randint

def okno():
    def Sprawdzam_epoki():
        sprawdzam_epoki.destroy()
        back.destroy()
        odp.lower()
        odp.replace("\n", " ")
        odp.replace(" ", "")
        a = dialog.get()
        a.lower()
        a.replace(" ", "")
        global dobra
        dobra = Label(text="Dobrze!", font=("Consolas", 20), fg="blue")
        global zla
        zla = Label(text="Źle!", font=("Consolas", 20), fg="red")
        if a==odp:
            dobra.pack()
            wstecz(frame, 43)
        else:
            zla.pack()
            wstecz(frame, 44)
    def xle():
        global zla
        A.destroy()
        B.destroy()
        C.destroy()
        zla = Label(text="Źle!", font=("Consolas", 20), fg="red")
        zla.pack()
    def dobrze():
        global dobra
        A.destroy()
        B.destroy()
        C.destroy()
        dobra = Label(text="Dobrze!", font=("Consolas", 20), fg="blue")
        dobra.pack()

    def latwe_granie(frame):
        wstecz(frame, 41)
        los = randint(0, 6)
        global A
        global B
        global C
        global tekst
        global epoki_haslo

        if los == 0:
            plik = open("antyk_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 5)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 1:
            plik = open("sredniowiecze_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 2:
            plik = open("renesans_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 3:
            plik = open("barok_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 4:
            plik = open("oswiecenie_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 2)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 5:
            plik = open("romantyzm_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        else:
            plik = open("pozytywizm_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            plik_epoki = open("nazwy_epok.txt", "r")
            epoque = plik_epoki.readlines()
            plik_epoki.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)

        los_odp = randint(0,2)
        if los_odp==0:
            A = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: dobrze())
            A.pack(side=TOP)
            epoque.pop(los)
            los=randint(0,8)
            B = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: xle())
            B.pack(side=TOP)
            epoque.pop(los)
            los = randint(0, 7)
            C = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: xle())
            C.pack(side=TOP)
        elif los_odp==1:
            B = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: dobrze())
            B.pack(side=TOP)
            epoque.pop(los)
            los = randint(0, 8)
            A = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: xle())
            A.pack(side=TOP)
            epoque.pop(los)
            los = randint(0, 7)
            C = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: xle())
            C.pack(side=TOP)
        elif los_odp==2:
            C = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: dobrze())
            C.pack(side=TOP)
            epoque.pop(los)
            los = randint(0, 8)
            B = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: xle())
            B.pack(side=TOP)
            epoque.pop(los)
            los = randint(0, 7)
            A = Button(text=epoque[los], font=("Consolas", 20), width=20, command=lambda: xle())

    def trudne_granie(frame):
        wstecz(frame, 42)
        los = randint(0, 6)
        global odp
        global epoki_haslo

        plik_epoki = open("nazwy_epok.txt", "r")
        epoque = plik_epoki.readlines()
        plik_epoki.close()
        odp = epoque[los].lower().replace("\n","").replace(" ","")

        if los == 0:
            plik = open("antyk_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 5)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 1:
            plik = open("sredniowiecze_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 2:
            plik = open("renesans_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 3:
            plik = open("barok_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 4:
            plik = open("oswiecenie_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 2)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        elif los == 5:
            plik = open("romantyzm_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        else:
            plik = open("pozytywizm_hasla.txt", "r")
            tekst = plik.readlines()
            plik.close()
            i = randint(0, 3)
            epoki_haslo = Label(text=tekst[i], font=("Consolas", 20))
            epoki_haslo.pack(side=TOP)
        global dialog
        dialog = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        dialog.pack(side="top")
        global sprawdzam_epoki
        sprawdzam_epoki = Button(text="Sprawdz", font=("Consolas", 20), command=lambda: Sprawdzam_epoki())
        sprawdzam_epoki.pack(side=TOP)





    def latwizna(frame):
        latwo.destroy()
        trudno.destroy()
        back.destroy()
        global wstep
        wstep = Label(frame, text="Jakiej epoki hasło widzisz?", font=("Consolas", 25))
        wstep.pack(side="top")
        latwe_granie(frame)
    def trud(frame):
        latwo.destroy()
        trudno.destroy()
        back.destroy()
        global wstep
        wstep = Label(frame, text="Jakiej epoki hasło widzisz?", font=("Consolas", 25))
        wstep.pack(side="top")
        trudne_granie(frame)
    def epoki_check(frame, pkt):
        a = antyk.get()
        antyk.destroy()
        s = sredniowiecze.get()
        sredniowiecze.destroy()
        r = renesans.get()
        renesans.destroy()
        b = barok.get()
        barok.destroy()
        o = oswiecenie.get()
        oswiecenie.destroy()
        rom = romantyzm.get()
        romantyzm.destroy()
        p = pozytywizm.get()
        pozytywizm.destroy()
        m = mloda.get()
        mloda.destroy()
        x = XX.get()
        XX.destroy()
        w =wspolczesnosc.get()
        wspolczesnosc.destroy()
        back.destroy()
        submit.destroy()

        global wantyk
        global wsredniowiecze
        global wrenesans
        global wbarok
        global woswiecenie
        global wromantyzm
        global wpozytywizm
        global wmloda
        global wxx
        global wwspolczesnosc
        global punktacja
        if a.lower().replace(" ", "") == "antyk":
            wantyk = Label(text=a, bg="green", font=("Consolas", 17), width=25)
            wantyk.pack(side="top")
            pkt+=1
        else:
            wantyk = Label(text=a, bg="red", font=("Consolas", 17), width=25)
            wantyk.pack(side="top")
        if s.lower().replace(" ", "") == "średniowiecze":
            wsredniowiecze = Label(text=s, bg="green", font=("Consolas", 17), width=25)
            wsredniowiecze.pack(side="top")
            pkt += 1
        else:
            wsredniowiecze = Label(text=s, bg="red", font=("Consolas", 17), width=25)
            wsredniowiecze.pack(side="top")
        if r.lower().replace(" ", "") == "renesans":
            wrenesans = Label(text=r, bg="green", font=("Consolas", 17), width=25)
            wrenesans.pack(side="top")
            pkt += 1
        else:
            wrenesans = Label(text=r, bg="red", font=("Consolas", 17), width=25)
            wrenesans.pack(side="top")
        if b.lower().replace(" ", "") == "barok":
            wbarok = Label(text=b, bg="green", font=("Consolas", 17), width=25)
            wbarok.pack(side="top")
            pkt += 1
        else:
            wbarok = Label(text=b, bg="red", font=("Consolas", 17), width=25)
            wbarok.pack(side="top")
        if o.lower().replace(" ", "") == "oświecenie":
            woswiecenie = Label(text=o, bg="green", font=("Consolas", 17), width=25)
            woswiecenie.pack(side="top")
            pkt += 1
        else:
            woswiecenie = Label(text=o, bg="red", font=("Consolas", 17), width=25)
            woswiecenie.pack(side="top")
        if rom.lower().replace(" ", "") == "romantyzm":
            wromantyzm = Label(text=rom, bg="green", font=("Consolas", 17), width=25)
            wromantyzm.pack(side="top")
            pkt += 1
        else:
            wromantyzm = Label(text=rom, bg="red", font=("Consolas", 17), width=25)
            wromantyzm.pack(side="top")
        if p.lower().replace(" ", "") == "pozytywizm":
            wpozytywizm = Label(text=p, bg="green", font=("Consolas", 17), width=25)
            wpozytywizm.pack(side="top")
            pkt += 1
        else:
            wpozytywizm = Label(text=p, bg="red", font=("Consolas", 17),width=25)
            wpozytywizm.pack(side="top")
        if m.lower().replace(" ", "") == "młodapolska":
            wmloda = Label(text=m, bg="green", font=("Consolas", 17), width=25)
            wmloda.pack(side="top")
            pkt += 1
        else:
            wmloda = Label(text=m, bg="red", font=("Consolas", 17), width=25)
            wmloda.pack(side="top")
        if x.lower().replace(" ", "") == "xx-leciemiędzywojenne" or x.lower().replace(" ", "") == "20-leciemiędzywojenne" or x.lower().replace(" ", "") == "dwudziestoleciemiędzywojenne":
            wxx = Label(text=x, bg="green", font=("Consolas", 17), width=25)
            wxx.pack(side="top")
            pkt += 1
        else:
            wxx = Label(text=x, bg="red", font=("Consolas", 17), width=25)
            wxx.pack(side="top")
        if w.lower().replace(" ", "") == "literaturawspółczesna":
            wwspolczesnosc = Label(text=w, bg="green", font=("Consolas", 17), width=25)
            wwspolczesnosc.pack(side="top")
            pkt += 1
        else:
            wwspolczesnosc = Label(text=w, bg="red", font=("Consolas", 17), width=25)
            wwspolczesnosc.pack(side="top")
        punktacja = Label(frame, text="Twój wynik: " + str(pkt) + "/10", font=("Consolas", 20), fg="blue")
        punktacja.pack(side="bottom")
        wstecz(frame, 3)

    def powrot(frame, tabelka): #===========================komenda do przycisku============================
        okno()
        back.destroy()
        if tabelka==0:
            autorzy_apk_menu.destroy()
            autorzy_apki.destroy()
        elif tabelka==1:
            motywacja_menu.destroy()
            motywacja_tresc.destroy()
        elif tabelka==2:
            instrukcja_menu.destroy()
            instrukcja_tresc.destroy()
        elif tabelka==3:
            epoki_menu.destroy()
            epoki_tresc.destroy()
            antyk.destroy()
            sredniowiecze.destroy()
            renesans.destroy()
            barok.destroy()
            oswiecenie.destroy()
            romantyzm.destroy()
            pozytywizm.destroy()
            mloda.destroy()
            XX.destroy()
            wspolczesnosc.destroy()
            submit.destroy()
            wantyk.destroy()
            wsredniowiecze.destroy()
            wrenesans.destroy()
            wbarok.destroy()
            woswiecenie.destroy()
            wromantyzm.destroy()
            wpozytywizm.destroy()
            wmloda.destroy()
            wxx.destroy()
            wwspolczesnosc.destroy()
            punktacja.destroy()
        elif tabelka==4:
            hasla_menu.destroy()
            latwo.destroy()
            trudno.destroy()
            srodek.destroy()
            wstep.destroy()
            epoki_haslo.destroy()
        elif tabelka==41:
            hasla_menu.destroy()
            latwo.destroy()
            trudno.destroy()
            srodek.destroy()
            wstep.destroy()
            epoki_haslo.destroy()
            A.destroy()
            B.destroy()
            C.destroy()
            dobra.destroy()
            zla.destroy()
        elif tabelka==42:
            hasla_menu.destroy()
            latwo.destroy()
            trudno.destroy()
            srodek.destroy()
            wstep.destroy()
            epoki_haslo.destroy()
            dialog.destroy()
            sprawdzam_epoki.destroy()
        elif tabelka==43:
            hasla_menu.destroy()
            latwo.destroy()
            trudno.destroy()
            srodek.destroy()
            wstep.destroy()
            epoki_haslo.destroy()
            dialog.destroy()
            sprawdzam_epoki.destroy()
            dobra.destroy()
        elif tabelka==44:
            hasla_menu.destroy()
            latwo.destroy()
            trudno.destroy()
            srodek.destroy()
            wstep.destroy()
            epoki_haslo.destroy()
            dialog.destroy()
            sprawdzam_epoki.destroy()
            zla.destroy()
        elif tabelka==5:
            przedstawiciele_menu.destroy()
        elif tabelka==6:
            obrazy_menu.destroy()
        else:
            autorzy_menu.destroy()

    def wstecz(frame, tabelka): #==========================PRZYCISK==========================
        global back
        back = Button(text="Wstecz", font=("Consolas", 17), width=40, command=lambda: powrot(frame, tabelka))
        back.pack(side="bottom")

    def distroj():
        autorzy_apk.destroy()
        witamy.destroy()
        motywacja.destroy()
        instrukcja.destroy()
        epoki.destroy()
        hasla.destroy()
        przedstawiciele.destroy()
        obrazy.destroy()
        autorzy_obrazow.destroy()
        wyjscie.destroy()

    def Autorzy_apk(frame):
        distroj()
        global autorzy_apk_menu
        autorzy_apk_menu = Label(frame, text="Autorzy:", font=("Consolas", 30))
        autorzy_apk_menu.pack(side="top")
        global autorzy_apki
        autorzy_apki = Label(frame, text="Jakub Błaszczyk - jakies tam pliki\n"
                                    "Filip Frankowski - jakies tam pliki, dokumentacje tez\n"
                                    "Maciej Kalemba - kodzik jak szef B)\n", font=("Consolas", 20))
        autorzy_apki.pack(side="top")
        wstecz(frame, 0)

    def Motywacja(frame):
        distroj()
        global motywacja_menu
        motywacja_menu = Label(frame, text="Dlaczego akurat taki pomysł?", font=("Consolas", 30))
        motywacja_menu.pack(side="top")
        global motywacja_tresc
        motywacja_tresc = Label(frame, text="Ta aplikacja powstała z myślą o przyszłości naszej, jak i przyszłych pokoleń\n"
                                            "przygotowujących się do matury z języka polskiego. Regularnie dokonywane badania\n"
                                            "bardzo często wskazują na to, że wykonywanie testów, quizów i tym podobnych nie tylko\n"
                                            "redukuje stres związany z ostatecznym podejściem do egzaminu, ale także stanowi\n"
                                            "przyjemną, wygodną i efektywną formę nauki - taką funkcję ma spełniać nasza aplikacja\n", font=("Consolas", 20))
        motywacja_tresc.pack(side="top")
        wstecz(frame, 1)

    def Instrukcja(frame):
        distroj()
        global instrukcja_menu
        instrukcja_menu = Label(frame, text="Instrukcja obsługi", font=("Consolas", 25))
        instrukcja_menu.pack(side="top")
        global instrukcja_tresc
        instrukcja_tresc = Label(frame, text="Aplikacja zawiera głównie zadania otwarte, w których\n"
                                     "należy wprowadzić z klawiatury, w odpowiedniej przestrzeni\n"
                                     "odpowiedź. Po wprowadzeniu odpowiedzi należy podsumować\n"
                                     "odpowiedzi poprzez kliknięcie odpowiedniego przycisku\n"
                                     "\n",
                                font=("Consolas", 20))
        instrukcja_tresc.pack(side="top")
        wstecz(frame, 2)

    def Epoki(frame):
        distroj()
        global epoki_menu
        epoki_menu = Label(frame, text="Epoki literackie", font=("Consolas", 25))
        epoki_menu.pack(side="top")
        global epoki_tresc
        epoki_tresc = Label(frame, text="Wymień epoki literackie poniżej\n"
                                        "w kolejności chronologicznej\n", font=("Consolas", 17))
        epoki_tresc.pack(side="top")

        global antyk
        antyk = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        antyk.pack(side="top")
        global sredniowiecze
        sredniowiecze = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        sredniowiecze.pack(side="top")
        global renesans
        renesans = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        renesans.pack(side="top")
        global barok
        barok = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        barok.pack(side="top")
        global oswiecenie
        oswiecenie = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        oswiecenie.pack(side="top")
        global romantyzm
        romantyzm = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        romantyzm.pack(side="top")
        global pozytywizm
        pozytywizm = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        pozytywizm.pack(side="top")
        global mloda
        mloda = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        mloda.pack(side="top")
        global XX
        XX = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        XX.pack(side="top")
        global wspolczesnosc
        wspolczesnosc = Entry(frame, width=25, justify=CENTER, font=("Consolas", 20))
        wspolczesnosc.pack(side="top")
        pkt = 0
        global submit
        submit = Button(frame,text="Sprawdź!", font=("Consolas", 20), width=20, command=lambda: epoki_check(frame, pkt))
        submit.pack(side="top")


        wstecz(frame, 3)

    def Hasla(frame):
        distroj()
        global hasla_menu
        hasla_menu = Label(frame, text="Hasła epok", font=("Consolas", 25), width=25)
        hasla_menu.pack(side="top")
        global srodek
        srodek = Label(frame, text="I", font=("Consolas", 40), fg="purple", bg="purple", width=25)
        srodek.pack()
        wstecz(frame, 4)
        global latwo
        latwo = Button(frame, text="Tryb łatwy", font=("Consolas", 17), command=lambda: latwizna(frame))
        latwo.pack(side="left")
        global trudno
        trudno = Button(frame, text="Tryb trudny", font=("Consolas", 17), command=lambda: trud(frame))
        trudno.pack(side="right")

    def Przedstawiciele(frame):
        distroj()
        global przedstawiciele_menu
        przedstawiciele_menu = Label(frame, text="Przedstawiciele epok", font=("Consolas", 25))
        przedstawiciele_menu.pack(side="top")
        wstecz(frame, 5)

    def Obrazy(frame):
        distroj()
        global obrazy_menu
        obrazy_menu = Label(frame, text="Tytuły obrazów", font=("Consolas", 25))
        obrazy_menu.pack(side="top")
        wstecz(frame, 6)



    def Autorzy(frame):
        distroj()
        global autorzy_menu
        autorzy_menu = Label(frame, text="Autorzy obrazów", font=("Consolas", 25))
        autorzy_menu.pack(side="top")
        wstecz(frame, 7)

    witamy = Label(frame, text="Witamy w aplikacji 'Zdaj z polskiego!'!", font=("Consolas", 25, "bold"))
    autorzy_apk = Button(frame, text="Autorzy", font=("Consolas", 17), width=40, command=lambda: Autorzy_apk(frame), activebackground="lightblue")
    motywacja = Button(frame, text="Motywacja", font=("Consolas", 17), width=40, command=lambda: Motywacja(frame),
                           activebackground="lightblue")
    instrukcja = Button(frame, text="Instrukcja obsługi", font=("Consolas", 17), width=40,
                            command=lambda: Instrukcja(frame), activebackground="lightblue")
    epoki = Button(frame, text="Epoki literackie", font=("Consolas", 17), width=40, command=lambda: Epoki(frame),
                       activebackground="lightblue")
    hasla = Button(frame, text="Hasła epok", font=("Consolas", 17), width=40, command=lambda: Hasla(frame),
                       activebackground="lightblue")
    przedstawiciele = Button(frame, text="Przedstawiciele epok", font=("Consolas", 17), width=40,
                                 command=lambda: Przedstawiciele(frame), activebackground="lightblue")
    obrazy = Button(frame, text="Rozpoznawanie obrazów", font=("Consolas", 17), width=40,
                        command=lambda: Obrazy(frame), activebackground="lightblue")
    autorzy_obrazow = Button(frame, text="Autorzy obrazów", font=("Consolas", 17), width=40,
                                 command=lambda: Autorzy(frame), activebackground="lightblue")
    wyjscie = Button(frame, text="Wyjdź", font=("Consolas", 20), width=40,
                             command=lambda: zdaj.quit(), activebackground="pink")

    witamy.pack(side="top")
    autorzy_apk.pack(side="top")
    motywacja.pack(side="top")
    instrukcja.pack(side="top")
    epoki.pack(side="top")
    hasla.pack(side="top")
    przedstawiciele.pack(side="top")
    obrazy.pack(side="top")
    autorzy_obrazow.pack(side="top")
    wyjscie.pack(side="bottom")

zdaj = Tk()
zdaj.title("Zdaj z polskiego!")
zdaj.geometry('1024x600')
frame = Frame(zdaj, bg="purple")
frame.pack()
okno()

zdaj.mainloop()