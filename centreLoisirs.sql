-- 
-- Structure de la table `Adultes`
-- 

CREATE TABLE `Adultes` (
  `Numero` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Nom` varchar(12) NOT NULL,
  `Prenom` varchar(12) NOT NULL,
  `Adresse` varchar(48) NOT NULL,
  `TelephoneFixe` varchar(10)  DEFAULT NULL,
  `TelephonePortable` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Numero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Adultes`
-- 

INSERT INTO `Adultes` ( `Numero` , `Nom` , `Prenom` , `Adresse` , `TelephoneFixe` , `TelephonePortable` ) VALUES
(1 , 'Dupont', 'Hervé', '3 rue Pieplu', '0203040506', '0605040302'),
(2 , 'Dupont', 'Maryse', '3 rue Pieplu', '0203040506', '0605040302'),
(3 , 'Radigues', 'Maurice', '1 rue du Pré-aux-vaches', '0223485759', NULL);

-- --------------------------------------------------------

-- 
-- Structure de la table `Medecins`
-- 

CREATE TABLE `Medecins` (
  `Medecin` char(12) NOT NULL,
  `Ville` varchar(12) NOT NULL,
  `TelephoneFixe` varchar(10) DEFAULT NULL,
  `TelephonePortable` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Medecin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Medecins`
-- 

INSERT INTO `Medecins` (`Medecin`, `Ville`, `TelephoneFixe`, `TelephonePortable`) VALUES 
('Geriton', 'Auray', NULL, '0617161514'),
('Petro', 'Vannes', '0299555555', '0618151312'),
('Radigues', 'Saint Muflin', '0203040506', NULL),
('Di Pietro', 'Auray', '0265248793', NULL);

-- --------------------------------------------------------

-- 
-- Structure de la table `Animateurs`
-- 

CREATE TABLE `Animateurs` (
  `Identifiant` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Nom` varchar(12) NOT NULL,
  `Prenom` varchar(12) NOT NULL,
  `PetiteEnfance` tinyint(1) NOT NULL,
  `Bafa` tinyint(1) NOT NULL,
  `Secouriste` tinyint(1) NOT NULL,
  `Naissance` date NOT NULL,
  `Sexe` enum('G','F') NOT NULL,
  `Adresse` varchar(48) NOT NULL,
  `TelephoneFixe` varchar(10) DEFAULT NULL,
  `TelephonePortable` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Identifiant`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Animateurs`
-- 

INSERT INTO `Animateurs` ( `Identifiant` , `Nom` , `Prenom` , `PetiteEnfance` , `Bafa` , `Secouriste` , `Naissance` , `Sexe` , `Adresse` , `TelephoneFixe` , `TelephonePortable` ) VALUES
('1', 'Robert', 'Pierre', '0', '1', '1', '1975-01-21', 'G', 'rue du clos de ville', '0251282420', '0619161314'),
('2', 'Sarde', 'Camille', '1', '1', '1', '1978-07-12', 'F', 'rue de la Monnaie', '0187942420', '0619113714'),
('3', 'Legrand', 'Edmond', '1', '0', '0', '1982-02-17', 'G', 'rue de la Gare', '0251456420', '0619166497'),
('4', 'Lapierre', 'Albert', '0', '1', '1', '1973-01-14', 'G', 'rue Dumont', '0265943720', '0664287131'),
('5', 'Thibaut', 'Aimé', '1', '1', '1', '1977-03-03', 'G', 'rue du General Leclerc', '0258754420', '0613561314'),
('6', 'Bidault', 'Anne', '0', '1', '1', '1979-05-28', 'F', 'rue du Nile', '0245712020', '0667461314'),
('7', 'Robert', 'Jessica', '1', '0', '1', '1974-03-21', 'F', 'rue du Commandant mouchotte', '0251514420', '0614962314');

-- --------------------------------------------------------

-- 
-- Structure de la table `Transports`
-- 

CREATE TABLE `Transports` (
  `Nom` char(12) NOT NULL,
  `Coordonnées` varchar(48) NOT NULL,
  PRIMARY KEY (`Nom`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Transports`
-- 

INSERT INTO `Transports` (`Nom`, `Coordonnées`) VALUES 
('ExpressCars', 'Route de Lorient, Rennes, au feu à gauche - 06 1'),
('OuestTrans', 'Pacé, contact : Monsieur Raoul, 06 14 18 17 19');

-- --------------------------------------------------------

-- 
-- Structure de la table `Periodes`
-- 

CREATE TABLE `Periodes` (
  `Vacances` varchar(12) NOT NULL,
  `Transport` char(12) NULL,
  `IDdirecteur` int(11) unsigned NOT NULL,
  PRIMARY KEY (`Vacances`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Periodes`
-- 

INSERT INTO `Periodes` (`Vacances`, `Transport`, `IDdirecteur`) VALUES 
('Aout', 'ExpressCars', 1),
('Fevrier', 'ExpressCars', 1),
('Juillet', 'OuestTrans', 3),
('Noel', 'OuestTrans', 1),
('Paques', 'OuestTrans', 2),
('Toussaint', 'OuestTrans', 2);

-- Contraintes pour la table `Periodes`
-- 
ALTER TABLE `Periodes`
  ADD FOREIGN KEY (`IDdirecteur`) REFERENCES `Animateurs` (`Identifiant`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `Periodes`
  ADD FOREIGN KEY (`Transport`) REFERENCES `Transports` (`Nom`) ON DELETE SET NULL ON UPDATE CASCADE;

-- --------------------------------------------------------

-- 
-- Structure de la table `Groupes`
-- 

CREATE TABLE `Groupes` (
  `Identifiant` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Periode` varchar(12) NOT NULL,
  `Age` enum('petits','moyens','grands','6-7ans','8-10ans') NOT NULL,
  `IDresponsable` int(11) unsigned NOT NULL,
  `IDadjoint` int(11) unsigned NOT NULL,
  PRIMARY KEY (`Identifiant`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Groupes`
-- 

INSERT INTO `Groupes` (`Identifiant`, `Periode`, `Age`, `IDresponsable`, `IDadjoint`) VALUES 
(1, 'Toussaint', 'petits', 3, 4),
(2, 'Toussaint', 'moyens', 2, 5),
(3, 'Noel', 'moyens', 2, 5),
(4, 'Fevrier', 'grands', 2, 5),
(7, 'Toussaint', '6-7ans', 1, 6),
(8, 'Noel', 'petits', 3, 4),
(10, 'Noel', '8-10ans', 1, 6);

-- Contraintes pour la table `Groupes`
-- 
ALTER TABLE `Groupes`
  ADD FOREIGN KEY (`IDresponsable`) REFERENCES `Animateurs` (`Identifiant`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `Groupes`
  ADD FOREIGN KEY (`IDadjoint`) REFERENCES `Animateurs` (`Identifiant`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `Groupes`
  ADD FOREIGN KEY (`Periode`) REFERENCES `Periodes` (`Vacances`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- --------------------------------------------------------

-- 
-- Structure de la table `Enfants`
-- 

CREATE TABLE `Enfants` (
  `Numero` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Prenom` varchar(12) NOT NULL,
  `Nom` varchar(12) NOT NULL,
  `Sexe` enum('G','F') NOT NULL,
  `Naissance` date NOT NULL,
  `Ecole` varchar(12) NOT NULL,
  `Medecin` char(12) NULL,
  `Vaccin` tinyint(1) NOT NULL,
  `Allergies` tinyint(1) NOT NULL,
  PRIMARY KEY (`Numero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Enfants`
-- 

INSERT INTO `Enfants` (`Numero`, `Prenom`, `Nom`, `Sexe`, `Naissance`, `Ecole`, `Medecin`, `Vaccin`, `Allergies`) VALUES 
(1, 'Marie', 'Dupont', 'F', '2001-01-08', 'les glayeuls', 'Geriton', 1, 0),
(2, 'Elodie', 'Dupont', 'F', '2005-07-28', 'les glayeuls', 'Geriton', 1, 0),
(3, 'Claude', 'Radigues', 'F', '2001-04-07', 'la Fontaine', 'Radigues', 1, 1),
(4, 'François', 'Radigues', 'G', '2005-02-21', 'Zola', 'Petro', 1, 1);

-- Contraintes pour la table `Enfants`
-- 
ALTER TABLE `Enfants`
  ADD FOREIGN KEY (`Medecin`) REFERENCES `Medecins` (`Medecin`) ON DELETE SET NULL ON UPDATE CASCADE;

-- --------------------------------------------------------

-- 
-- Structure de la table `Affectations`
-- 

CREATE TABLE `Affectations` (
  `Enfant` int(11) unsigned NOT NULL ,
  `Groupe` int(11) unsigned NOT NULL ,
  PRIMARY KEY (`Enfant`, `Groupe`)
) ENGINE=innodb DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Affectations`
-- 

INSERT INTO `Affectations` (`Enfant`, `Groupe`) VALUES 
(2, 2),
(4, 2),
(2, 3),
(1, 10),
(3, 10);

-- Contraintes pour la table `Affectations`
-- 
ALTER TABLE `Affectations`
  ADD FOREIGN KEY (`Enfant`) REFERENCES `Enfants` (`Numero`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Affectations`
  ADD FOREIGN KEY (`Groupe`) REFERENCES `Groupes` (`Identifiant`) ON DELETE CASCADE ON UPDATE CASCADE;

-- --------------------------------------------------------

-- 
-- Structure de la table `Contacts`
-- 

CREATE TABLE `Contacts` (
  `NumeroEnfant` int(11) unsigned NOT NULL,
  `NumeroAdulte` int(11) unsigned NOT NULL,
  `Role` enum('pere','mere','frere','soeur','grand-pere','grand-mere','garde') NOT NULL,
  PRIMARY KEY (`NumeroEnfant`,`NumeroAdulte`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Contacts`
-- 

INSERT INTO `Contacts` (`NumeroEnfant`, `NumeroAdulte`, `Role`) VALUES 
(1, 1, 'pere'),
(1, 2, 'mere'),
(2, 1, 'pere'),
(2, 2, 'mere'),
(3, 2, 'garde'),
(3, 3, 'pere'),
(4, 1, 'garde'),
(4, 3, 'pere');


-- Contraintes pour la table `Contacts`
-- 
ALTER TABLE `Contacts`
  ADD FOREIGN KEY (`NumeroAdulte`) REFERENCES `Adultes` (`Numero`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Contacts`
  ADD FOREIGN KEY (`NumeroEnfant`) REFERENCES `Enfants` (`Numero`) ON DELETE CASCADE ON UPDATE CASCADE;

-- --------------------------------------------------------

-- 
-- Structure de la table `Animations`
-- 

CREATE TABLE `Animations` (
  `Type` char(12) NOT NULL,
  `Description` text NOT NULL,
  `Lieu` text NOT NULL,
  `BesoinCar` tinyint(1) NOT NULL,
  PRIMARY KEY (`Type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Animations`
-- 

INSERT INTO `Animations` (`Type`, `Description`, `Lieu`, `BesoinCar`) VALUES 
('Cuisine', 'Apprendre à faire un gateau au chocolat : 4 oeufs, 250g farine, 150g gras, 200g chocolat, 250g sucre + 1 sachet sucre vanillé,  penser à graisser les formes en silicone. ', 'Cusine centre aéré', 0),
('Foot', 'Entrainement si moins de 12, sinon deux équipes sur petite largeur', 'terrains la touche', 1),
('Lecture', 'Rayons 1 et 3 adaptés au petit, allée 2 pour les grands, prévoir allumer le chauffage à l''avance + coussins', 'Biblio centre aéré', 0),
('Nature1', 'Sortie découverte flore, forêt de Rennes', 'Saint Sulpice la forêt', 1),
('Nature2', 'Sortie découverte faune', 'maison de la chasse', 1);

-- --------------------------------------------------------

-- 
-- Structure de la table `Sorties`
-- 

CREATE TABLE `Sorties` (
  `Date` date NOT NULL,
  `Periode` enum('matin','aprem') NOT NULL,
  `IDresponsable` int(11) unsigned NOT NULL,
  `Groupe` int(11) unsigned NOT NULL,
  `Type` char(12) NOT NULL,
  PRIMARY KEY (`Date`,`Periode`,`Groupe`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 
-- Contenu de la table `Sorties`
-- 

INSERT INTO `Sorties` ( `Date` , `Periode` , `IDresponsable` , `Groupe` , `Type` ) VALUES
('2009-12-28', 'matin', '2', '3', 'Cuisine'),
('2009-12-28', 'aprem', '5', '3', 'Lecture'),
('2009-12-28', 'matin', '6', '10', 'Cuisine'),
('2009-12-28', 'aprem', '1', '10', 'Foot'),
('2009-12-29', 'matin', '7', '3', 'Nature1'),
('2009-12-29', 'aprem', '7', '3', 'Nature2'),
('2009-12-29', 'matin', '7', '10', 'Nature1'),
('2009-12-29', 'aprem', '7', '10', 'Nature2');

-- Contraintes pour la table `Sorties`
-- 
ALTER TABLE `Sorties`
  ADD FOREIGN KEY (`IDresponsable`) REFERENCES `Animateurs` (`Identifiant`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `Sorties`
  ADD FOREIGN KEY (`Groupe`) REFERENCES `Groupes` (`Identifiant`) ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE `Sorties`
  ADD FOREIGN KEY (`Type`) REFERENCES `Animations` (`Type`) ON DELETE RESTRICT ON UPDATE CASCADE;
