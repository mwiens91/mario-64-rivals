[![Build Status](https://travis-ci.com/mwiens91/mario-64-rivals.svg?branch=master)](https://travis-ci.com/mwiens91/mario-64-rivals)
[![codecov](https://codecov.io/gh/mwiens91/mario-64-rivals/branch/master/graph/badge.svg)](https://codecov.io/gh/mwiens91/mario-64-rivals)
[![Python version](https://img.shields.io/badge/python-3.5%20|%203.6%20|%203.7-blue.svg)](https://github.com/mwiens91/mario-64-rivals)

# Mario 64 Rivals

Mario 64 Rivals is an open-source web application for competing against
your best friends (dawww :heart:) in Mario 64.  While you're free to
host your own instance of it, I'm hosting mine at
[mario64rivals.ca](https://mario64rivals.ca) (come and have a look!).

## How does it work?

There are two main classes of records: course records and category
records. Course records involve getting stars in a particular course,
while category records can be essentially anything (the canonical 16,
70, and 120 star categories are included out of the box).

Users make records by selecting a record class, recording a video of
themselves making a record, and submitting their time along with a video
link. Mario 64 Rivals displays leaderboards for each type of record,
which users can look at see how great they are at Mario 64 :grin:.

## Tech stack

Mario 64 Rivals uses lots of tech. Its direct dependencies are

- [Django](https://www.djangoproject.com/) - the web framework for perfectionists with deadlines
- [PostgreSQL](https://www.postgresql.org/) - the world's most advanced open source database
- [jQuery](https://jquery.com/) - the write less, do more, JavaScript library
- [Bootstrap](https://getbootstrap.com/) - the most popular HTML, CSS, and JS library in the world
- [Popper.js](https://popper.js.org/) - a kickass library used to manage poppers in web applications
- [DataTables](https://datatables.net/) - table plug-in for jQuery
- [Waypoints](http://imakewebthings.com/waypoints/) - a library that makes it easy to execute a function whenever you scroll to an element
- [Font Awesome](https://fontawesome.com/) - the iconic SVG, font, and CSS toolkit
- [Rollbar](https://rollbar.com/) - error tracking & crash reporting for software developers

## Let me host this!

Alright! I'll show you have to get a local server running. Follow these
steps:

### Step 1: set up a Django-ready PostgreSQL database

If you're running Ubuntu, DigitalOcean's instructions are great:

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

### Step 2: let Mario 64 Rivals know about your database

From the base of this repository, copy [`.env.example`](.env.example) to
`.env` and fill in the `DATABASE_*` variables. All the other variables
you can leave as-is, although you may wish to set `DEBUG=True` if you
want to change the source code.

### Step 3: set up your environment

Using a virtual environment (or otherwise), install requirements with
pip by running

```
pip3 install -r requirements.txt
```

### Step 4: make database migrations

To get your database tables working with Mario 64 Rivals, run

```
./manage migrate
```

### Step 5: collect static files

This step is unnecessary if you set `DEBUG=True` in your `.env`;
otherwise, run

```
./manage collectstatic
```

### Step 6: create an admin account

Run

```
./manage createsuperuser
```

and follow the instructions that the command gives you.

### Step 7: run the server

Now you can run a local Mario 64 Rivals server with

```
./manage runserver
```
