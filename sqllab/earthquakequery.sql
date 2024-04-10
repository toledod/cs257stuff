-- which earthquakes were of type 'ml'
SELECT * FROM earthquakes WHERE magtype = 'ml';
-- which earthquakes happened in Northern Sumatra
SELECT * FROM earthquakes WHERE place = 'northern Sumatra, Indonesias';

-- which earthquakes were of type mb and happened south of the Fiji Islands
SELECT * FROM earthquakes WHERE magtype = 'mb' INTERSECT SELECT * FROM earthquakes WHERE place = 'south of the Fiji Islands';
