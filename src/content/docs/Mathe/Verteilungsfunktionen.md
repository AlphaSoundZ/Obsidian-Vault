---
title: Verteilungsfunktionen
tags:
  - Mathe/Stochastik
---

## Verteilungsfunktionen

### Definition

Die (kumulierte) Verteilungsfunktion, beschreibt die Stammfunktion einer Glockenkurve bzw. Wahrscheinlichkeitsverteilung, welches auf der linken Seite offen ist. Anschaulich entspricht dabei der Wert der Verteilungsfunktion an der Stelle $x$ der Wahrscheinlichkeit, dass die zugehörige Zufallsvariable $X$ einen Wert kleiner oder gleich $x$ annimmt.

Die Wahrscheinlichkeit ist definiert durch:
$$F_p(x) = P((-\infty, x])$$
wobei $F_p$ eine reelle Zahl in dem Bereich $[0,1]$ ist.

### Funktion

$$
F_p(x) = \sum_{i=0}^{k}{{n\choose i} \cdot p^i \cdot (1-p)^{n-i}}
$$
$k$ ist das $x$ bzw. die rechte Grenze des Integrals.
$p$ ist die Wahrscheinlichkeit.

#### Beispiel

Ist beispielsweise die Verteilung der Schuhgrößen in Europa gegeben, so entspricht der Wert der entsprechenden Verteilungsfunktion bei 45 der Wahrscheinlichkeit, dass ein beliebiger Europäer die Schuhgröße 45 oder kleiner besitzt.

## Sigma-Regeln

Anwendbarkeit beim Hypothesentest

## Wahrscheinlichkeitsverteilung

Die Summe der Wahrscheinlichkeiten für alle möglichen Werte $k$ ([[Bernoulli und Binomial-Verteilung#Binomial-Verteilung|Binomialverteilung]]) bzw. das Integral mit offenen Grenzen ([[Hypothesentest und Fehlerarten#Normalverteilung|Normalverteilung]]) muss 1 ergeben.