-- settings.sql
CREATE DATABASE nostaldja;
CREATE USER nostaldjauser
WITH PASSWORD 'nostaldja';
GRANT ALL PRIVILEGES ON DATABASE nostaldja TO nostaldjauser;