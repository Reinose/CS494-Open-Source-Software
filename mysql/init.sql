USE cs494;

CREATE TABLE testset (
  id INT NOT NULL AUTO_INCREMENT,
  data INT,
  PRIMARY KEY(id)
);

delimiter $$
DROP FUNCTION IF EXISTS generate_data$$
CREATE PROCEDURE generate_data( count INT )
BEGIN
  DECLARE i INT DEFAULT 0;
  WHILE i < count DO
    INSERT INTO testset(data) VALUES (CAST(rand()*100000000 AS UNSIGNED));
    SET i = i+1;
  END WHILE;
END $$
delimiter ;
CALL generate_data(1000000);
