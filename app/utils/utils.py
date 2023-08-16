import csv
from typing import Optional
from fastapi import UploadFile, File
from sqlalchemy.orm import Session

def get_gln_cliente_from_upload_file(file: UploadFile):
    try:
        file.file.seek(0)
        content = file.file.read().decode('utf-8')
        lines = content.split("\n")
        csv_reader = csv.DictReader(lines)
        for row in csv_reader:
            return row.get('GLN_Cliente')
    except Exception as e:
        print(f"Error al procesar el archivo UploadFile: {str(e)}")
        return None
    
def count_records_in_file(file: UploadFile) -> int:
    file.file.seek(0)
    content = file.file.read().decode('utf-8')
    lines = content.split("\n")
    num_records = len(lines) - 1
    return num_records

def validate_flush(db: Session):
    try:
        db.flush()
    except Exception as e:
        db.rollback()
        raise e

def apply_changes(db: Session):
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()