title: "Débuter et survivre dans VIM"
author: Benoit
date: 2022-03-10 19:32:33 +0100
categories: [sysadmin, linux]
tags: [vim]
math: true
image: /images/security.jpg

# SORTIR de Vim

```text
:q	: sort
:q!	: force à sortir et abandonner les modifications
:w	: enregistre
:wq	: enregistre et sort
```

# Se déplacer

```text
Flèches de direction: se déplacer

h	: déplacer le curseur vers la gauche
j	: déplacer le curseur vers le bas
k	: déplacer le curseur vers le haut
l	: déplacer le curseur vers la droite

gg	: aller au début du fichier
G	: aller à la fin du fichier

w	: aller au début du mot suivant (espace et ponctuation comme séparateur)
W	: aller au début du mot suivant (espace comme séparateur)

^	: aller au début de la ligne (premier caractère)
$	: aller à la fin de la ligne

:42	: se déplace à la ligne 42
42G	: se déplace à la ligne 42

/unMot	: se déplace au mot "unMot" vers le bas
	 n	: mot suivant vers le bas
	 N	: mot suivant vers le haut
?unMot	: se déplace au mot "unMot" vers le haut
	 n	: mot suivant vers le bas
	 N	: mot suivant vers le haut
```

# Modification

## Modification avec basculement en mode insertion

```text
a	: Insertion après le curseur
i	: Insertion avant le curseur

A	: Insertion à la fin de la ligne
I	: Insertion au début de la ligne

o	: Insertion en ajoutant une ligne vers le bas
O	: Insertion en ajoutant une ligne vers le haut
```
## Copier - Coller

```text
dd	: Coupe la ligne (peut servir à supprimer la ligne)
yy	: Copie la ligne
d	: Coupe le mot
y	: Copie le mot
p	: colle
```

## Rechercher / Remplacer

```text
/unMot	: se déplace au mot "unMot" vers le bas
	 n	: mot suivant vers le bas
	 N	: mot suivant vers le haut

?unMot	: se déplace au mot "unMot" vers le haut
	 n	: mot suivant vers le bas
	 N	: mot suivant vers le haut

:%s/old/new/g	: Recherche le mot "old" et le remplace 
				  par le mot "new" dans tout le fichier
```

## Commenter et décommenter un bloc de texte
Commenter un bloc de code


![Commenter un bloc de texte](https://i.stack.imgur.com/lu6aU.gif)


Décommenter un bloc de code

![Décommenter un bloc de texte](https://i.stack.imgur.com/2Y7eH.gif)


Source: <https://stackoverflow.com/a/1676690>