import csv

from fastapi import HTTPException
from fastapi.responses import FileResponse
from app.repositories.candidates import CandidatesRepository


class ReportService:

    @staticmethod
    async def generate_report():
        # Retrieve candidate data from the database
        candidates = await CandidatesRepository.get_all_candidate()

        if not candidates:
            raise HTTPException(status_code=404, detail="No candidates found in the database.")

        # Define the CSV file path
        csv_file_path = "candidates_report.csv"

        # Create and write data to the CSV file
        with open(csv_file_path, "w", newline="") as csv_file:
            fieldnames = ["_id", "first_name", "last_name", "email", "UUID", "career_level", "job_major",
                          "years_of_experience", "degree_type", "skills", "nationality", "city", "salary", "gender"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for candidate in candidates:
                writer.writerow(candidate)

        # Serve the CSV file as a response
        return FileResponse(csv_file_path, headers={"Content-Disposition": "attachment; filename=candidates_report.csv"})