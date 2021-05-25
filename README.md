This project contains a script that scrapes this [research facilities](https://navigator.innovation.ca/en/search) website.

to run the script, simply run

```bash
scrapy runspider -o output.csv scrape_projects.py
```

This site is perfect for crawling, because there are unique CSS classes for nearly field. For example, the institution name and location is

```css
#block-views-block-facility-block-facility-address > div > div > div > div > div > span
```

And the "what this facility does" section is described by:

```css
#block-mainpagecontent > article > div > div.clearfix.text-formatted.field.field--name-field-what-the-lab-facility-does.field--type-text-long.field--label-above > div.field__item
```

# Installing

```bash
python3 -m virtualenv venv/
pip install -r requirements.txt
source venv/bin/activate
# now you're ready to run scrapy...
```