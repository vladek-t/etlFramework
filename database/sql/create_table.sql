create table if not exists loader_name (
id_loader_name integer primary key autoincrement
, loader_name string unique not null
, tech_changed_dttm timestamp not null
);