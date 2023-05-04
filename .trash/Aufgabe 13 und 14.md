# Aufgabe 13 und 14

Date: April 21, 2023
Date Created: April 19, 2023 12:10 PM
Status: Done 🙌
Subject: Mathe
URL: https://moodle.ght-hh.de/mod/assign/view.php?id=12948

# Aufgabe 13

## a)

Richtungsvektoren der Geraden ablesen / berechnen und schauen bei welchem $x_3 < 0$ ist. Die anderen beiden Komponenten verwenden um die Himmelsrichtung zu berechnen: Aus $x_1$ und $x_2$ einen Vektor im $r^2$ bilden und den Winkel zum Vektor Richtung Norden mithilfe dem Skalarprodukts berechnen. Es muss ein Vektor im $r^2$ verwendet werden, da Oben keine Himmelsrichtung ist.

Der Vektor Richtung Norden:

$$
\vec{v_1} =
\begin{pmatrix}
0 \\
1
\end{pmatrix}
$$

Richtungsvektor von g:

$$
\vec{v_2} = \overrightarrow{AB} = \begin{pmatrix}
10 \\
10 \\
0
\end{pmatrix}
$$

Richtungsvektor von h:

$$
\vec{v_3} = \overrightarrow{CD} = \begin{pmatrix}
6 \\
-6 \\
-1
\end{pmatrix}
$$

Die Komponente der Höhe ($x_3$) ist beim Richtungsvektor der Gerade h negativ. Dadurch sinkt das Flugzeug während des Flugs. Bei der anderen Gerade ist die Komponente 0 (keine Höhenveränderung).

Winkel zwischen $\vec{v_2}$ und $\vec{v_1}$:

Da die Beträge von beiden Komponenten von $\vec{v_3}$ gleich sind, zeigt der Vektor genau zwischen zwei Himmelsrichungen. $x_1$ zeigt Richtung Osten (Wert positiv) und $x_2$ zeigt Richtung Norden (Wert positiv). Somit fliegt das Flugzeug in Richtung Nordosten.

Winkel zwischen $\vec{v_3}$ und $\vec{v_1}$:

Da die Beträge von beiden Komponenten von $\vec{v_3}$ gleich sind, zeigt der Vektor genau zwischen zwei Himmelsrichungen. $x_1$ zeigt Richtung Osten (Wert positiv) und $x_2$ zeigt Richtung Süden (Wert negativ). Somit fliegt das Flugzeug in Richtung Südosten.

## b)

Geradengleichung gleichsetzen:

$$
\begin{pmatrix} x_1 \\ x_2 \\ 7.5 \end{pmatrix} = \begin{pmatrix} 13 \\ 33 \\ 10 \end{pmatrix} + t \cdot \begin{pmatrix} 6 \\ -6 \\ -1 \end{pmatrix}
$$

$t$ mit einer Komponente ausrechnen, wo nur eine Unbekannte ist ($x_3$):

$$
t = \frac{7.5[km]-10}{-1} = 2.5[min]
$$

Mit $t$ und der Geradengleichung den Punkt ausrechnen:

$$
\begin{pmatrix} 28 \\ 18 \\ 7.5 \end{pmatrix} = \begin{pmatrix} 13 \\ 33 \\ 10 \end{pmatrix} + 2.5 \cdot \begin{pmatrix} 6 \\ -6 \\ -1 \end{pmatrix}
$$

## c)

Geradengleichung gleichsetzen:

$$
\begin{pmatrix} x_1 \\ x_2 \\ 0 \end{pmatrix} = \begin{pmatrix} 13 \\ 33 \\ 10 \end{pmatrix} + t \cdot \begin{pmatrix} 6 \\ -6 \\ -1 \end{pmatrix}
$$

$t$ mit einer Komponente ausrechnen, wo nur eine Unbekannte ist ($x_3$):

$$
t = \frac{0[km]-10}{-1} = 10[min]
$$

Mit $t$ und der Geradengleichung den Punkt ausrechnen:

$$
\begin{pmatrix} 73 \\ -27 \\ 0 \end{pmatrix} = \begin{pmatrix} 13 \\ 33 \\ 10 \end{pmatrix} + 10 \cdot \begin{pmatrix} 6 \\ -6 \\ -1 \end{pmatrix}
$$

## d)

Das eine Flugzeug ändert sich nicht in der Höhe und befindet sich durchgängig auf einer Höhe von 8 Kilometern (g). D.h. man muss in diesem Fall die Punkt von Geradengleichung h ausrechnen, wo $x_3 = 8$ ist.

Geradengleichung gleichsetzen:

$$
\begin{pmatrix} x_1 \\ x_2 \\ 8 \end{pmatrix} = \begin{pmatrix} 13 \\ 33 \\ 10 \end{pmatrix} + t \cdot \begin{pmatrix} 6 \\ -6 \\ -1 \end{pmatrix}
$$

