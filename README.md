# Metody i Zadania Rozpoznawania Wzorców - Projekt zaliczeniowy

## **Opis**

Projekt opracowany na potrzebę realizacji przedmiotu Metody i Zadania Rozpoznawania Wzorców realizowanego podczas semestru VII w Wydziale Cybernetyki WAT na specjalności Sieci Teleinformatyczne.

---

## **Instalacja**

### **Wymagania**

- **Python** - wersja **3.10.8**
- **biblioteki** - zawarte w pliku *requirements.txt*

### **Proces instalacji**

1. Instalacja interpretera języka Python za pomocą CMD:

   - Uruchom CMD jako Administrator,

   - Pobierz i zainstaluj Chocolatey za pomocą podanej komendy:

        ``` code
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.      exe"-NoProfile -InputFormat None -ExecutionPolicy Bypass    -Command"iex ((New-Object System.Net.WebClient).DownloadStrin     ('https://chocolatey.org/install.ps1'))" && SET      "PATH=%PATH%%ALLUSERSPROFILE%\chocolatey\bin"
        ```

   - Zainstaluj interpreter języka Python za pomocą Chocolatey:

        ``` code
        choco install -y python3
        ```

    - Możesz sprawdzić, czy interpreter został poprawnie zainstalowany:

        ``` code
        python -V
        ```

1. Instalacja wymaganych bilbiotek:

``` code
python -m pip install -r requirements.txt
```

3. Uruchomienie programu:

``` code
python main.py
```

---

## **Problem**

...
