SELECT NomClient, PrenomClient, NaissanceClient FROM CLIENT WHERE GenreClient = "Femme" AND NaissanceClient < '1970-01-01';

SELECT NomRegion, ContinentRegion FROM REGION WHERE ContinentRegion = "Europe" OR ContinentRegion = "Asie";

SELECT NomEspece, RusticiteEspece FROM ESPECE WHERE RusticiteEspece<-20 AND FloraisonEspece = 1;

SELECT NomCultivar, ReferenceCultivar FROM CULTIVAR WHERE NomCultivar LIKE "%Silver%" OR NomCultivar LIKE '%Gold%'

SElECT IdCommande, DateCommande, ClientCommande FROM COMMANDE WHERE DateCommande BETWEEN "2022-01-01" AND "2024-01-01" ORDER BY DateCommande ASC

SELECT FamilleGenre, COUNT(FamilleGenre) FROM GENRE GROUP BY FamilleGenre ORDER BY COUNT(FamilleGenre) DESC;

SELECT EspeceCultivar, COUNT(EspeceCultivar) FROM CULTIVAR GROUP BY EspeceCultivar HAVING COUNT(EspeceCultivar)>1

SELECT Commande, SUM(Quantite), MIN(Quantite), MAX(Quantite) FROM DETAIL\_COMMANDE GROUP BY Commande	

SELECT IdCommande, DateCommande, NomClient, PrenomClient FROM COMMANDE c JOIN CLIENT l ON c.IdCommande = l.IdClient;

SELECT l.NomClient,

&#x20;      c.DateCommande,

&#x20;      cu.NomCultivar,

&#x20;      dc.Quantite

FROM COMMANDE c

JOIN CLIENT l

&#x20;   ON c.ClientCommande = l.IdClient

JOIN DETAIL\_COMMANDE dc

&#x20;   ON c.IdCommande = dc.Commande

JOIN CULTIVAR cu

&#x20;   ON dc.Cultivar = cu.IdCultivar;

SELECT NomFamille, NomGenre, NomEspece, RusticiteEspece FROM ESPECE e JOIN GENRE g ON e.GenreEspece = g.IdGenre JOIN FAMILLE f ON g.FamilleGenre = f.IdFamille



SELECT NomClient, PrenomClient, IdCommande, DateCommande FROM CLIENT c LEFT OUTER JOIN COMMANDE co ON c.IdClient = co.ClientCommande;

SELECT NomEspece, NomRegion, ContinentRegion FROM ESPECE e LEFT OUTER JOIN REGION r ON e.RegionEspece=r.IdRegion;

SELECT NomFamille, COUNT(NomEspece) FROM FAMILLE f LEFT OUTER JOIN GENRE g ON f.IdFamille=g.FamilleGenre LEFT OUTER JOIN ESPECE e ON g.IdGenre=e.GenreEspece GROUP BY f.NomFamille;

-----------------------------------------------------------------------------------------------------------------------------------------------

SELECT Nom FROM Enfants WHERE Allergies=1;

SELECT COUNT(Numero) FROM Enfants GROUP BY Medecin HAVING Medecin="Geriton";

SELECT Nom, Prenom, Groupe FROM Affectations a RIGHT OUTER JOIN Enfants e ON a.Enfant = e.Numero ORDER BY Groupe

SELECT Groupe, Type FROM Sorties ORDER BY Groupe;

SELECT Groupe, COUNT(Enfant) FROM Affectations GROUP BY Groupe

SELECT Groupe, COUNT(Enfant) FROM Affectations GROUP BY Groupe HAVING COUNT(Enfant)>1

SELECT COUNT(Numero) FROM Enfants WHERE Medecin IS NULL

