# Vektoren Und Vektorgleichungen

# Vektoren

## Notation

$$
\vec{v} = 
\begin{pmatrix}
v_x \\
v_y \\
v_z
\end{pmatrix} 
$$

Vektoren werden immer klein geschrieben und Punkte groß geschrieben.

## Betrag Eines Vektors (Länge)

$$
|\vec{v}|= \sqrt{{v_x}^2 + {v_y}^2 + {v_z}^2}
$$

## Skalare Multiplikation Und Division

Bei der Multiplikation eines Vektors mit einem Skalar verändert sich die Länge des Vektors. Die Division funktioniert gleich.

$$
\vec{v} \cdot a =
\begin{pmatrix}
v_x \cdot a \\
v_y \cdot a \\
v_z \cdot a
\end{pmatrix} 
$$

### Gegenvektor / Inverse

Bei der Multiplikation eines Vektors mit -1 erhält man den entgegengesetzten Vektor, auch inverser Vektor genannt.

$$ - \vec{v} $$

## Vektoren Addieren Und Subtrahieren

### Addition

Bei dem Addieren von Vektoren ensteht ein Vektor, der Anfangspunkt und Endpunkt verbindet.

![Untitled](Vektoren%20und%20Vektorgleichungen/Untitled.png)

$$
\vec{v} + \vec{w} =
\begin{pmatrix} v_x + w_x \\ v_y + w_y \\ v_z + w_z \end{pmatrix}
$$

### Subtraktion

Bei der Subtraktion von Vektoren erhält man den Vektor, der die Länge zwischen zwei Vektoren ausmacht. Der Vektor verbindet die beiden Vektoren, betrachtet als Ortsvektoren.

![bild.png](Vektoren%20und%20Vektorgleichungen/bild.png)

$$
\vec{u} - \vec{v} =
\begin{pmatrix} u_x - v_x \\ u_y - v_y \\ u_z - v_z \end{pmatrix}
$$

Das Gleiche funktioniert mit zwei Punkten aus, denen ein Vektor entsteht, der von Anfangspunkt zu Endpunkt zeigt. Dies nennt man Translation.

$$
Endpunkt - Anfangspunkt
$$

$$
\overrightarrow{AE} = 
\begin{pmatrix} E_x - A_x \\ E_y - A_y \\ E_z - A_z \end{pmatrix} 
$$

## Ortsvektor

Der Ortsvektor ist ein Vektor, der den Koordinatenursprung als Anfangspunkt hat. Er beschreibt die Position eines Punktes im Verhältnis zu diesem Ursprung.

$$
\vec{v} = \overrightarrow{OP} = 
\begin{pmatrix} P_x \\ P_y \\ P_z \end{pmatrix}
$$

Der Punkt O ist der Ursprung des Koordinatensystems und P ein beliebiger Punkt.

## Einheitsvektor

### Kanonischen Einheitsvektoren

Der Einheitsvektor ist ein Vektor, der eine Länge von 1 hat. Es gibt 3 Standard-Einheitsvektoren, die im 3-dimensionalen Raum für die Achsen verwendet werden. 

$$
\vec{e}_1 =
\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix}
\newline
\vec{e}_2 =
\begin{pmatrix}
0 \\
1 \\
0
\end{pmatrix}
\newline
\vec{e}_3 =
\begin{pmatrix}
0 \\
0 \\
1
\end{pmatrix}
$$

### Normieren

Beim Normieren eines Vektors, wird seine Länge auf 1 geändert, indem man ihn durch seinen Betrag teilt.

$$
\vec{e}_{\vec{v}} = \frac{\vec{v}}{|\vec{v}|}
$$

## Skalarprodukt

Das Skalarprodukt ist eine mathematische Methode zur Messung der Ähnlichkeit zwischen zwei Vektoren. Es wird als Innerer Winkel bezeichnet und berechnet sich wie folgt:

