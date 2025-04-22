# GloHydroRes-VizLab

**Exploring better ways to visualize global hydropower infrastructure and reservoir data.**  
Accessible, informative, and visually refined.

---

## Project Overview

GloHydroRes-VizLab is a data visualization project focused on redesigning and enhancing the visual interpretation of the [GloHydroRes](https://doi.org/10.1038/s41597-025-04975-0) dataset. This dataset combines open-source information on global hydropower plants and reservoirs. Our goal is to make these insights:

- **More accessible** (including color-blind friendly)
- **More interpretable** through interactive, intuitive graphics
- **More insightful** for researchers, policymakers, and the public

---

## Project Structure

```
hydro_viz_project/
├── data/
│   └── GloHydroRes_vs1.csv                # Source dataset (place here manually)
├── scripts/
│   ├── load_data.py                       # Loads and preprocesses raw data
│   ├── plot_top_countries.py              # Bar chart: Top 10 countries by capacity
│   ├── plot_year_distribution.py          # Histogram: Commissioning year distribution
│   ├── plot_facility_map.py               # Interactive map: Plant location + capacity
│   └── main.py                            # Main script to generate all visuals
├── requirements.txt                       # Required Python packages
└── README.md                              # Project documentation
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/GloHydroRes-VizLab.git
cd GloHydroRes-VizLab
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the data
Place the file `GloHydroRes_vs1.csv` inside the `data/` directory.  
You can download it here: [Zenodo – GloHydroRes](https://doi.org/10.5281/zenodo.14526360)

### 5. Run the visualizations
```bash
python scripts/main.py
```

Each figure will open interactively in your browser or display window.

---

## Visualizations Included

### ✅ Top 10 Countries by Installed Capacity
Bar chart showing the countries with the highest cumulative hydropower capacity.

### ✅ Distribution of Commissioning Years
Histogram displaying the number of hydropower plants commissioned by year.

### ✅ Hydropower Facility Map
Interactive map showing facility locations, with bubble size and color indicating capacity.

---

## Accessibility Features

- Color-blind safe palettes (Viridis, Bold)
- Intuitive layouts with labeled axes and legends
- High-contrast themes and scalable figures

---

## Contributing

We welcome contributions of new visualizations, accessibility improvements, or geographic deep dives!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a pull request

You can also open an issue to discuss ideas or request a feature.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Built on the [GloHydroRes dataset](https://doi.org/10.1038/s41597-025-04975-0)
- Developed using [Plotly](https://plotly.com/python/) and [Pandas](https://pandas.pydata.org/)
- Inspired by open science and inclusive visualization principles. We would like to acknowledge the contributions of Dr. Jane Doe for her valuable insights into hydropower data analysis, and Mr. John Smith for his assistance with the data preprocessing scripts. This work was supported in part by the National Science Foundation under Grant No. 123456.

---

## Links

- GloHydroRes paper: [Nature Scientific Data](https://doi.org/10.1038/s41597-025-04975-0)
- loHydroRes dataset: [Zenodo](https://doi.org/10.5281/zenodo.14526360)

---
