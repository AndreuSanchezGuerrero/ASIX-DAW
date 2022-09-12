DELIMITER //
DROP FUNCTION IF EXISTS sp_JugadorFaltesComeses//
CREATE FUNCTION sp_JugadorFaltesComeses(pParitId INT,pJugadorId INT) RETURNS TINYINT
    NOT DETERMINISTIC READS SQL DATA
BEGIN
    DECLARE vRetorn TINYINT DEFAULT NULL;
    SELECT valor INTO vRetorn
        FROM estadistic_partit_jugador
        WHERE jugador_id = pJugadorId AND partit_id = pParitId AND estadistic_id = 8;
    RETURN vRetorn;
END
//
SELECT sp_JugadorFaltesComeses(9,63)//