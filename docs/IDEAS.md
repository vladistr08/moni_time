# IDEI

## Functionalitatea Aplicatiei

-- Aplicatia va functiona pe sisteme de tip desktop

-- Colecteaza la 10 secunde informatii **procese active**

-- Aplicatia filtreaza din procesele active, doar procesele in care user-ul e activ (Chrome, Jocuri, etc.) nu si cele de tip sistem

-- Adauga informatiile colectate in baza de date locala (cache local)

--Cand exista o conexiune stabila la internet, aplicatia transmite datele la baza de date de pe server

-- User-ul poate vizualiza statistici(Online sau pe Mobil)

## Web Back/Front end

-- Python cu [Flask](https://www.fullstackpython.com/flask.html) pentru backend

-- [Vue.js](https://vuejs.org/) si [bulma](https://bulma.io/) pentru CSS 

-- Pentru Legatura Front-Back folosim [alpine.js](https://github.com/alpinejs/alpine)

-- Pentru Baza de Date [SQLite](https://www.sqlite.org/index.html)

## Urmarire procese

-- Vom folosi [psutil](https://github.com/giampaolo/psutil).
Tutorialul pe [windows](https://www.thepythoncode.com/article/make-process-monitor-python).


## GUI / App Frontend (Mac, Linux, Windows)

-- Vom folosi [kivy py](https://kivy.org/#home)

## Pentru Mobile(IOS, Android)

-- Vom folosi [Flutter](https://flutter.dev/?gclid=Cj0KCQjwzZj2BRDVARIsABs3l9L6oSGb1LCJxLa6TBHBQOKRzkj0rG2AG1hvUV0gKDzhKIGkYaLud5MaAlk6EALw_wcB&gclsrc=aw.ds) 