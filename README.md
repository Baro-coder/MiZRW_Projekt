# Metody i Zadania Rozpoznawania Wzorców - Projekt zaliczeniowy

## **Opis**

Projekt opracowany na potrzebę realizacji przedmiotu Metody i Zadania Rozpoznawania Wzorców realizowanego podczas semestru VII w Wydziale Cybernetyki WAT na specjalności Sieci Teleinformatyczne.

---

## **Instalacja**

## Wymagania

- **Python** - wersja >= **3.10.8**
- **biblioteki** - zawarte w pliku *requirements.txt*

## Proces instalacji

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

2. Pobranie repozytorium:

    ``` code
    git clone https://github.com/Baro-coder/MiZRW_Projekt
    ```

3. Instalacja wymaganych bilbiotek:

    ``` code
    python -m pip install -r requirements.txt
    ```

4. Uruchomienie programu:

    ``` code
    python accent_recognition.py
    ```

---

## **Zadanie projektowe**

## Założenie

Założeniem projektu jest opracowanie sieci neuronowej zdolnej do rozpoznawania angielskiego akcentu. Po rozwinięciu dana sieć będzie mogła rozponawać głos konkretnej osoby, co może posłużyć jako kolejny etap autoryzacji dla dowolnego systemu informatycznego.

---

## Zestaw danych

Dane do analizy pozyskałem ze strony:

***<https://www.kaggle.com/datasets/rtatman/speech-accent-archive/versions/1?resource=download>***

Zestaw zawiera ponad 2000 nagrań różnych osób wymawiających tę samą frazę w języku angielskim, ale o innym akcencie. Nazwa każdego pliku z nagraniem stanowi jednocześnie oczekiwany wynik predykcji sieci, tj.:

> {akcent}{numer}.{rozszerzenie}

Na przykład:

> russian12.mp3

Co oznacza, że plik zawiera nagranie frazy z akcentem rosyjskim, jest to 12 z kolei plik z danym akcentem oraz jest to plik typu *mp3*.

---

## Dane wejściowe

Każde nagranie jest wczytywane przez program, standaryzowane do jednego formatu, np. częstotliwość próbkowania, a następnie tworzony jest spektrogram Mela.

Spektrogram jest zapisywany jako obraz oraz podlega przetworzeniu wstępnemu, tj. formatowany do postaci czarno-białej.

Tak przygotowane dane stanowią dane wejściowe do sieci neuronowej.

---

## Dane wyjsciowe

Jak wspomniano powyżej w sekcji ***Zestaw danych*** nazwa każdego pliku zawiera jednocześnie oczekiwany wynik predykcji sieci. Dla łatwiejszego przetwarzania przestrzeń nazw jest alfabetycznie indeksowana, tzn. pierwszy alfabetycznie akcent po zmapowaniu to *0*, kolejny to *1* ...
