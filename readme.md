# Candidate Profile Management API

## Introduction

This project provides a set of APIs for managing candidate profiles. The system revolves around two main collections: `user` and `candidate`. Users can perform various operations on candidate profiles, including creation, viewing, deletion, and updates. Additionally, users have the capability to search for specific candidates based on different criteria.

## Features

- **Create Candidate Profile:** Users can create detailed profiles for candidates, including information such as name, email, career level, job major, years of experience, education details, skills, nationality, location, salary, and gender.

- **View Candidate Profile:** Users can retrieve and view detailed information about a specific candidate.

- **Update Candidate Profile:** Users have the ability to update the details of an existing candidate profile.

- **Delete Candidate Profile:** Unwanted or outdated candidate profiles can be deleted from the system.

- **Search for Candidates:** Users can perform searches for candidates based on various criteria, facilitating efficient candidate retrieval.

- **Generate reports:** Users can generate report and download it as csv file.

## Technologies Used

- **FastAPI:** A modern, fast web framework for building APIs with Python.
  
- **MongoDB:** A NoSQL database used to store and manage candidate and user information.

## Prerequisites

- Ensure you have Docker and Docker Compose installed on your system.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/candidate-profile-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd candidatemanager
   ```

3. Build and start the application using Docker Compose:

   ```bash
   docker-compose up -d
   ```

   The FastAPI application and MongoDB will be launched.

4. Access the FastAPI application at [http://localhost:8000](http://localhost:8000).

## API Documentation

Explore the detailed API documentation and endpoints by accessing the Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs).

## Running Tests

Tests are meant to be executed in CI/CD pipelines. Set up your CI/CD configuration to run the tests.
you can run py.test.exe to perform the test

## NOTES

Due to certain issues encountered during Docker setup on Windows within the given time constraints, we recommend running the project on an Ubuntu environment using Docker.

#### Known Issues

- **Windows Compatibility**: Docker on Windows might encounter issues not present in Ubuntu. We suggest using Ubuntu for a smoother experience until Windows-specific problems are resolved.


