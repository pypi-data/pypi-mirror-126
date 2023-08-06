# Celebrities-Births

This package allows you to get celebrities based on their birthdate, correlating to a date the user passes.

---

## How to install

```bash
pip install C3l3br1t1es-B1rth5-123142143523415
```

## Examples/How to use

```python
date = Date(29, 8, 1998)
scrape = Scraper()
wiki_date = date.to_wiki_format()
res = scrape.get_celebrities(wiki_date)
>>> #returns list of celebs born on the 29th August.
```