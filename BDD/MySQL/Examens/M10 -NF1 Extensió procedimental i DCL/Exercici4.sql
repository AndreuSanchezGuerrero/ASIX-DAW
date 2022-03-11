DELIMITER //

DROP TRIGGER IF EXISTS NJugadorsAny//
CREATE TRIGGER NJugadorsAny AFTER UPDATE ON contractes
	FOR EACH ROW
BEGIN
	UPDATE equips_anys
		SET numero_jugadors = (SELECT COUNT(jugador_id)
                                FROM contractes
                                WHERE equip_any_id = OLD.equip_any_id
                                GROUP BY equip_any_id);
END
//