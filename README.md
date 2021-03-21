# US Energy Analysis

> Gather and Analyze Data on energy production and consumption in the United States exploring the options of alternatives.

## Folder Structure

```bash
├── US-Energy-Analysis
├── data
│ ├── external
│ ├── interim
│ ├── processed
│ └── raw
├── notebooks
└── resources
```

The other key structural issue is that the input and output files are stored in different directories:

- external - files and api calls that do not live in our project.
- interim - Used if there is a multi-step manipulation. This is a scratch location and not always needed but helpful to have in place so directories do not get cluttered or as a temp location form troubleshooting issues.
- processed - In many cases, I read in multiple files, clean them up and save them to a new location in a binary format. This streamlined format makes it easier to read in larger files later in the processing pipeline.
- raw - Contains the unedited csv and Excel files used as the source for analysis.

## Data Links

### Energy

- [EIA OPEN DATA](https://www.eia.gov/opendata/register.php)
- [TOTAL ENERGY](https://www.eia.gov/totalenergy/data/browser/)
- [Form EIA-923 detailed data with previous form data (EIA-906/920)](https://www.eia.gov/electricity/data/eia923/)
- [ELECTRICITY](https://www.eia.gov/electricity/data.php)

### Energy Production

### Energy Demand

- [Section 19. Energy and Utilities](https://www.census.gov/library/publications/2011/compendia/statab/131ed/energy-utilities.html)

### Energy Pricing

- [Electric Sales, Revenue, and Average Price](https://www.eia.gov/electricity/sales_revenue_price/)

### People and Energy

- [2020 Quarterly Survey of Plant Capacity Utilization](https://www.census.gov/data/tables/2020/econ/qpc/qpc-quarterly-tables.html)
- [Greenhouse Gas Reporting Program (GHGRP)](https://www.epa.gov/ghgreporting)

### People in the U.S.

- [ZIP Code Tabulation Area](https://en.wikipedia.org/wiki/ZIP_Code_Tabulation_Area)
- [ZIP Code Tabulation Areas (ZCTAs)](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)
- [ZCTA Data to Map](https://www2.census.gov/geo/docs/maps-data/data/rel/zcta_tract_rel_10.txt)

### Emissions

## Todo Checklist

A helpful checklist to gauge how your README is coming on what I would like to finish:

- [ ] Parsing of data for each energy data file
- [ ] Cleaning of data for each energy data file
- [ ] Storing useful tables into a Database in AWS or local server
- [ ] Analysis of energy data using visual tools of choice
- [ ] Mapping of the energy data for each energy type and total
- [ ] Predictions of energy alternatives
- [ ] Predictions of impacts from energy production sources

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

1. Fork this repository;
2. Create your branch: `git checkout -b my-new-feature`;
3. Commit your changes: `git commit -m 'Add some feature'`;
4. Push to the branch: `git push origin my-new-feature`.

**After your pull request is merged**, you can safely delete your branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more information.
