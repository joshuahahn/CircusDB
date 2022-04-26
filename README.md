# Circus DB

This project is a fullstack implementation of a database (PostgreSQL hosted on Google cloud) with frontend written in HTML and Python (Flask and SQLAlchemy). <br>
Server & Applications written by myself (Joshua Hahn) <br>
HTML templates written by Kayla Poulsen <br>
Completed for COMS W4111 Introduction to Databases in Columbia University

---

## Database Implementaition

The database is written on a **PostgreSQL** server hosted in Google Cloud. There are 8 tables, which follow complex structures including nested ISA relations and aggregate relations. Checks and triggers are included within the tables to maintain the integrity of data inserted into the tables.

---

## Frontend Implementation

Users accessing the database from the website can add and query entitites, as well as perform complex queries involving constraints and sorts. The server was written in **Python** using the **Flask** web framework, and queries were written and executed using **SQLAlchemy**. 
