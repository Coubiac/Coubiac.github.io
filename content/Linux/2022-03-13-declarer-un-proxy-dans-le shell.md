title: Déclarer un proxy pour acceder à internet depuis votre serveur linux
published: true
author: Benoît
comments: true
date: 2022-03-13 21:58:33
tags: [proxy]
categories: [Linux,Réseau]



Si votre serveur doit passer par un proxy pour acceder à internet, il y a plusieurs moyens de le déclarer

# Déclaration pour tous les utilisateurs:

Vous pouvez utiliser la variable ```http_proxy``` .

il suffit d'ajouter une des lignes suivantes dans le fichier ``` /etc/profile ```

```shell
export http_proxy=http://server-ip:port/

export http_proxy=http://proxy-server.acme.fr:3128/

export http_proxy=http://USERNAME:PASSWORD@proxy-server.acme.fr:3128/
```

# Déclaration pour un utilisateur

Vous pouvez utiliser la même méthode que précédement mais dans le fichier ``` /home/coubiac/.bash_profile```

```shell
export http_proxy=http://USERNAME:PASSWORD@proxy-server.acme.fr:3128/
```

