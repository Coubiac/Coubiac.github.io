title: "Créer une infrastructure active directory sous Linux"
author: Benoit
date: 2021-11-06 15:55:33 +0100
categories: [it]
tags: [active directory, linux, samba]
math: true



# Introduction

Dans ce tutoriel nous allons mettre en place une infrastructure active directory complète sous linux à l'aide de SAMBA.

# Qu'est ce que samba ?

Samba est à l'origine une implémentation libre des protocoles SMB/CIFS sous linux. A l'origine, il servaut simplement à partager des fichiers d'un serveur linux à des clients Windows. Depuis la version 4, il permet de créer un controleur de domaine active directory et ainsi fournir les services d'authentification AD mais aussi des stratégies de groupes à des clients Windows. La documentation de [Samba][Samba] peut être trouvée [ici][Samba]

## Présentation du labo

Pour ce labo je vais utiliser 3 machines virtuelles:

- 1 VM Debian 11 nommée "SRV-AD-Linux": IP= 192.168.142.10
- 1 VM d'administration sous Windows 10: PC-ADMIN
- 1 VM Cliente: PC-CLient
- 1 routeur pour l'accès internet: IP= 192.168.142.250


## Installation du serveur AD

## Installation de la VM Linux

Pour cette VM, je vais utiliser Debian 11. Je vais commencer par l'installer de manière standard avec juste le minimum syndical. Je ne vais pas décrire l'installation d'une VM Debian basique car ce n'est pas l'objet du tuto mais voici les paquets choisis:

![Installation de debian](/images/samba/packets-debian.png)

C'est parti...

![Installation de debian](/images/samba/install-in-progress.png)

Et voila !

![Installation de debian](/images/samba/install-terminée.png)


## Configuration Pré-installation

### Désactivation d'IPV6.

N'ayant pas besoin d'IPV6 dans ce tuto, je vais le désactiver complètement en ajoutant ces lignes à la fin du fichier /etc/sysctl.conf

```bash
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

On applique les changements à l'aide de la commande "sysctl -p"

### Vérification du fichier /etc/hosts:


Il faut que le fichier /etc/hosts soit correctement configuré pour résoudre le nom de domaine enièrement qualifié (FQDN) et le nom d'hôte court vers l'adresse IP du controlleur de domaine.

![fichier /etc/hosts](/images/samba/etc-hosts.png)

### installation d'un serveur de temps (ntp):


Je ne vais pas m'attarder sur l'installation et la configuration d'un serveur de temps sous linux mais je vous met sur la piste:

```bash
apt update
apt install ntp
```

### installation de Samba:

```bash
apt-get install acl attr samba samba-dsdb-modules samba-vfs-modules winbind libpam-winbind libnss-winbind libpam-krb5 krb5-config krb5-user
```

L'installation commence:

![installation de samba](/images/samba/install-samba.png)

Le programme d'installation nous demande le nom du domaine par défault. Il s'agit du domaine AD. Pour moi, j'ai choisit coubiac.local


![domaine-kerberos](/images/samba/domaine-kerberos.png)

![serveur administratif kerberos](/images/samba/server-administratif-kerberos.png)

Voila, l'installation est terminée !

![installation de samba terminée](/images/samba/install-samba-terminee.png)

### Configuration de samba

Il faut commencer par arreter tous les process samba|smbd|nmbd|winbindd:

![installation de samba terminée](/images/samba/process1.png)

Ensuite il faut supprimer le fichier smb.conf créé par défault. Vous pouvez le trouver à l'aide cette commande:

```bash
smbd -b | grep "CONFIGFILE"
```

![fichier de conf samba](/images/samba/find-smbd.png)

On peut donc le renomer en smb.conf.old

```bash
mv /etc/samba/smb.conf /etc/samba/smb.conf.old
```

Il faut ensuite supprimer tous les fichiers de base de donnée *.tdb et *.ldb. 
Pour lister les dossiers qui contiennent ces bases de données:

```bash
smbd -b | egrep "LOCKDIR|STATEDIR|CACHEDIR|PRIVATE_DIR"
```

![fichier de conf samba](/images/samba/sambatld.png)

```bash
rm /run/samba/{*.tdb,*.ldb}
rm /var/lib/samba/{*.tdb,*.ldb}
rm /var/cache/samba/{*.tdb,*.ldb}
rm /var/lib/samba/private/{*.tdb,*.ldb}
```

Ensuite édite le fichier /etc/krb5.conf de cette manière:

![fichier de conf krb5](/images/samba/krb5conf.png)


Pour provisionner notre domaine, nous allons utiliser l'outil "samba-tool"

```bash
samba-tool domain provision --use-rfc2307 --interactive
```


![provisionning](/images/samba/provisionning.png)

On peut maintenant vérifier notre fichier /etc/samba/smb.conf

![smb.conf](/images/samba/smbconf.png)

Le script de config crée un fichier krb5.conf dans le dossier /var/lib/samba/private/krb5.conf.
Il faut supprimer ce fichier et le remplacer par celui se trouvant dans /etc/krb5.conf

```bash
rm -f /var/lib/samba/private/krb5.conf
ln -s /etc/krb5.conf /var/lib/samba/private/krb5.conf
```

Ensuite on peut configurer le démarrage des services:

```bash
systemctl unmask samba-ad-dc
systemctl enable samba-ad-dc
systemctl disable samba winbind nmbd smbd
systemctl mask samba winbind nmbd smbd
```

On vérifie:

```bash
systemctl list-unit-files |egrep 'samba|winbind|nmbd|smbd'
```

Il faut ensuite activer les ACL et attributs étendus sur la partition ou est installée SAMBA. On modifie donc notre fichier fstab:

```bash
vi /etc/fstab
```

et on ajoute les options 'acl' et 'user_xattr'

![smb.conf](/images/samba/fstab.png)

Ensuite on remonte la partition (ou on reboot):

```bash
mount -o remount /
```

Il faut maintenant corriger les permissions sur les partages sysvol et netlogon

```bash
samba-tool ntacl sysvolreset
```

Et voilà ! votre DC devrait être fonctionnel ! il ne reste plus qu'à le tester avec un windows 10.

## Ajout d'une machine au domaine

Si tout s'est bien passé, vous ne devriez pas avoir de soucis pour joindre le domaine:

![joindredomaine](/images/samba/joindredomaine.png)

![joindredomaine](/images/samba/joindredomaine2.png)

![joindredomaine](/images/samba/joindredomaine3.png)

Il faut ensuite installer les outils RSAT pour administrer l'active directory:

![rsat](/images/samba/rsat0.png)

![rsat](/images/samba/rsat1.png)

![rsat](/images/samba/rsat2.png)


J'ai ensuite, à l'aide des outils RSAT mis en place une GPO pour forcer le fond d'écran et un GPO pour mettre en place des administrateurs locaux et tout fonctionne !

![GPO](/images/samba/GPO_ADMIN_LOCAUX.png)

![GPO](/images/samba/GPO_FOND_ECRAN.png)



[Samba]: https://wiki.samba.org/index.php/

