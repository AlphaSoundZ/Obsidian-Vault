---
title: Vektoren (old)
tags:
  - Mathe/Vektoren
---

# Vektoren (old)

Alles was man nur mit einer Zahl beschreiben kann nennt man Skalare. 

Beispiel T: Temperatur ist ein Skalar.

Größen, die man mit mehr als einer Zahl beschreiben muss (Geschwindigkeiten, Kräfte …), nennt man Vektoren!

## Betrag Eines Vektors

$$
|\vec{v}|= \sqrt{{x_1}^2, {y_1}^2, {z_1}^2}
$$

## Vektoren Addieren

$$
\vec{v_1} + \vec{v_2} = 
\begin{pmatrix} x_1 + x_2 \\ y_2 + y_2 \\ z_1 + z_2 \end{pmatrix} 

= x_1 + x_2 + y_1 + y_2 + z_1 + z_2
$$

## Skalarprodukt

$$
\vec{v_1} * \vec{v_2} = 
\begin{pmatrix} x_1 * x_2 \\ y_2 * y_2 \\ z_1 * z_2 \end{pmatrix} 

= x_1 * x_2 + y_1 * y_2 + z_1 * z_2
$$

## Normieren Eines Vektors (Vektor Auf Länge 1 kürzen)

$$
\vec{v_1}=|\vec{v_1}|* \vec{e}_{\vec{v_1}} = \frac{\vec{v_1}}{|\vec{v_1}|} = \vec{e}_{\vec{v_1}}
$$

# Geometrische Objekte Und Vektoren

## Punkt

Ein Punkt beschreibt, wo sich etwas befindet. Beschrieben wird er durch seine Koordinaten (so viele, wie die Dimension des umgebenden Raumes ist).

$$
P = (x|y|z)
$$

## Vektor

Translation im Raum, von einem Punkt zum anderen Punkt. Vektoren beschreiben eine Bewegung im Raum. Vektoren sind durch ihre Komponenten eindeutig festgelegt, allerdings gibt es unendliche viele Repräsentanten.

$$
\overrightarrow{OP} = 
\begin{pmatrix} P_x \\ P_y \end{pmatrix} 
$$

Der Punkt O ist der Ursprung des Koordinatensystems.

Vektoren sind durch ihre Komponenten eindeutig festgelegt, allerdings gibt es unendliche viele Repräsentanten. In der geometrischen Anschauung sind alle diese Repräsentanten parallel zueinander, gleich lang und zeigen in dieselbe Richtung! Ein Repräsentant dieser Klasse ist der Ortsvektor. Anfangspunkt für den Ortsvektor ist der Koordinatenursprung.

## Aus 2 Punkten → Ein Vektor

Welche Translation führt vom Punkt A zum Punkt E?

$$
Endpunkt - Anfangspunkt
$$

$$
\overrightarrow{AE} = 
\begin{pmatrix} E_x - A_x \\ E_y - A_y \\ E_z - A_z \end{pmatrix} 
$$

Ein geschlossener Polygonzug hat den Wert 0.

## Winkel Zwischen Zwei Vektoren

$$
\varphi = \arccos(
\frac
{\vec{v_1} * \vec{v_2}}
{| \vec{v_1} | * | \vec{v_2} |}
)
$$

## Orthogonaler Vektor

Ein Vektor ist einem anderen Vektor gegenüber orthogonal, wenn das Skalarprodukt 0 ist. Die beiden Vektoren stehen dann senkrecht aufeinander bzw. der Winkel ist 90° ist.

Die Konstruktion eines orthogonalen Einheitsvektors ist im R² eindeutig, im R³ nicht!

# Von Vektorgleichungen Zu LGS

$$
\vec{v_1}=\lambda \vec{v_2}
$$

Komponentenweise aufschreiben

$$
I: x_1= \lambda x_2
$$

$$
II: y_1= \lambda y_2
$$

$$
III: z_1= \lambda x_3
$$

Wenn Lambda bei allen Gleichungen gleich ist, sind die Vektoren kolliniear.

## Die Nächsten Geometrischen Objekte

### Beschreibung Von Geraden

Mittels zweier Punkte oder mittels eines Punktes und des Vektors in Richtung der Gerade. Dieser Vektor ist ein Richtungsvektor.

Ein Punkt auf einer Geraden ist ein Aufpunkt.

Eine Gerade ist eine unendlich große Menge von Punkten. Um jeden Punkt berechnen zu können, benötigen wir eine Gleichung.

$$
\vec{g} = \overrightarrow{OP} + \lambda \vec{r}
$$

### Lagebeziehungen Zwischen Geometrischen Objekten

Objekte können sich schneiden (oder identisch sein → bei einem Punkt) oder nicht.

### Liegt Ein Punkt Auf Gerade G?

- Wandle Punkte in Ortsvektoren um
- Setze Ortsvektor und Geradengleichung gleich
- Komponentenweise hinschreiben → LGS mit 2 oder 3 Gleichungen und 1 Variable
- eine Gleichung nach Lambda auflösen
- Prüfen ob, die anderen Gleichungen mit dem ermittelten Wert für Lambda erfüllt sind. Ja → Punkt auf g; Nein (eine nicht erfüllte Gleichung reicht!) → P liegt nicht auf g

Punkt zu Ortsvektor:

$$
\overrightarrow{OP} = g
$$

# Schneiden Von Geraden

Zwei Geraden können sich schneiden, parallel oder windschief sein. Windschiefe Geraden gibt es nur im R³.

### Rechnerische Prüfung

1. Schnittpunkt suchen
2. Wenn es keinen SP gibt, dann prüfe ob die Richtungsvektoren linear abhängig/parallel/kolinear sind. Wenn nein, dann sind die Geraden windschief (Wenn man für beide das gleiche Lambda finden kann)