$$
\vec{v} \cdot \vec{w} = |\vec{v}| \cdot |\vec{w}| \cdot \cos(\theta)
$$

wobei $\theta$ der Winkel zwischen den beiden Vektoren ist.

### Winkel Berechnen

Um den inneren Winkel zu berechnen muss man die Formel auf $\theta$ umstellen.

$$
\theta = \arccos(\frac{\vec{v} \cdot \vec{w}}{|\vec{v}| \cdot |\vec{w}|})
$$

## Kreuzprodukt Zweier Vektoren (S. 74 Im Tafelwerk)

$$
\vec{v} \times \vec{w} =
\begin{pmatrix}v_y w_z - v_z w_y \\ v_z w_x - v_x w_z \\ v_x w_y - v_y w_x\end{pmatrix}
$$

Die Länge / der Betrag des Kreuzproduktes $\vec{a} \times \vec{b}$  ist gleich der Fläche des Parallelogramms, das von a und b aufgespannt wird.

## Orthogonaler Vektor

Zwei Vektoren die senkrecht zueinanderstehen sind orthogonale Vektoren. Das Skalarprodukt zweier orthogonaler Vektoren ist immer 0.

# Vektorgleichungen

## Gleichung

$$
\vec{g} = \overrightarrow{OP} + \lambda \vec{r}
$$

Die Gleichung besteht aus dem Aufpunkt und einem mit Lambda multiplizierten Richtungvektor.

## Punkte Auf Geraden

Ein Punkt auf einer Geraden ist ein Aufpunkt. Ein Punkt liegt dann auf einer Geraden, wenn das Lambda für alle Komonenten gleich ist.

Bei dem Berechnen von Lambda setzt man den Vektor $\vec{g}$ mit dem Ortsvektor $\overrightarrow{OP}$ des gegebenen Punktes gleich.

## Kollinieare Vektoren

Kollinear bedeutet, dass zwei Vektoren in derselben Richtung verlaufen. Die Länge der Vektoren müssen dabei nicht übereinstimmen.

## Aufpunkt

Ein Aufpunkt ist der Punkt auf einer Geraden, der als Ausgangspunkt für die Berechnungen verwendet wird.

## Richtungsvektor

Der Richtungsvektor einer Geraden gibt an, in welche Richtung sie verläuft und ist immer orthogonal zur Geraden. Ein Richtungsvektor kann berechnet werden, indem man zwei Punkte, Anfangspunkt und den Endpunkt, der Geraden betrachtet und die Ortsvektoren subtrahiert.

## Beziehungen Zwischen Geraden

### Parallel

Zwei Vektorgleichungen sind parallel, wenn der Richtungsvektor der einen gleich dem Richtungsvektor der anderen ist. Wenn die Richtungsvektoren verschieden sind, können die Geraden schneiden oder windschief sein.

- Richtungsvektoren normieren
- Wenn sie gleich oder invers sind, dann sind sie parallel

### Schnitt

Um herauszufinden, ob sich zwei Geraden schneiden, muss man die Parametergleichungen beider Geraden gleich setzen und nach Lambda aufgelöst werden. Wenn das Ergebnis eine eindeutige Lösung hat, schneiden sich die beiden Geraden. Wenn das Ergebnis keine eindeutige Lösung hat, sind die Geraden parallel.

Wir betrachten die folgenden zwei Vektorgleichungen:

$$ \vec{g_1} = \overrightarrow{OA} + \lambda \cdot \vec{r_1} $$

$$ \vec{g_2} = \overrightarrow{OB} + \mu \cdot \vec{r_2} $$

Gleichungen gleichsetzen und mihilfe des LGS (Gleichungen komponentenweise austellen) nach Lambda oder Mu auflösen:

