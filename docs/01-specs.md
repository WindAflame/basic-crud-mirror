# Specs

## Objective

The goal of this project is to build a simple **BookStore** CRUD application, used as a coding dojo to experiment with different languages and frameworks.

## Architecture

The project is split into two independent services:

- **Backend** — exposes a REST API to manage books
- **Frontend** — consumes the backend API and displays the BookStore UI

Each service must be independently deployable. Any backend implementation must be interoperable with any frontend implementation, regardless of the language or framework used. This is guaranteed by a shared API contract defined in [02-resources.md](02-resources.md).

## Use case

A **BookStore** application that allows users to:

- View all books
- Add a new book
- Update an existing book
- Delete a book
