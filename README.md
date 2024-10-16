# Wochenaufgabe-5

### 1. `def ist_palindrom(s):`
- Hier wird eine Funktion namens `ist_palindrom` definiert, die einen Parameter `s` annimmt,
- der den eingegebenen Text repräsentiert.

### 2. `s = s.lower().replace(" ", "")`
- Diese Zeile bearbeitet den Text `s` folgendermaßen:
    - **`s.lower()`**: Wandelt alle Zeichen des Strings in Kleinbuchstaben um, um sicherzustellen, 
    - dass die Groß- und Kleinschreibung ignoriert wird. Zum Beispiel wird aus "Otto" => "otto".
    - **`.replace(" ", "")`**: Entfernt alle Leerzeichen im String, um sicherzustellen, 
    - dass auch Sätze wie "Ein Neger mit Gazelle zagt im Regen nie" als Palindrom erkannt werden. 
    - Es ersetzt jedes Vorkommen von `" "` (ein Leerzeichen) durch nichts (`""`), also wird es einfach gelöscht.

  Nach dieser Zeile ist der String standardisiert: Es gibt nur noch Kleinbuchstaben und keine Leerzeichen mehr.

### 3.  `return s == s[::-1]`
- **`s[::-1]`**: Das ist eine spezielle Python-Syntax, die den String `s` umkehrt. Der Operator `[::-1]` sorgt dafür, 
- dass der String von hinten nach vorne gelesen wird.
- Die Zeile `return s == s[::-1]` vergleicht, ob der umgekehrte String `s[::-1]` gleich dem Original-String `s` ist. 
- Wenn beide gleich sind, dann handelt es sich um ein Palindrom, und die Funktion gibt `True` zurück. 
- Wenn sie unterschiedlich sind, gibt die Funktion `False` zurück.

Beispiel:

Angenommen, der Benutzer gibt das Wort `"Otto"` ein:
1. Der Text wird durch `lower()` zu `"otto"`.
2. Leerzeichen gibt es keine, also bleibt der String unverändert.
3. Jetzt wird `"otto"` mit `"otto"[::-1]` verglichen, was ebenfalls `"otto"` ergibt.
4. Da beide gleich sind, wird `True` zurückgegeben, und der Benutzer bekommt die Meldung, dass es ein Palindrom ist.
### Funktion benutzt in Aufgabe 12: Palindrom-Erkennung




Die Funktion **wort.isdigit()** 
prüft, ob ein Wort im Satz eine Zahl ist.
Falls zahlen im Satz vorhanden sind,
wird eine fehlermeldung ausgegeben und der Benutzer wird aufgefordert,
einen neuen satz einzugeben.
#### **(Funktion benutzt in Aufgabe 13: Wortzähler)**