# Une accélération des évolutions technologiques

Au cours de ces dernières années le paysage informatiques a bien évolué et il va continuer à évoluer au fur et à mesure des années prochaines.

## Le DevOps : une appropriation des outils des ops par les dev

Il y a 6 ans, L'Insee a engagé une démarche DevOps avec pour objectif de briser le mur entre les équipes de développement et d’exploitation.
Cette transformation s’est traduite par le fait de donner aux développeurs les droits et responsabilités auparavant réservés aux équipes ops, afin de gagner en autonomie, en rapidité de livraison et en collaboration.

!!! warning "Impacts"

    * Autonomie : :arrow_up:
    * Sécurité : :arrow_down:
    * Charge équipe dev : :arrow_up:

Cette première phase était surtout basée sur des devs utilisant les mêmes outils que les Ops, sans interface/outil simplifiant l'utilisation. Certains dev ont appris à maitriser les outils et les notions d'Ops

## Le DPII en mode produit : les devs adopte le language des ops

Il y a 2 ans, l’Insee a poursuivi sa transformation avec un découpage en mode produit. La production a été réorganisée en équipes de service, chacune responsable d’un domaine fonctionnel. Le but étant de mieux répondre aux besoins des développeurs. Concrètement, cela s’est traduit par la création de N équipes et la suppression des RIAPs.

Les RIAPs jouaient auparavant un rôle de proxy entre les développeurs et les équipes ops.

Désormais, c’est au développeur d’identifier et de contacter directement l’équipe service concernée, de suivre l'avancement des taches demandés, ou de réaliser soit même les opérations avec les outils mis à disposition par les équipes.

!!!warning "Impacts"

    * Charge équipe dev : :arrow_up:

Cette mise en place des équipes services à également permis la mise en place d'outil orienté dev. On ne met plus des outils d'Ops au dev mais des surcouches aux outils des Ops pour les devs.

## IAC / Kubernetes : Modernisation des outils des Ops

Depuis maintenant 5 ans l'Insee modernise les outils qu'elle propose aux développeurs: 

- Les développeurs ont maintenant la possibilités d'avoir des environnements "Kubernetes". Par rapport au monde VM (historique à l'Insee), ces nouveaux environnements offrent un fonctionnement différents (nouvelles fonctionnalitées) à l'état de l'art mais également plus de responsabilités aux développeurs. L'intéraction avec cet environnements ce fait par le biais de nouvelles pratiques et de nouveaux outils qu'il faut que l'utilisateur s'approprie.
- Les outils historiques du monde VM se modernise pour s'orienter vers des standards pour le déploiement. Prochainement la production informatique abandonnera l'outil puppet ainsi qu'un certains nombre d'outil maison (Rainette - création de plateforme / oiseau - création applishare - fenêtre de service / ...) pour des outils moderne à base de OpenTofu (Terraform) et Ansible.

L'ensemble de ces changements de technologies n'est pas neutre pour les développeurs qui doivent s'adapter et s'approprier les nouveaux outils.

!!!warning "Impacts"

    * Charge cognitive : :arrow_up:

## Cloud: Déployer une application n'importe où

Avec la doctrine « Cloud au centre » : le Cloud devient dorénavant le mode d’hébergement et de production par défaut des services numériques de l’État, pour tout nouveau produit numérique et pour les produits connaissant une évolution substantielle;

L'objectif de la DSI est désormais de s'orienter vers une trajectoire cloud-First. Les technologies Kubernetes sont une des solutions cloud possible mais ce n'est pas la seule. Afin d'établir la stratégie cloud de l'insee un questionnaire concernant la maturité cloud est actuellement diffusé au SNDI afin d'établir une roadmap. Les résultats sont prévus pour Juin 2026

!!!info

    La charge de l'infra va encore augmenter coté développeur et peut être même s'accelérer au cours des prochaines années.

## Des enjeux de sécurité croissant

L'accélération de l'exploitation des failles de sécurités, notamment grâce aux outils propulsés par l'IA, fait que les developpeurs passent de plus en plus de temps sur le MCO / MCS de leurs applications. Les outils tel que **analyzer** mettent en évidence les failles de sécurités (CVE) qu'embarquent les applications et encourage les développeurs à les corriger et à relivrer leur applications régulièrement.

# Bilan

!!!info

    **Constat** :
    
    - **Des changements liés à l'infrastructure de plus en plus régulier** : Les développeurs connaissent depuis 10 ans en moyenne une migration lié à l'infra tout les 2 ans.
      - 2017 => migration à Telis et mise en place de puppet3
      - 2020 => migration Osny / Auzeville
      - 2022 => migration puppet6 / applishareV3 / Debian11
      - 2024 => passage Debian12
      - 2026 => migration applishareV4
      - 2026/2027 => passage ansible
      - 2027 => arrêt VMWare passage proxmox
    - **Une orientation DevOps** : La modernisation des outils apporte aux développeurs de plus en plus d'autonomie. Cette autonomie demande une appropriation des nouveaux outils par les devs et un accompagnement des Ops.
    - **Multiplication des interlocuteurs / canaux de communication**: Avec la disparition des RIAPs ce sont désormais les développeurs qui jouent le role d'orchestrateur.
    - **Des enjeux de sécurités / disponibilités croissant**

    **Conséquences**:

    - Une charge coginitive des développeurs qui augmente, il ne se concentre plus uniquement sur du dev applicatif mais sur de la correction de vulnérabilité, du déploiement, de la résolution d'incident,... 
    - Un temps de développement de feature réduit