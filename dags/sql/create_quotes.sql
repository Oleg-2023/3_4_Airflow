CREATE TABLE IF NOT EXISTS quotes
(
	rate_id bigserial primary key,
	get_date          timestamp,
	base_rate         varchar(5),
	target_rate       varchar(5),
	rate              float
)