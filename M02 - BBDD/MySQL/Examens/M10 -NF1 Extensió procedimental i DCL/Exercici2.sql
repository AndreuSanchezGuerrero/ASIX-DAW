ALTER TABLE partits_jugadors
    ADD COLUMN punts INT;
DELIMITER //
DROP PROCEDURE IF EXISTS spOmplePuntsJugadorPartit//
CREATE PROCEDURE spOmplePuntsJugadorPartit(IN pParitId INT,IN pJugadorId INT)
BEGIN
    DECLARE vPunts INT;
    DECLARE P1 INT;
    DECLARE P2 INT;
    DECLARE P3 INT;
    SELECT valor INTO P1 
        FROM estadistic_partit_jugador
        WHERE jugador_Id = pJugadorId AND partit_id = pParitId AND estadistic_id = 3;
    SELECT valor INTO P2
        FROM estadistic_partit_jugador
        WHERE jugador_Id = pJugadorId AND partit_id = pParitId AND estadistic_id = 5;
    SELECT valor INTO P3 
        FROM estadistic_partit_jugador
        WHERE jugador_Id = pJugadorId AND partit_id = pParitId AND estadistic_id = 7;
    SET vPunts = P1 + P2*2 + P3*3;
    UPDATE partits_jugadors SET punts = vPunts 
        WHERE jugador_Id = pJugadorId AND partit_id = pParitId;
END
//

CALL spOmplePuntsJugadorPartit(5,46);

SELECT * FROM estadistic_partit_jugador WHERE (estadistic_id = 3 OR estadistic_id = 5 OR estadistic_id = 7) AND partit_id = 5 AND jugador_id = 46;