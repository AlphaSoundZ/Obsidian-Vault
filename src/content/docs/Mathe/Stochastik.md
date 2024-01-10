---
title: Stochastik
tags:
  - Mathe/Stochastik
---

## Stochastik

## Laplace-Versuch

ein Zufallsexperiment mit genau zwei möglichen Ausgängen. Zum Beispiel ein Münzwurf oder die Wahrscheinlichkeit, dass man eine bestimmte Zahl würfelt, oder nicht.

## Bernoulli-Kette

viele hintereinander ausgeführte gleiche Laplace-Experimente

## Permutation

[[Permutation]]

## Binomialkoeffizient

$\binom{n}{k} = \frac{n!}{(n-k)! * n!}$

## Arithmetische Mittel

$$
y \cdot i = \frac{\sum_{i=1}^{N}y_i}{N} = : <y>
$$

## Varianz

$$
v = \sum_{i=1}^{K} (x_i - \mu )^2 \cdot p_i
$$
$\mu$ ist $f(x_i)$
p ist die relative Häufigkeit

## Normalverteilung: bei großen N ist der Median gleich dem Mittelwert

Für große N und viele Versuche (Ebenen im Baumdiagramm) geht die (diskrete) Normalverteilung in eine (stetige) Verteilungsfunktion über!
$$
f(x | \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
$$