$t$ mit einer Komponente ausrechnen, wo nur eine Unbekannte ist ($x_3$):

$$
t = \frac{8[km]-10}{-1} = 2[min]
$$

Mit $t$ und der Geradengleichung den Punkt ausrechnen:

$$
\begin{pmatrix} 25 \\ 21 \\ 8 \end{pmatrix} = \begin{pmatrix} 13 \\ 33 \\ 10 \end{pmatrix} + 2 \cdot \begin{pmatrix} 6 \\ -6 \\ -1 \end{pmatrix}
$$

Überprüfen, ob der Punkt auf der anderen Flugbahn liegt (von g).

$$
\begin{pmatrix} 25 \\ 21 \\ 8 \end{pmatrix} = \begin{pmatrix} -5 \\ -9 \\ 8 \end{pmatrix} + t \cdot \begin{pmatrix} 10 \\ 10 \\ 0 \end{pmatrix}
$$

gemeinsames $t$ finden:

$$
t = \frac{21[km]-(-9)}{10} = 3[min]
$$

Es gibt ein gemeinsames $t$, was sich daran erkennen lässt, wenn man t komponentenweise einsetzt.

## e)

In Aufgabe d bereits berechnet, ist die Zeit, wo beide Flugzeuge sich beim Schnittpunkt befinden bei dem ersten Flugzeug 3 Minuten und bei dem anderen Flugzeug 2 Minuten. Diese Zeitdifferenz wird ausreichen, sodass die Flugzeuge nicht kollidieren.

## f)

Da die Geschwindigkeit in der gegebenen Zeitspanne konstant ist. Kann man auch die Zeitspanne von einer Minute verwenden, was genau dem Betrag des Richtungsvektors entspricht.

$$
|\vec{v_2}| = 14,14[km/min]
$$

$$
|\vec{v_3}| = 8,54[km/min]
$$

## g)

![Untitled](Aufgabe%2013%20und%2014/Untitled.png)

## h)

orthogonalen Vektor zum Richtungsvektor der Geradengleichung g:

$$
\begin{pmatrix} 10 \\ 10 \end{pmatrix} \cdot \vec{v} = 10*\vec{v_{x_1}} + 10*\vec{v_{x_2}} = 0
$$

$$
\vec{v} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

Resultierende Geradengleichung, die orthogenal zur anderen Geraden ist, und durch FS geht.

$$
\vec{x} = \begin{pmatrix} 100 \\ 100 \end{pmatrix} + \lambda \cdot \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

$$
\vec{x} = \begin{pmatrix} -5 \\ -9 \end{pmatrix} + t \cdot \begin{pmatrix} 10 \\ 10 \end{pmatrix}
$$

LGS bilden:

$$
100 + \lambda = 10t - 5
\newline
100 - \lambda = 10t - 9

$$

$$
2 \lambda = 4
\newline
\lambda = 2
$$

$$
\begin{pmatrix} 102 \\ 98\end{pmatrix} = \begin{pmatrix} 100 \\ 100 \end{pmatrix} + 2 \cdot \begin{pmatrix} 1 \\ -1 \end{pmatrix}
$$

Die höhe des Flugzeuges ist durchgängig 8 km über dem Boden, somit ist $x_3 = 8$:

$$
\begin{pmatrix} 102 \\ 98 \\ 8 \end{pmatrix}
$$

$$
|\begin{pmatrix} 102 \\ 98 \\ 8 \end{pmatrix} - \begin{pmatrix} 100 \\ 100 \\ 0 \end{pmatrix}| = \sqrt{72}
$$

# Aufgabe 14

## b)

$$
\vec{x} = \begin{pmatrix} 1200 \\ 0 \\ -540 \end{pmatrix}
 + \lambda \cdot 
\begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}
$$

## c)

Winkel in der horizontalen Ebene:

$$
\vec{v_1} = \begin{pmatrix} -8 \\ -13 \end{pmatrix}
$$

$$
\vec{v_2} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}
$$

$$
103.39° = \cos^{-1} \left( \frac{\vec{v_1} \cdot \vec{v_2}}{|\vec{v_1}| \cdot |\vec{v_2}|} \right)
$$

Steigung:

Hypotenuse berechnen:

$$
17.72 = |\begin{pmatrix} -8 \\ -13 \\ 9 \end{pmatrix}|
$$

$$
30.5° = sin^{-1}\left( \frac{9}{17.72} \right)
$$

Punkt bestimmen, an dem das U-Boot an der Wasseroberfläche ankommt:

$$
\begin{pmatrix} x_1 \\ x_2 \\ 0 \end{pmatrix} = \begin{pmatrix} 400 \\ 800 \\ -540 \end{pmatrix}
 + \lambda \cdot 
\begin{pmatrix} -8 \\ -13 \\ 9 \end{pmatrix}
$$

Lambda ausrechnen:

$$
\lambda = \frac{540}{9} = 60
$$

$$
P(-80|20|0)
$$