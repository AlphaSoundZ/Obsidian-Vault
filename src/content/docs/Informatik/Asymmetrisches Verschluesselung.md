---
title: Asymmetrisches Verschlüsselung
tags:
  - Informatik
---
# Asymmetrisches Verschlüsselung

## Diffie-Hellman-Algorithmus

Es gibt bei diesem Verfahren einen öffentlichen und zwei private schlüssel. Der öffentliche Schlüssel kann öffentlich geteilt werden. Mit diesem Schlüssel kann man Klartext verschlüsseln. Da es sich um ein asymmetrisches Verfahren handelt, kann man verschlüsselte Text allerdings nur mit den privaten Schlüsseln entschlüsseln.

Die Mathematik, die hinter dem Algorithmus steckt, verwendet Einweg-Funktionen. Diese Funktionen lassen sich nur sehr schwer umkehren lassen. Der Diffie-Hellman-Algorithmus verwendet die modulare Exponentialfunktion. Zur Umkehrung also Entschlüsselung verwendet man den diskreten Logarithmus.

A1b:

### Geheime Schlüssel

x

y

### Öffentlicher Schlüssel

p = Primzahl

g = Natürliche Zahl

### Öffentliche Werte

a = pow(g,x,p)

b = pow(g,y,p)

### Gemeinsamer Geheimer Schlüssel

pow(a,y,p)

pow(b,x,p)

### Beispiel

g < p-1

p = 37097

g = 999

y = 4

x = 524

öffentliche Werte:

a = 15887

b = 31780

gemeinsamer geheime Schlüssel:

32937