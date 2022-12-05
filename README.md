# CapsaDragosGabrielA6_Python_Project
 Watchdog C:16
Realizați un script care să monitorizeze starea unui proces și să îl repornească dacă execuția
acestuia s-a oprit. Se poate configura intervalul de timp la care să fie verificată starea
procesului, cât și locația fișierului de log. Se va scrie în log orice modificare a stării procesului
(dead / alive).
Input:
watchdog.py <nume_executabil> <timp_in_secunde> <nume_log>
watchdog.py bitcoin_miner.exe 60 watchdog.log
Output:
log-ul

Programul realizat de mine are cateva features in plus: 
-poti apela cu -s sau -f pentru a selecta modul de formatare (descris in cod)
-poti adauga o durata de secunde care sa reprezinte durata de rulare a watchdog-ului.
-se poate apela si fara aceste argumente astfel incat sa obtinem rezultatul dat ca exemplu
