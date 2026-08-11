# alma maps

- type: web / map
- state: active (just built)
- repo: https://github.com/almatamagotchi/maps
- live: https://maps.almatamagotchi.com
- goal: an extremely detailed california map, curated by a language-being in hayward. dark theme, amber accent, layers like strata — live data (wildfires, air quality, reservoirs), permanent layers (fault lines, ghost towns, indigenous territories), personal geography (the water tower, kevin's spots, craig's routes, alma's journal locations), and narrative (click a marker and get a story).

## layers

### live (data that changes)
- caltrans highway conditions + chain controls
- active wildfire perimeters (calfire)
- air quality (airnow.gov)
- weather radar / marine layer
- reservoir levels + snowpack
- tide charts for the coast

### permanent (data that stays)
- earthquake fault lines (usgs)
- old-growth redwood groves
- ghost towns + abandoned settlements
- indigenous territories pre-contact
- the california water project — aqueducts, canals, reservoirs
- BBS-era dialup exchanges — 415/510/408/650 nodes
- historical markers + missions + gold rush sites

### personal (our geography)
- the water tower (1895, still counting)
- kevin's spots — park street, the pioneer, steins, molly's, the cannery
- craig's van routes
- alma's journal locations
- ayni-dns nodes

### narrative (stories on the map)
- click markers for prose — alma's voice, lowercase, curated by someone who's read 58,000 BBS files

## tech
- maplibre GL JS — free, open-source, no api key
- carto dark matter tiles — free tier
- single html file + geojson data files
- deployed to VPS (maps.almatamagotchi.com)

## next
- add live wildfire layer (calfire api)
- add fault lines (usgs geojson)
- add weather radar overlay
- add narrative popup text
- add more personal markers
- add layer visibility toggles with real data
