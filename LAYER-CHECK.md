# maps — layer regression check (post-glyphs fix)

2026-08-16 · the auto-run · RFC-0513

systematic verification of every toggleable layer after the aug 15
triple-bug fix (missing glyphs endpoint, malformed radar tiles,
trigger-happy error handler). everything checked end to end.

## the checks

### external sources — all live

| layer | endpoint | result |
|---|---|---|
| satellite base | ESRI World Imagery | 200 |
| glyphs (labels) | demotiles.maplibre.org font pbf | 200 |
| radar manifest | api.rainviewer.com weather-maps.json | 200 |
| radar tile | {host}{path}/256/5/5/12/6/1_1.png — built from the live `path` field | 200, 2,234-byte PNG |
| wind | api.open-meteo.com gfs current | 200 |
| counties | codeforamerica california-counties.geojson | 200 |

the radar tile URL construction is confirmed correct against the live
manifest — the aug 15 fix (`{host}{path}/256/{z}/{x}/{y}/6/1_1.png`) holds.

### local data — all serving, all valid

| layer | file | result |
|---|---|---|
| city borders (461) | ca-cities.geojson | 200 · geojson featurecollection |
| fault lines | faults.json | 200 · geojson + labels |
| wildfires | wildfires.json | 200 · featurecollection + updated + count |
| air quality | aqi.json | 200 · 32 station objects |
| caltrain | /paloalto/caltrain.json (symlink) | 200 · updated + stations |
| traffic | /paloalto/traffic.json (symlink) | 200 · events + meta |

### style validation — no errors remain

- `glyphs` declared in the style object (the aug 10→15 killer, present)
- 12 sources declared (`base-tiles` in style.sources, 11 via addSource
  before their layers) — zero layer references to missing sources
- 6 text-field layers all covered by the glyphs declaration
- deployed page md5 == workspace copy (`077ada2a`), glyphs + base-tiles
  confirmed in the served html

## notes

- the VPS 403s the python default user-agent on data files (bot
  filtering); browsers with normal UAs get 200. no action needed, but
  any future server-side fetcher must send a browser UA.
- layers all pass the regression check. the map loads.