$$
\overrightarrow{OA} + \lambda \cdot \vec{r_1}_x = \overrightarrow{OB} + \mu \cdot \vec{r_2}_x
\newline
\overrightarrow{OA} + \lambda \cdot \vec{r_1}_y = \overrightarrow{OB} + \mu \cdot \vec{r_2}_y
\newline
\overrightarrow{OA} + \lambda \cdot \vec{r_1}_z = \overrightarrow{OB} + \mu \cdot \vec{r_2}_z
$$

### Windschief

Geraden werden als windschief bezeichnet, wenn sie sich weder schneiden noch parallel zueinander sind. Windschiefe Geraden gibt es nur ab dem R³.

## Abstand Zwischen Punkt Und Gerade Ausrechnen

- Vektor bliden der Orthogonal ist (Skalarprodukt 0)
- Vektorgleichung bilden (mit Punkt und orthogonalen Vektor)
- Schnittpunkt finden
- Abstand zwischen Schnittpunkt und Punkt berechnen

## Ebenen

## Punkt Auf Ebene

3 Punkte (die nicht auf einer Gerade liegen) liegen immer in einer Ebene.

Ebenen:

$$
\overrightarrow{OA}+\lambda_1 \cdot \overrightarrow{AB} + \lambda_2 \cdot \overrightarrow{AC}
$$

gegeben: Ebenengleichung und Koordinaten eines Punktes

gesucht: Liegt der Punkt auf der Ebene?

Lösungsverfahren:

Prüfe, ob der Punkt zur Menge der Ebenenpunkte gehört. Setze den Ortsvektor gleich mit der Ebenengleichung → komponentenweise auflösen (LGS) → auflösen nach lambda 1 und lambda 2 → mit der nicht benutzten Gleichung überprüfen.

## Lage Zwischen Ebenen Und Geraden

### Möglichkeiten

- Gerade schneidet die Ebene → gemeinsamer Punkt
- Gerade liegt in der Ebene → alle (unendlich viele) Punkte
- Gerade schneidet die EBene nicht → 0 Punkte gemeinsam

### Der Normalenvektor

$$
\vec{N} = \vec{r_1} \times \vec{r_2}
$$

### Koordinatenform

$$
ax+by+cz=d
$$

$\begin{pmatrix}
a \\
b \\
c
\end{pmatrix}$= ist der Normalenvektor der Ebene, also orthogonal zur Ebene

In der Koordinatenform sind a, b und c die Komponenten des Normalenvektors.

# Typische Aufgaben Der Linearen Algebra Und Lösungsverfahren

1. Geradengleichung aus 2 Punkten aufstellen
    - Wandle Punkte in Ortsvektoren um
    - Bilde die Differenz der beiden Ortsvektoren → Richtungsvektor der Geraden
    - Wähle einen der beiden gegebenen Punkte als Aufpunkt
2. Prüfe, ob ein Punkt auf einer Geraden liegt
    - Wandle den Punkt in einen Ortsvektor um
    - Setze den Ortsvektor mit der Geradengleichung gleich
    - Schreibe die Geradengleichung dann Komonentenweise hin → LGS mit 1 Unbekannten
    - Löse eine der Gleichungen nach Lambda auf
    - Setze Lambda in alle anderen Gleichungen ein, und prüfe ob diese erfüllt sind. Wenn ja liegt der Punkt auf der Gerade.
3. Schneiden sich zwei Geraden? (g und h)
    - Setze die Vektor-Geradengleichungen gleich
    - Schreibe die Geradengleichung komponentenweise hin → LGS mit 2 Unbekannten (ggf. aus 3 Gleichungen)
    - Löse das Gleichungssystem (du erhältst Lambda 1 und Lambda 2)
    - Solte das LGS nicht lösbar sein (oder unendlich viele Lösungen besitzen, dann schneiden sich die Geraden nicht
    
    Nur im R³: Setze Lambda 1 / 2 in die noch nicht benutzte Gleichung ein. Nur wenn diese erfüllt ist, dann schneiden sich die Geraden
    
    Hinweis: in R³ gibt es die zusätzliche Lagebeziehung “windschief”.