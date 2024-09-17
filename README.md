# ISO19157-3 Data Quality Measures Register

This repository contains:

* automation tooling to ingest a draft register from content included as a submodule
* a original demo pipeline configuration to semantically uplift a Google Spreadsheet containing ISO19157-3 properties.

The content is (currently) pushed to a staging/development node of the OGC Rainbow as a set of related vocabularies linked together by identifiers.

[Search for iso19157 on HOSTED node of OGC RAINBOW (Development)](http://defs-dev.opengis.net/vocprez-hosted/vocab/?filter=iso19157)

Top level [Quality Measures Register](https://defs-dev.opengis.net/vocprez-hosted/object?uri=https%3A//standards.isotc211.org/19157/-3/1/dqc/content/qualityMeasure)

Note that when live, the URIs for each measure will redirect to these or equivalent machine-readable resources using HTTP Content-Negotiation.

# ISO 19157-3 register ingest

A set of sheets are ingested from CSV sources into a set of RDF graphs that combine to form a complete register complete with multivalued complex properties for examples, formulae etc.

## Files

### content files
Source XLS and extracted CSV and derived forms are in the directory [ISO19157-3/](./ISO19157-3/)

### configuration
- `.ogc/`: OGC tools configuration
  - `config.yml`: General configuration (download URLs and target files) 
  - `catalog.ttl`: Domain Configuration catalog with uplift definition for `*.csv.json` files.
- `csv2python.yml`: Uplift definition that simply turns CSV into JSON
- `properties-uplift.yml`: Uplift definition that takes the JSONified CSV and converts it to JSON-LD and Turtle
- `.github/workflows/`: GitHub workflows
  - `uplift-and-join.yaml`: Converts CSV to Linked Data with cross references between elemennts
  - `pus-to-rainbow.yaml`: Uploads RDF files to configured node of the OGC RAINBOW (currently HOSTED-DEV)
  - 

## See also

- [OGC Naming Authority tools (ogc-na)](https://opengeospatial.github.io/ogc-na-tools/)
  - [Domain configuration and uplift context examples](https://opengeospatial.github.io/ogc-na-tools/examples/)
  - [ingest_json reference](https://opengeospatial.github.io/ogc-na-tools/reference/ogc/na/ingest_json/)
  - [CSV input filter configuration](https://opengeospatial.github.io/ogc-na-tools/reference/ogc/na/input_filters/csv/)
