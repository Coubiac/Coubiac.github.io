title: "Fonctionnement du DHCP avec un Boot PXE"
author: Benoit
date: 2022-04-03 19:07:00 +0100
categories: [sysadmin, windows]
tags: [pxe,dhcp,wds]



## Fonctionnement normal

Dans un contexte de boot par le réseau PXE, le fonctionnement normal implique juste quelques échanges de packets DHCP.
Nous avons donc trois acteurs: Le serveur DHCP, Le serveur PXE, et le client.

Vous connaissez tous la séquence "DORA" (Discover, Offer, Request, Ack) d'un échange DHCP.

1. Le client diffuse (Broadcast) un packet DHCP demandant l'adresse des serveurs DHCP (serveurs qui peuvent distribuer des adresses IP). C'est le "D" de DORA, le DHCP DISCOVER. C'est ce qu'on appelle une découverte, le client cherche les serveurs. Comme il veut booter sur le réseau il va indiquer dans le même packet qu'il recherche des serveurs PXE (option DHCP 60). ![DHCP Discover avec PXE](/images/Boot-PXE-DHCP/DHCP-Discover.jpeg)
2. Le serveur DHCP répond par un Broadcast (diffusion) pour indiquer au client qu'il est un serveur d'adresses IP. Il lui indique aussi l'adresse IP qu'il compte lui attribuer si l'échange va jusqu'au bout. C'est le "O" de DORA, le DHCP OFFER. ![DHCP Offer sans PXE](/images/Boot-PXE-DHCP/DHCP-Offer1.jpeg)
3. Le serveur PXE répond lui aussi (eh oui...) pour indiquer qu'il est serveur de démarrage PXE. C'est encore un "O" de DORA, un autre DHCP OFFER ! ![DHCP Offer avec PXE](/images/Boot-PXE-DHCP/DHCP-Offer2.png)
4. Le client envoie au serveur DHCP un message demandant une adresse IP. Celle proposée par le serveur DHCP à l'étape 2. C'est le "R" de DORA, le DHCP REQUEST.[DHCP Request](/images/Boot-PXE-DHCP/DHCP-Request1.png)
5. Le Serveur DHCP répond par un DHCP ACK pour confirmer qu'il a bien attribuer l'adresse au client. C'est le "A" de DORA. [DHCP ACK](/images/Boot-PXE-DHCP/DHCP-ACK1.png)
6. Le client va envoyer une requete au serveur PXE pour lui demander le chemin du programme de boot (NBP, Network Boot Program). [proxyDHCP Request](/images/Boot-PXE-DHCP/DHCPProxy-Request1.png)
7. Le serveur PXE répond avec le chemin du NBP. [proxyDHCP ACK](/images/Boot-PXE-DHCP/DHCPProxy-ACK.png)


La suite bientôt...
