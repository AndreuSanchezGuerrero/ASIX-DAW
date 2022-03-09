DELIMITER //
CREATE TRIGGER trgEliminarVolumFacturacio AFTER DELETE ON factures
	FOR EACH ROW
BEGIN
	UPDATE comercials
		SET volum_fact = volum_fact - OLD.import
	WHERE comercial_id = OLD.comercial_id;
END//

DELIMITER //
CREATE TRIGGER trgUpdateVolumFacturacio AFTER UPDATE ON factures
	FOR EACH ROW
BEGIN
	UPDATE comercials
		SET volum_fact = volum_fact - OLD.import + NEW.import
	WHERE comercial_id = OLD.comercial_id;
END//
